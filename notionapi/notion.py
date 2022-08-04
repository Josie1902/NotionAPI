# Import external python modules
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

# Import internal python modules
import json
import requests
import timeit

# Import functions from personal modules
from notionapi import loop
from notionapi import recursive


def display_json(res):
    """For error handling

    Args:
        res (response): response variable which gets/posts/patch from Notion API
    """
    # Retuns back a dictionary
    json_data = res.json()
    # Takes in dictionary and output formatted json
    formatted_json = json.dumps(json_data, indent=2)
    print(formatted_json)


# Data input
def content_format(*blocks):
    # List of main structure of the page
    main_children = []
    # Main structure of the page
    main_children.extend(blocks)
    return main_children


def get_database(database_id, headers):
    """Checks whether we are connected to the database

    Args:
        database_id (str): Id from notioin database (can be found in url)
        headers (dict): Permissions to Notion API
    
    Returns: 
        dict: Accessible dicts to be modified by user
    """
    # Get a list of pages from databse
    database_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    res = requests.post(database_url, headers=headers)
    # Make response editable as a json
    response_data = res.json()
    # Check for errors
    if res.status_code == 400 or res.status_code == 404 or res.status_code == 429:
        display_json(res)
    else:
        print(f"{res.status_code}: Successful response!")

    return response_data


def get_page_info_from_database(database_id, headers):
    """Get title, id, date and time (created_time) of the Notion page

    Args:
        database_id (str): Id from notioin database (can be found in url)
        headers (dict): Permissions to Notion API
    """

    response_data = get_database(database_id, headers)
    results = response_data["results"]

    # for result in results:
    # Check for keys in result
    # dict_keys(['object', 'id', 'created_time', 'last_edited_time', 'created_by', 'last_edited_by', 'cover', 'icon', 'parent', 'archived', 'properties', 'url'])
    # print(result.keys())

    with ThreadPoolExecutor(max_workers=3) as e:
        f1 = e.submit(loop.page_datetime_in_database, results)
        f2 = e.submit(loop.page_name_in_database, results)
        f3 = e.submit(loop.page_id_in_database, results)

    # Get title, id, date and time of the Notion page
    date_list, time_list = f1.result()
    name_list = f2.result()
    id_list = f3.result()

    # Create pandas dataframe
    data = {"Title": name_list, "Id": id_list, "Date": date_list, "Time": time_list}
    pd.set_option("display.max_columns", 5)
    df = pd.DataFrame(data)
    print(f"--- You are viewing pages of database {database_id} ---")
    print(df)


def create_page(
    database_id,
    headers,
    property_field,
    content_format=[],
    cover="https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2020/02/Usign-Gradients-Featured-Image.jpg",
    emoji="🗿",
):
    """Add a Notion page to a database with given properties and blocks

    Args:
        database_id (str): Id from Notion database (can be found in url)
        headers (dict): Permissions to Notion API
        property_field (dict): Requires properties
        content_format (list, optional): Add content. Defaults to [].
        cover (str, optional): Add cover page. Defaults to "https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2020/02/Usign-Gradients-Featured-Image.jpg".
        emoji (str, optional): Add cover emoji. Defaults to "🗿".
    
    Note:
        For properties, define them in the columns of your database first.
        If not, there would be a "property does not exist".
    """
    page_url = "https://api.notion.com/v1/pages"
    # Writing out the new page
    new_page = {
        "cover": {"type": "external", "external": {"url": cover}},
        "icon": {"type": "emoji", "emoji": emoji},
        "parent": {"type": "database_id", "database_id": database_id,},
        "properties": property_field,
        "children": content_format,
    }

    data = json.dumps(new_page)
    res = requests.post(page_url, headers=headers, data=data)
    # Check for errors
    if res.status_code == 400 or res.status_code == 404 or res.status_code == 429:
        display_json(res)
    else:
        print(f"{res.status_code}: Successful response!")


def update_page(page_id, headers, property_field):
    """You can only update page properties

    Args:
        page_id (str): Id from Notion page (can be found in url)
        headers (dict): Permissions to Notion API
    
    See Also:
        If you want to update the content (see below)
        update_block: The update replaces the entire value for a given block
        append_block: Creates and appends new children blocks to the parent block_id specified.
    """
    page_url = f"https://api.notion.com/v1/pages/{page_id}"
    update_data = {
        "properties": property_field,
    }
    data = json.dumps(update_data)

    res = requests.patch(page_url, headers=headers, data=data)

    # Check for errors
    if res.status_code == 400 or res.status_code == 404 or res.status_code == 429:
        display_json(res)
    else:
        print(f"{res.status_code}: Successful response!")


def delete_page(page_id, headers):
    """Archives the page

    Args:
        page_id (str): Id from Notion page (can be found in url)
        headers (dict): Permissions to Notion API
    """
    page_url = f"https://api.notion.com/v1/pages/{page_id}"
    # This is a page object
    update_data = {"archived": True}
    data = json.dumps(update_data)
    res = requests.patch(page_url, headers=headers, data=data)

    # Check for errors
    if res.status_code == 400 or res.status_code == 404 or res.status_code == 429:
        display_json(res)
    else:
        print(f"{res.status_code}: Successful response!")


def update_block(block_id, headers, content_format):
    """Updates the content of a block for the specified block_id based on the block type.
       The update replaces the entire value for a given field

    Args:
        block_id (str): Id from Notion page (can be found in url from copy link to block after #)
        headers (dict): Permissions to Notion API
    """
    block_url = f"https://api.notion.com/v1/blocks/{block_id}"
    data = json.dumps(content_format)
    res = requests.patch(block_url, headers=headers, data=data)

    # Check for errors
    if res.status_code == 400 or res.status_code == 404 or res.status_code == 429:
        display_json(res)
    else:
        print(f"{res.status_code}: Successful response!")


def append_blocks(block_id, headers, content_format):
    """Creates and appends new children blocks to the parent block_id specified.
       Much like nest blocks in a parent block

    Args:
        block_id (str): Id from Notion page (can be found in url from copy link to block after #)
        headers (dict): Permissions to Notion API
    """
    block_url = f"https://api.notion.com/v1/blocks/{block_id}/children"
    update_data = {"children": content_format}
    data = json.dumps(update_data)
    res = requests.patch(block_url, headers=headers, data=data)

    # Check for errors
    if res.status_code == 400 or res.status_code == 404 or res.status_code == 429:
        display_json(res)
    else:
        print(f"{res.status_code}: Successful response!")


def delete_block(block_id, headers):
    """Sets a Block object, including page blocks, to archived: true using the ID specified.

    Args:
        block_id (str): Id from Notion page (can be found in url from copy link to block after #)
        headers (dict): Permissions to Notion API
    """
    block_url = f"https://api.notion.com/v1/blocks/{block_id}"
    res = requests.delete(block_url, headers=headers)

    # Check for errors
    if res.status_code == 400 or res.status_code == 404 or res.status_code == 429:
        display_json(res)
    else:
        print(f"{res.status_code}: Successful response!")


def get_block_children(block_id, headers):
    """Get a list of block children objects from a parent block

    Args:
        block_id (str): Id from Notion page (can be found in url)
        headers (dict): Permissions to Notion API

    Returns:
        dict: Response data to be accessed and modified
    """
    block_url = f"https://api.notion.com/v1/blocks/{block_id}/children"
    res = requests.get(block_url, headers=headers)
    block_response_data = res.json()
    return block_response_data


def get_page_children(page_id, headers):
    """ Get a list of block objects from a page

    Args:
        page_id (str): Id from Notion page (can be found in url)
        headers (dict): Permissions to Notion API

    Returns:
        dict: Response data to be accessed and modified
    """
    page_url = f"https://api.notion.com/v1/blocks/{page_id}/children"
    res = requests.get(page_url, headers=headers)
    response_data = res.json()
    # Check for errors
    if res.status_code == 400 or res.status_code == 404 or res.status_code == 429:
        display_json(res)
    else:
        print(f"{res.status_code}: Successful response!")
        # display_json(res)
    return response_data


def get_page_content(page_id, headers):
    """ - REDACTED: Get name of blocks, its contents, id, parent_id and check whether they have children -

    Args:
        page_id (str): Id from Notion page (can be found in url)
        headers (dict): Permissions to Notion API
    
    See Also:
        get_page_content_threads: Same function but uses threading
    """
    response_data = get_page_children(page_id, headers)

    results = response_data["results"]

    block_list = recursive.recursive_blocks(results, headers)

    id_list = recursive.recursive_id(results, headers)

    has_children_list = recursive.recursive_has_children(results, headers)

    content_list = recursive.recursive_content(results, headers)

    parent_list = recursive.recursive_parent_id(results, headers)

    # Check list contents
    # print(block_list)
    # print(id_list)
    # print(has_children_list)
    # print(content_list)
    # print(parent_list)

    # Create pandas dataframe
    data = {
        "Block": block_list,
        "Id": id_list,
        "Content": content_list,
        "Has_children?": has_children_list,
        "Parent_id": parent_list,
    }
    pd.set_option("display.max_columns", 5)
    df = pd.DataFrame(data)
    print(f"--- You are viewing content of page: {page_id} ---")
    print(df)


def get_page_content_threads(page_id, headers):
    """Get name of blocks, its contents, id, parent_id and check whether they have children

    Args:
        page_id (str): Id from Notion page (can be found in url)
        headers (dict): Permissions to Notion API
    """
    response_data = get_page_children(page_id, headers)
    results = response_data["results"]

    with ThreadPoolExecutor(max_workers=5) as e:
        f1 = e.submit(recursive.recursive_blocks, results, headers)
        f2 = e.submit(recursive.recursive_id, results, headers)
        f3 = e.submit(recursive.recursive_has_children, results, headers)
        f4 = e.submit(recursive.recursive_content, results, headers)
        f5 = e.submit(recursive.recursive_parent_id, results, headers)

    # Check list contents
    # print(block_list)
    # print(id_list)
    # print(has_children_list)
    # print(content_list)
    # print(parent_list)

    # Get block (name), id, content and parent_id of the Notion block
    # and checks whether block has children

    block_list = f1.result()
    id_list = f2.result()
    has_children_list = f3.result()
    content_list = f4.result()
    parent_list = f5.result()

    # Create pandas dataframe
    data = {
        "Block": block_list,
        "Id": id_list,
        "Content": content_list,
        "Has_children?": has_children_list,
        "Parent_id": parent_list,
    }
    pd.set_option("display.max_columns", 5)
    df = pd.DataFrame(data)
    print(f"--- You are viewing content of page: {page_id} ---")
    print(df)
