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

# Web scrapping component

# TO UPDATE: Web scrape netflix movie
res = requests.get("https://www.hbo.com/movies/last-night-in-soho")

# Check for errors getting URL
# print(res.raise_for_status())

soup = bs4.BeautifulSoup(res.text, "html.parser")

movie_title = soup.find("section", {"class": "hero-text"}).get_text()

description = soup.find("p", {"class": "text-left"}).get_text().strip()

# Check whether content was added
# print(movie_title)
# print(description)

# TO UPDATE: Movie poster, netflix page cover and page emoji

movie_poster = "https://m.media-amazon.com/images/M/MV5BZjgwZDIwY2MtNGZlNy00NGRlLWFmNTgtOTBkZThjMDUwMGJhXkEyXkFqcGdeQXVyMTEyMjM2NDc2._V1_.jpg"

HBO_page_cover = "https://play-lh.googleusercontent.com/ELLR6rcIP_mr6pB4kX9QhBKF-najkWHfb8RqceX4CBsyel3o_W9DoGas7WfPgfiIsQ"

page_emoji = "🥂"

# TO UPDATE: Property headers for Notion Page
Title = property.title(movie_title)
Status = property.select("Not started")
Genre = property.multi_select("Thriller")
Movie = property.select("Movie")
Review = property.select("Review Ongoing")

# Nothing needs to be changed unless otherwise from this point

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

# TO UPDATE: Property_field
property_field = {
    "Name": Title,
    "Status": Status,
    "Genre": Genre,
    "Program": Movie,
    "Review": Review,
}

# Checks whether database is successfully paired
# notion.get_database(database_id, headers)

# This portion formates the Notion Page

synopsis = block.paragraph(f"Synopsis: {description}")
review = block.paragraph("Review: ")
colomn_two = block.column(synopsis, review)
main_image = block.image(movie_poster)
colomn_one = block.column(main_image)
colomn_list = block.column_list(colomn_one, colomn_two)
content = notion.content_format(colomn_list)


notion.create_page(
    database_id, headers, property_field, content, HBO_page_cover, page_emoji,
)

# More Info
# Dataframe of pages and info from current database
# notion.get_page_info_from_database(database_id, headers)

# Dataframe of block info from current page
# notion.get_page_content("page_id", headers)

