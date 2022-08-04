# Import secret
import os
from dotenv import load_dotenv
from dotenv import dotenv_values

# Import functions from personal modules
from notionapi import notion
from notionapi import block
from notionapi import property

# Import scrapping modules
import bs4
import requests

# Import python modules
from concurrent.futures import ThreadPoolExecutor

# TO UPDATE: Web scrape netflix
res = requests.get("https://www.netflix.com/sg/title/81280924")

# Check for errors getting URL
# print(res.raise_for_status())

soup = bs4.BeautifulSoup(res.text, "html.parser")

# TO UPDATE: page cover, emoji and series poster
page_cover = (
    "https://i.pcmag.com/imagery/reviews/05cItXL96l4LE9n02WfDR0h-5..v1582751026.png"
)
page_emoji = "🎸"
series_poster = "https://occ-0-2706-2705.1.nflxso.net/dnm/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAABdjWxFr68018gShUbIIpIpwER-TcxdyKqLXWUrWXF6TcrROGcm1Zd4BVrv_QX9SXhzyUUpnmxT2ElNCXWmFv16A7anV6cWFEGqqMcVesef7jzIkiuuSAsyXUqv76pcaLFh9ccg.jpg"
series_title = soup.find(class_="title-title").get_text()

# TO UPDATE: Property headers for Notion Page
Title = property.title(series_title)
Status = property.select("Not started")
Genre = property.multi_select("Documentary")
Series = property.select("Series")
Review = property.select("Review Ongoing")


# Nothing needs to be changed unless otherwise from this point
# Web scrapping component

# Empty list to be linked into Notion API
description_list = []
title_list = []
image_list = []


def get_descriptions():
    descriptions = soup.find_all(class_="epsiode-synopsis")
    for description in descriptions:
        description_text = description.get_text().strip()
        description_list.append(description_text)


def get_titles():
    titles = soup.find_all("h3", {"class": "episode-title"})
    for title in titles:
        title_text = title.get_text()
        title_list.append(title_text)


def get_episode_images():
    images = soup.find_all("img", {"class": "episode-thumbnail-image"})
    for image in images:
        link = image["src"]
        image_list.append(link)


# Get titles, description and episode images from IMDB
with ThreadPoolExecutor(max_workers=3) as e:
    e.submit(get_titles)
    e.submit(get_descriptions)
    e.submit(get_episode_images)

# Check whether content was added
# print(description_list)
# print(title_list)
# print(image_list)
# print(movie_title)

# Load secrets
load_dotenv()

config = dotenv_values(".env")
MY_NOTION_TOKEN = os.getenv("MY_NOTION_TOKEN")
database_id = os.getenv("DATABASE_ID")

# Check env variables
# print(MY_NOTION_TOKEN)
# print(database_id)

# Notion API component
# Headers
headers = {
    "Authorization": f"Bearer {MY_NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

property_field = {
    "Name": Title,
    "Status": Status,
    "Genre": Genre,
    "Program": Series,
    "Review": Review,
}

# Checks whether database is successfully paired
# notion.get_database(database_id, headers)

# This portion formates the Notion Page
# Empty list for children blocks of page
children_blocks = []


def column(block):
    """A single column

    Returns:
       dict : Placeholder dictionary for column to be used in "children"
    """
    children_blocks.append(block)

    column_structure = {
        "object": "block",
        "type": "column",
        "column": {"children": children_blocks},
    }
    return column_structure


def get_episodes_colomn():
    """Formats toggles with the episode synopsis into one coloumn

    Returns:
        dict: The dictionary for the coloumn to be used into coloumn list
    """
    for i in range(len(title_list)):
        episode_title = title_list[i]
        episode_image = block.image(image_list[i])
        synopsis = block.paragraph(description_list[i])
        toggle = block.toggle(f"{episode_title}", synopsis, episode_image)
        episodes_colomn = column(toggle)
    return episodes_colomn


colomn_two = get_episodes_colomn()

main_image = block.image(series_poster)

# More page formating (you don't have to look at this)
colomn_one = block.column(main_image)
colomn_list = block.column_list(colomn_one, colomn_two)
overall_review = block.paragraph("Overall Review", color="gray_background")
content = notion.content_format(colomn_list, overall_review)

notion.create_page(
    database_id, headers, property_field, content, page_cover, page_emoji,
)

# More Info
# Dataframe of pages and info from current database
# notion.get_page_info_from_database(database_id, headers)

# Dataframe of block info from current page
# notion.get_page_content_threads("6540eb7151044bbc9023733108468dab", headers)

