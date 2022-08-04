import json


def paragraph(
    content,
    color="default",
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
    link=None,
):
    """Nested child block of the main_paragraph block.

    Args:
        content (str): Insert a paragraph 
        color (str, optional): Choose a colour. Defaults to "default".
        bold (bool, optional): Bolds the text. Defaults to False.
        italic (bool, optional): Italicise the text. Defaults to False.
        strikethrough (bool, optional): Strikes through the text. Defaults to False.
        underline (bool, optional): Unerlines the text. Defaults to False.
        code (bool, optional): Text in code style. Defaults to False.
        link (str,optional): Inline link in this text. Defaults to None.

    Returns:
        dict: Placeholder dictionary for nested paragraph to be used in "children"
    
    Notes:
        colors: "default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", 
        "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", 
        "blue_background", "purple_background", "pink_background", "red_background"
    
    See Also: 
        main_paragraph: Main paragraph block
    """
    nested_paragraph_structure = {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content, "link": link},
                    "annotations": {
                        "bold": bold,
                        "strikethrough": strikethrough,
                        "underline": underline,
                        "italic": italic,
                        "code": code,
                    },
                }
            ],
            "color": color,
        },
    }

    return nested_paragraph_structure


def main_paragraph(
    content,
    *nestedblocks,
    color="default",
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
    link=None,
):
    """Main paragraph block

    Args:
        content (str): Insert what you want to type
        color (str, optional): Colour of text. Defaults to "default".
        bold (bool, optional): Bolds the text. Defaults to False.
        italic (bool, optional): Italicise the text. Defaults to False.
        strikethrough (bool, optional): Strikes through the text. Defaults to False.
        underline (bool, optional): Unerlines the text. Defaults to False.
        code (bool, optional): Text in code style. Defaults to False.
        link (str,optional): Inline link in this text. Defaults to None.

    Returns:
        dict: Placeholder dictionary for paragraph to be used in "children"
    
    Notes:
        colors: "default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", 
        "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", 
        "blue_background", "purple_background", "pink_background", "red_background"
    
    See Also:
        paragraph: Nested child block of the main_paragraph block.
    
    Example:
        one = block.paragraph("I am a child", "red", True)
        two = block.paragraph("I am also another child", "blue", underline=True)
        main_paragraph("This is the main paragraph", one, two, color="gray_background", strikethrough=True)
    """
    children_blocks = []
    for nestedblock in nestedblocks:
        children_blocks.append(nestedblock)

    main_paragraph_structure = {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content, "link": link},
                    "annotations": {
                        "bold": bold,
                        "strikethrough": strikethrough,
                        "underline": underline,
                        "italic": italic,
                        "code": code,
                    },
                }
            ],
            "color": color,
            "children": children_blocks,
        },
    }
    return main_paragraph_structure


def heading_1(
    content,
    color="default",
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
    link=None,
):
    """Heading 1

    Args:
        content (str): Insert what you want to type
        color (str, optional): Colour of text. Defaults to "default".
        bold (bool, optional): Bolds the text. Defaults to False.
        italic (bool, optional): Italicise the text. Defaults to False.
        strikethrough (bool, optional): Strikes through the text. Defaults to False.
        underline (bool, optional): Unerlines the text. Defaults to False.
        code (bool, optional): Text in code style. Defaults to False.
        link (str,optional): Inline link in this text. Defaults to None.

    Returns:
        dict: dict: Placeholder dictionary for heading 1 to be used in "children"
    """
    heading_1_structure = {
        "object": "block",
        "type": "heading_1",
        "heading_1": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content, "link": link},
                    "annotations": {
                        "bold": bold,
                        "strikethrough": strikethrough,
                        "underline": underline,
                        "italic": italic,
                        "code": code,
                    },
                }
            ],
            "color": color,
        },
    }
    return heading_1_structure


def heading_2(
    content,
    color="default",
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
    link=None,
):
    """Heading 2

    Args:
        content (str): Insert what you want to type
        color (str, optional): Colour of text. Defaults to "default".
        bold (bool, optional): Bolds the text. Defaults to False.
        italic (bool, optional): Italicise the text. Defaults to False.
        strikethrough (bool, optional): Strikes through the text. Defaults to False.
        underline (bool, optional): Unerlines the text. Defaults to False.
        code (bool, optional): Text in code style. Defaults to False.
        link (str,optional): Inline link in this text. Defaults to None.

    Returns:
        dict: dict: Placeholder dictionary for heading 2 to be used in "children"
    """
    heading_2_structure = {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content, "link": link},
                    "annotations": {
                        "bold": bold,
                        "strikethrough": strikethrough,
                        "underline": underline,
                        "italic": italic,
                        "code": code,
                    },
                }
            ],
            "color": color,
        },
    }
    return heading_2_structure


def heading_3(
    content,
    color="default",
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
    link=None,
):
    """Heading 3

    Args:
        content (str): Insert what you want to type
        color (str, optional): Colour of text. Defaults to "default".
        bold (bool, optional): Bolds the text. Defaults to False.
        italic (bool, optional): Italicise the text. Defaults to False.
        strikethrough (bool, optional): Strikes through the text. Defaults to False.
        underline (bool, optional): Unerlines the text. Defaults to False.
        code (bool, optional): Text in code style. Defaults to False.
        link (str,optional): Inline link in this text. Defaults to None.

    Returns:
        dict: dict: Placeholder dictionary for heading 3 to be used in "children"
    """
    heading_3_structure = {
        "object": "block",
        "type": "heading_3",
        "heading_3": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content, "link": link},
                    "annotations": {
                        "bold": bold,
                        "strikethrough": strikethrough,
                        "underline": underline,
                        "italic": italic,
                        "code": code,
                    },
                }
            ],
            "color": color,
        },
    }
    return heading_3_structure


def heading_1_toggle(
    content,
    *nestedblocks,
    color="default",
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
    link=None,
):
    """Heading 1 toggle

    Args:
        content (str): Insert what you want to type
        color (str, optional): Colour of text. Defaults to "default".
        bold (bool, optional): Bolds the text. Defaults to False.
        italic (bool, optional): Italicise the text. Defaults to False.
        strikethrough (bool, optional): Strikes through the text. Defaults to False.
        underline (bool, optional): Unerlines the text. Defaults to False.
        code (bool, optional): Text in code style. Defaults to False.
        link (str,optional): Inline link in this text. Defaults to None.

    Returns:
        dict: dict: Placeholder dictionary for heading 1 toggle to be used in "children"
    """

    children_blocks = []
    for nestedblock in nestedblocks:
        children_blocks.append(nestedblock)

    heading_1_toggle_structure = {
        "object": "block",
        "type": "heading_1",
        "heading_1": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content, "link": link},
                    "annotations": {
                        "bold": bold,
                        "strikethrough": strikethrough,
                        "underline": underline,
                        "italic": italic,
                        "code": code,
                    },
                }
            ],
            "color": color,
            "children": children_blocks,
        },
    }
    return heading_1_toggle_structure


def heading_2_toggle(
    content,
    *nestedblocks,
    color="default",
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
    link=None,
):
    """Heading 2 toggle

    Args:
        content (str): Insert what you want to type
        color (str, optional): Colour of text. Defaults to "default".
        bold (bool, optional): Bolds the text. Defaults to False.
        italic (bool, optional): Italicise the text. Defaults to False.
        strikethrough (bool, optional): Strikes through the text. Defaults to False.
        underline (bool, optional): Unerlines the text. Defaults to False.
        code (bool, optional): Text in code style. Defaults to False.
        link (str,optional): Inline link in this text. Defaults to None.

    Returns:
        dict: dict: Placeholder dictionary for heading 2 toggle to be used in "children"
    """

    children_blocks = []
    for nestedblock in nestedblocks:
        children_blocks.append(nestedblock)

    heading_2_toggle_structure = {
        "object": "block",
        "type": "heading_2",
        "heading_2": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content, "link": link},
                    "annotations": {
                        "bold": bold,
                        "strikethrough": strikethrough,
                        "underline": underline,
                        "italic": italic,
                        "code": code,
                    },
                }
            ],
            "color": color,
            "children": children_blocks,
        },
    }
    return heading_2_toggle_structure


def heading_3_toggle(
    content,
    *nestedblocks,
    color="default",
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
    link=None,
):
    """Heading 3 toggle

    Args:
        content (str): Insert what you want to type
        color (str, optional): Colour of text. Defaults to "default".
        bold (bool, optional): Bolds the text. Defaults to False.
        italic (bool, optional): Italicise the text. Defaults to False.
        strikethrough (bool, optional): Strikes through the text. Defaults to False.
        underline (bool, optional): Unerlines the text. Defaults to False.
        code (bool, optional): Text in code style. Defaults to False.
        link (str,optional): Inline link in this text. Defaults to None.

    Returns:
        dict: dict: Placeholder dictionary for heading 3 toggle to be used in "children"
    """

    children_blocks = []
    for nestedblock in nestedblocks:
        children_blocks.append(nestedblock)

    heading_3_toggle_structure = {
        "object": "block",
        "type": "heading_3",
        "heading_3": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content, "link": link},
                    "annotations": {
                        "bold": bold,
                        "strikethrough": strikethrough,
                        "underline": underline,
                        "italic": italic,
                        "code": code,
                    },
                }
            ],
            "color": color,
            "children": children_blocks,
        },
    }
    return heading_3_toggle_structure


def toggle(
    content,
    *nestedblocks,
    color="default",
    bold=False,
    italic=False,
    strikethrough=False,
    underline=False,
    code=False,
    link=None,
):
    """A simple toggle

    Args:
        content (str): Insert what you want to type
        color (str, optional): Colour of text. Defaults to "default".
        bold (bool, optional): Bolds the text. Defaults to False.
        italic (bool, optional): Italicise the text. Defaults to False.
        strikethrough (bool, optional): Strikes through the text. Defaults to False.
        underline (bool, optional): Unerlines the text. Defaults to False.
        code (bool, optional): Text in code style. Defaults to False.
        link (str,optional): Inline link in this text. Defaults to None.

    Returns:
        dict: Placeholder dictionary for toggle to be used in "children"
    """
    children_blocks = []
    for nestedblock in nestedblocks:
        children_blocks.append(nestedblock)

    toggle_structure = {
        "object": "block",
        "type": "toggle",
        "toggle": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": content, "link": link},
                    "annotations": {
                        "bold": bold,
                        "strikethrough": strikethrough,
                        "underline": underline,
                        "italic": italic,
                        "code": code,
                    },
                }
            ],
            "color": color,
            "children": children_blocks,
        },
    }

    return toggle_structure


def embed(url):
    """Link to website the embed block will display.

    Args:
        url (str): Link to website you want to embed

    Returns:
        dict: Placeholder dictionary for embed block to be used in "children"
    """
    embed_structure = {"object": "block", "type": "embed", "embed": {"url": url}}
    return embed_structure


def image(url):
    """Includes supported image urls (i.e. ending in .png, .jpg, .jpeg, .gif, .tif, .tiff, .bmp, .svg, or .heic)

    Args:
        url (str): Link address of image 

    Returns:
        dict: Placeholder dictionary for image to be used in "children"
    """
    image_structure = {
        "object": "block",
        "type": "image",
        "image": {"type": "external", "external": {"url": url},},
    }
    return image_structure


def video(url):
    """Includes supported video urls (e.g. ending in .mkv, .flv, .gifv, .avi, .mov, .qt, .wmv, .asf, .amv, .mp4, .m4v, .mpeg, .mpv, .mpg, .f4v, etc.)

    Args:
        url (str): Link address to video

    Returns:
       dict: Placeholder dictionary for video to be used in "children"
    """
    video_structure = {
        "object": "block",
        "type": "video",
        "video": {"type": "external", "external": {"url": url}},
    }
    return video_structure


def bookmark(url):
    """Bookmark link

    Args:
        url (str): Link you want to bookmark

    Returns:
        dict: Placeholder dictionary for bookmark block to be used in "children"
    """
    bookmark_structure = {
        "object": "block",
        "type": "bookmark",
        "bookmark": {"url": url},
    }
    return bookmark_structure


def table_of_content(color="default"):
    """Displays table_of_content

    Args:
        color (str, optional): Colour of text. Defaults to "default".

    Returns:
        dict: Placeholder dictionary for table of content block to be used in "children"
    
    Notes:
        colors: "default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", 
        "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", 
        "blue_background", "purple_background", "pink_background", "red_background"
    """
    table_of_content_structure = {
        "object": "block",
        "type": "table_of_contents",
        "table_of_contents": {"color": color},
    }
    return table_of_content_structure


def divider():
    """A line across the page

    Returns:
        dict: Placeholder dictionary for table of divider block to be used in "children"
    """
    divider_structure = {"object": "block", "type": "divider", "divider": {}}
    return divider_structure


def column_list(*columnblocks):
    """Columns read from right to left according to added arguments 

    Args:
        columnblock (var): A variable from column function 

    Returns:
        dict : Placeholder dictionary for column list to be used in "children"
    """
    column_list_children = []
    for column in columnblocks:
        column_list_children.append(column)

    column_list_structure = {
        "object": "block",
        "type": "column_list",
        "column_list": {"children": column_list_children},
    }
    return column_list_structure


def column(*nestedblocks):
    """A single column

    Returns:
       dict : Placeholder dictionary for column to be used in "children"
    """
    children_blocks = []
    for nestedblock in nestedblocks:
        children_blocks.append(nestedblock)

    column_structure = {
        "object": "block",
        "type": "column",
        "column": {"children": children_blocks},
    }
    return column_structure


def callout(content, *nestedblocks, emoji="💡", color="gray_background"):
    """Callout block

    Args:
        content (str): Insert a paragraph
        emoji (str, optional): Choose an emoji. Defaults to "". 
        color (str, optional): Choose a colour. Defaults to "default".

    Returns:
        dict : Placeholder dictionary for callout to be used in "children"

    Notes:
        colors: "default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", 
        "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", 
        "blue_background", "purple_background", "pink_background", "red_background"
    """
    children_blocks = []
    for nestedblock in nestedblocks:
        children_blocks.append(nestedblock)

    callout_structure = {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": [{"type": "text", "text": {"content": content,},}],
            "icon": {"emoji": emoji},
            "color": color,
            "children": children_blocks,
        },
    }
    return callout_structure


def quote(content, color="default"):
    """Quote block

    Args:
        content (str): Insert a paragraph
        color (str, optional): Choose a colour. Defaults to "default".

    Returns:
        dict : Placeholder dictionary for quote to be used in "children"

    Notes:
        colors: "default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", 
        "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", 
        "blue_background", "purple_background", "pink_background", "red_background"
    """
    quote_structure = {
        "object": "block",
        "type": "quote",
        "quote": {
            "rich_text": [{"type": "text", "text": {"content": content,},}],
            "color": color,
        },
    }
    return quote_structure


def bulleted_list(content, *nestedblocks, color="default", link="None"):
    """Create bulleted points

    Args:
        content (str): Insert content
        color (str, optional): Choose a colour. Defaults to "default".
        link (str, optional): Insert a link. Defaults to "None".

   Returns:
        dict : Placeholder dictionary for bulleted list to be used in "children"

    Notes:
        colors: "default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", 
        "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", 
        "blue_background", "purple_background", "pink_background", "red_background"
    """
    children_blocks = []
    for nestedblock in nestedblocks:
        children_blocks.append(nestedblock)
    bullet_list_structure = {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [{"type": "text", "text": {"content": content, "link": link}}],
            "color": color,
            "children": children_blocks,
        },
    }
    return bullet_list_structure


def numbered_list_item(content, *nestedblocks, color="default", link="None"):
    """Create numbered points

   Args:
        content (str): Insert content
        color (str, optional): Choose a colour. Defaults to "default".
        link (str, optional): Insert a link. Defaults to "None".

   Returns:
        dict : Placeholder dictionary for numbered list to be used in "children"

    Notes:
        colors: "default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", 
        "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", 
        "blue_background", "purple_background", "pink_background", "red_background"
    """
    children_blocks = []
    for nestedblock in nestedblocks:
        children_blocks.append(nestedblock)
    numbered_list_structure = {
        "object": "block",
        "type": "numbered_list_item",
        "numbered_list_item": {
            "rich_text": [{"type": "text", "text": {"content": content, "link": link}}],
            "color": "default",
            "children": children_blocks,
        },
    }
    return numbered_list_structure


def to_do(content, checked=False, *nestedblocks, color="default", link="None"):
    """Create to dos

   Args:
        content (str): Insert content
        checked (bool,optional): Choose either False for untick or True to tick. Defaults to False.
        color (str, optional): Choose a colour. Defaults to "default".
        link (str, optional): Insert a link. Defaults to "None".

   Returns:
        dict : Placeholder dictionary for to dos to be used in "children"

    Notes:
        colors: "default", "gray", "brown", "orange", "yellow", "green", "blue", "purple", "pink", "red", 
        "gray_background", "brown_background", "orange_background", "yellow_background", "green_background", 
        "blue_background", "purple_background", "pink_background", "red_background"
    """
    children_blocks = []
    for nestedblock in nestedblocks:
        children_blocks.append(nestedblock)
    to_do_structure = {
        "object": "block",
        "type": "to_do",
        "to_do": {
            "rich_text": [{"type": "text", "text": {"content": content, "link": link}}],
            "checked": checked,
            "color": color,
            "children": children_blocks,
        },
    }
    return to_do_structure


def child_page(title):
    """Add a child page

    Args:
        title (str): Insert name of page

    Returns:
        dict : Placeholder dictionary for child page to be used in "children"
    """
    child_page_structure = {
        "type": "child_page",
        "child_database": {"title": title},
    }
    return child_page_structure


def child_database(title):
    """Add a child database

    Args:
        title (str): Insert name of page

    Returns:
        dict : Placeholder dictionary for child database to be used in "children"
    """
    child_database_structure = {
        "type": "child_database",
        "child_database": {"title": title},
    }
    return child_database_structure


def pdf(url):
    """Add PDF file reference

    Args:
        url (str): Insert link to pdf

    Returns:
       dict : Placeholder dictionary for pdf to be used in "children"
    """
    pdf_structure = {
        "type": "pdf",
        "pdf": {"type": "external", "external": {"url": url}},
    }
    return pdf_structure


def file(url):
    """Add file

    Args:
        url (str): Insert link to pdf

    Returns:
       dict : Placeholder dictionary for pdf to be used in "children"
    """
    file_structure = {
        "type": "file",
        "file": {
            "type": "external",
            "external": {"url": "https://website.domain/files/doc.txt"},
        },
    }
    return file_structure


# print(json.dumps(main, indent=2))
