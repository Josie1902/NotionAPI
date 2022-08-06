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

description_list = []
title_list = []

base_link = "https://myanimelist.net/anime/47194/Summertime_Render/"
episodes_link = base_link + "episode"

# TO UPDATE: Web scrape myanimelist
res = requests.get(episodes_link)

# Check for errors getting URL
# print(res.raise_for_status())

soup = bs4.BeautifulSoup(res.text, "html.parser")

# TO UPDATE: network page cover, emoji and series poster
network_page_cover = "https://www.awn.com/sites/default/files/styles/original/public/image/featured/summertime_rendering-cropped.jpg?itok=eoFSYucb"
page_emoji = "🌊"
series_poster = "https://m.media-amazon.com/images/M/MV5BOGNjYmZlZGItODg2MC00NWYxLTkyYjktYzFjZmJkMmNmYjYwXkEyXkFqcGdeQXVyMTEzMTI1Mjk3._V1_FMjpg_UX1000_.jpg"
series_title = soup.find("h1", {"class": "title-name"}).get_text()

# TO UPDATE: Property headers for Notion Page
Title = property.title(series_title)
Status = property.select("Not started")
Genre = property.multi_select("Anime")
Series = property.select("Series")
Review = property.select("Review Ongoing")


def get_descriptions(soup):
    descriptions = soup.find_all("h2", {"class": "fw-b"})
    for description in descriptions:
        description_text = description.next_sibling.strip()
        if description_text == "":
            description_list.append("Synopsis pending")
        else:
            description_list.append(description_text)


def get_titles(soup):
    titles = soup.find_all("h2", {"class": "fs18 lh11"})
    for title in titles:
        title_text = title.get_text().strip()
        title_list.append(title_text)


# Get titles, description and episode images from myanimelist
with ThreadPoolExecutor(max_workers=3) as e:
    episode_links = soup.find_all("a", {"class": "fl-l fw-b"})
    for episode_link in episode_links:
        link = episode_link["href"]
        res = requests.get(link)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        e.submit(get_titles, soup)
        e.submit(get_descriptions, soup)

# Check content
# print(description_list)
# print(title_list)

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
        synopsis = block.paragraph(description_list[i])
        toggle = block.toggle(f"{episode_title}", synopsis)
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
    database_id, headers, property_field, content, network_page_cover, page_emoji,
)

# More Info
# Dataframe of pages and info from current database
# notion.get_page_info_from_database(database_id, headers)

# Dataframe of block info from current page
# notion.get_page_content("page_id", headers)

