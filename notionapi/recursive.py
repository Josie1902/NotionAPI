# Import functions from personal modules
import notionapi.notion as notion

# Empty lists
block_list = []
id_list = []
content_list = []
has_children_list = []
parent_list = []


def recursive_blocks(results, headers):
    """Get block name of page recursively 

     Args:
        results (dict): Accessing th key of the main dictionary given by Notion API
        headers (dict): Permissions to Notion API
    """
    for result in results:
        # print(result)
        has_children = result["has_children"]
        id = result["id"]
        list_of_keys = list(result.keys())
        last_element = len(list_of_keys) - 1
        block = list_of_keys[last_element]
        block_list.append(block)

        if has_children == True:
            block_with_children = notion.get_block_children(id, headers)
            results = block_with_children["results"]
            recursive_blocks(results, headers)

    return block_list


def recursive_id(results, headers):
    """Get block id of page recursively 

     Args:
        results (dict): Accessing th key of the main dictionary given by Notion API
        headers (dict): Permissions to Notion API
    """
    for result in results:
        # print(result)
        has_children = result["has_children"]
        id = result["id"]
        id_list.append(id)

        if has_children == True:
            block_with_children = notion.get_block_children(id, headers)
            results = block_with_children["results"]
            recursive_id(results, headers)

    return id_list


def recursive_has_children(results, headers):
    """Checks whether block has children recursively - True/False

    Args:
        results (dict): Accessing th key of the main dictionary given by Notion API
        headers (dict): Permissions to Notion API
    """
    for result in results:
        # print(result)
        has_children = result["has_children"]
        id = result["id"]
        has_children_list.append(has_children)

        if has_children == True:
            block_with_children = notion.get_block_children(id, headers)
            results = block_with_children["results"]
            recursive_has_children(results, headers)

    return has_children_list


def recursive_content(results, headers):
    """Get block content recursively 

     Args:
        results (dict): Accessing th key of the main dictionary given by Notion API
        headers (dict): Permissions to Notion API
    """
    for result in results:
        # print(result)
        has_children = result["has_children"]
        id = result["id"]
        list_of_keys = list(result.keys())
        last_element = len(list_of_keys) - 1
        block = list_of_keys[last_element]
        block_content = result[block]

        if block_content == {}:
            content = "---"
            content_list.append(content)
            if has_children == True:
                block_with_children = notion.get_block_children(id, headers)
                results = block_with_children["results"]
                recursive_content(results, headers)
        else:
            if "rich_text" in block_content:
                rich_text = block_content["rich_text"]
                text = rich_text[0]["text"]
                content = text["content"]
                content_list.append(content)
                if has_children == True:
                    block_with_children = notion.get_block_children(id, headers)
                    results = block_with_children["results"]
                    recursive_content(results, headers)
            else:
                content_list.append("- MEDIA -")
                if has_children == True:
                    block_with_children = notion.get_block_children(id, headers)
                    results = block_with_children["results"]
                    recursive_content(results, headers)

    return content_list


def recursive_parent_id(results, headers):
    """Get parent id recursively

    Args:
        results (dict): Accessing th key of the main dictionary given by Notion API
        headers (dict): Permissions to Notion API
    """
    for result in results:
        # print(result)
        has_children = result["has_children"]
        id = result["id"]
        parent = result["parent"]

        if "page_id" in parent:
            parent_id = result["parent"]["page_id"]
            parent_list.append(f"page: {parent_id}")
            if has_children == True:
                block_with_children = notion.get_block_children(id, headers)
                results = block_with_children["results"]
                recursive_parent_id(results, headers)

        else:
            parent_id = result["parent"]["block_id"]
            parent_list.append(f"block: {parent_id}")
            if has_children == True:
                block_with_children = notion.get_block_children(id, headers)
                results = block_with_children["results"]
                recursive_parent_id(results, headers)

    return parent_list
