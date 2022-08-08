def title(content):
    """Insert title

    Args:
        content (str):Insert what you want to type

    Returns:
        dict: Placeholder dictionary for title to be used in "properties"
    """
    title_structure = ({"title": [{"text": {"content": content}}]},)
    return title_structure[0]


def text(
    content,
    color="default",
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
):
    """Insert text 

    Args:
        content (str): Insert what you want to type
        color (str, optional): Colour of text. Defaults to "default".
        bold (bool, optional): Bolds the text. Defaults to False.
        italic (bool, optional): Italicise the text. Defaults to False.
        strikethrough (bool, optional): Strikes through the text. Defaults to False.
        underline (bool, optional): Unerlines the text. Defaults to False.
        code (bool, optional): Text in code style. Defaults to False.

    Returns:
        dict: Placeholder dictionary for text to be used in "properties"
    
    Notes:
        colors: "default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", 
        "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", 
        "blue_background", "purple_background", "pink_background", "red_background"
    """
    text_structure = {
        "rich_text": [
            {
                "text": {"content": content},
                "annotations": {
                    "color": color,
                    "bold": bold,
                    "strikethrough": strikethrough,
                    "underline": underline,
                    "italic": italic,
                    "code": code,
                },
            }
        ]
    }
    return text_structure


def number(number):
    """Insert number

    Args:
        number (int): Insert number

    Returns:
        dict: Placeholder dictionary for number to be used in "properties"
    """
    number_structure = {"number": number}
    return number_structure


def select(name):
    """Select a tag

    Args:
        name (str): Give the tag a name

    Returns:
        dict: Placeholder dictionary for select to be used in "properties"
    """
    select_structure = {"select": {"name": name}}
    return select_structure


def multi_select(*names):
    """Select multiple tags

    Args:
        *names (str): Make multiple tags

    Returns:
        dict: Placeholder dictionary for multi-select to be used in "properties"
    """
    multi_tags = []
    for name in names:
        multi_tags.append({"name": name})
    multi_select_structure = {"multi_select": multi_tags}
    return multi_select_structure


def url(url):
    """Insert url

    Args:
        url (str): Insert url 

    Returns:
         dict: Placeholder dictionary for url to be used in "properties"
    """
    url_structure = {"Website": {"url": url}}
    return url_structure

