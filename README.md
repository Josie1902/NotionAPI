# NotionAPI

Simple functions to implement Notion API into your automation projects

# Usage

## Setting up

1. Set up your bot:
   [Notion API Getting Started](https://pages.github.com/)

2. Install these modules

   > pip install beautifulsoup4

   > pip install requests

3. Make an .env file to store your NOTION_API_TOKEN and IDs

   Example:

   ```

   MY_NOTION_TOKEN = "Input bot token"

   DATABASE_ID = "Input database id"

   ```

# Notes

Modules Available:

1. block: Input blocks into a page
2. property: Deals with notion property field
3. notion: Get, patch, delete or update databases, pages and blocks

# Examples

## Create a Page

```
database_id = ""

headers = {

    "Authorization": f"Bearer {MY_NOTION_TOKEN}",

    "Content-Type": "application/json",

    "Notion-Version": "2022-06-28",
}


property_field = {"Name": Title, "Status": Status, "Genre": Genre, "Program": Movie, "Review": Review,}

page_cover = ""

colomn_one = block.column(main_image)

colomn_list = block.column_list(colomn_one, colomn_two)

overall_review = block.paragraph("Overall Review", color="gray_background")

content = notion.content_format(colomn_list, overall_review)

notion.create_page(
    database_id, headers, property_field, content, page_cover, page_emoji,
)

```

## Append Children Blocks

```
text = block.paragraph("I am a child", "red")

quote = block.quote("An extra quote child")

append_children = notion.content_format(text, quote)

notion.append_blocks(block_id, headers, append_children)

```

# Project

## Scrape movie and series info into a Notion Page

1. netflixmovie.py: scrape movie title and synopsis.
2. netflixseries.py: scrape title, synopsis and images of each episode.
