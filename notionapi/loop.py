# Import functions from personal modules
from notionapi import simpletime


def page_datetime_in_database(results):
    """Returns back the date and time of creation of each page

     Args:
       results (dict): Accessing th key of the main dictionary given by Notion API

    Returns:
        list: A list for date and time when the page was created respectively
    """
    date_list = []
    time_list = []

    for result in results:
        created_time = result["created_time"]
        # Simplify ISO 8601 into date and time strings
        date_time = simpletime.simple_time(created_time)
        # Get date in %d/%m/%Y format
        date = date_time[0]
        date_list.append(date)
        # Get time in am/pm format
        time = date_time[1]
        time_list.append(time)

    return date_list, time_list


def page_id_in_database(results):
    """Returns back the ids of each page

     Args:
       results (dict): Accessing th key of the main dictionary given by Notion API

    Returns:
        list: A list of page ids
    """
    id_list = []

    for result in results:
        # Get url from result key
        url = result["url"]
        # Remove front segment from url
        name_and_id = url.replace("https://www.notion.so/", "")
        # split into a list of elements from -
        seperate_name_and_id = name_and_id.split("-")
        # There is a title and id to the page
        if len(seperate_name_and_id) > 1:
            last_element = len(seperate_name_and_id) - 1
            # Get id
            id = seperate_name_and_id.pop(last_element)
            id_list.append(id)
        # There is only id to the page
        else:
            # Get id
            id = " ".join(seperate_name_and_id)
            id_list.append(id)

    return id_list


def page_name_in_database(results):
    """Returns back the titles of each page

    Args:
       results (dict): Accessing th key of the main dictionary given by Notion API

    Returns:
        list: A list of page titles
    """
    name_list = []

    for result in results:
        # Get url from result key
        url = result["url"]
        # Remove front segment from url
        name_and_id = url.replace("https://www.notion.so/", "")
        # split into a list of elements from -
        seperate_name_and_id = name_and_id.split("-")
        # There is a title and id to the page
        if len(seperate_name_and_id) > 1:
            # get rid of id_portion
            last_element = len(seperate_name_and_id) - 1
            seperate_name_and_id.pop(last_element)
            # Get name
            name = " ".join(seperate_name_and_id)
            name_list.append(name)
        # There is only id to the page
        else:
            # Get name
            name = "--No Title--"
            name_list.append(name)

    return name_list
