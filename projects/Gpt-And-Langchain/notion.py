import requests
import os
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()
import json
from datetime import datetime, timezone


token = os.getenv("NOTION_TOKEN")  # Notion token
dataset = os.getenv("DATABASE_ID")  # Notion Database

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22",
}


# Getting input from user and returning response Notionn Database
def createPage(title, youtube_url):
    createUrl = "https://api.notion.com/v1/pages"
    newPageData = {
        "parent": {"database_id": dataset},
        "properties": {
            "Descriptions": {
                "id": "title",
                "type": "title",
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": title,  # Title of the Project
                        },
                    }
                ],
            },
            "Youtube URL": {"url": youtube_url},  # title of youtube video
        },
    }
    data = json.dumps(newPageData)
    res = requests.request("POST", createUrl, headers=headers, data=data)
    print(res.status_code)
    if res.status_code == 200:
        return True
    else:
        False
