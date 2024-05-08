import json, requests
import sqlite3


def handle(content):
    if not content or content is None:
        content = None
    return content


def dump(endpoint, toget):
    headers = {"User-agent": "Chrome"}
    unique = set()
    url = (
        "http://www.reddit.com/r/python/" + str(endpoint) + "/.json?limit=" + str(toget)
    )
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    # parsed = json.dumps(data, indent = 4, sort_keys = True)
    return data


def _news(data, toget, unique):
    for i in range(toget):
        parsed_content = json.dumps(data["data"]["children"][i]["data"], indent=4)
        content_title = handle(data["data"]["children"][i]["data"]["title"].strip())
        content_text = handle(data["data"]["children"][i]["data"]["selftext"].strip())
        content_author = handle(
            data["data"]["children"][i]["data"]["author_fullname"].strip()
        )
        content_ups = handle(data["data"]["children"][i]["data"]["ups"])
        content_url = handle(data["data"]["children"][i]["data"]["url"].strip())
        content_id = handle(data["data"]["children"][i]["data"]["id"])

        post = (
            content_id,
            content_title,
            content_text,
            content_author,
            content_url,
            content_ups,
        )
        update_post = (
            content_title,
            content_text,
            content_author,
            content_url,
            content_ups,
            content_id,
        )

        if content_id in unique:
            c.execute(
                "UPDATE top_news SET ptitle = ?, ptext = ?, pauthor = ?, purl = ?, pups = ? where pid = ? ",
                update_post,
            )
            print("Updated")
        else:
            unique.add(content_id)
            c.execute("INSERT INTO top_news VALUES (?, ?, ?, ?, ?, ?)", post)
            print("Inserted")
        i = i + 1


def get_top_news(endpoint="top", toget=10):
    def connect():
        c.execute(
            """CREATE TABLE IF NOT EXISTS top_news
	             	(pid text PRIMARY KEY, ptitle text, ptext text, pauthor text, purl text, pups int)"""
        )

    connect()
    unique = set()
    data = dump(endpoint, toget)
    _news(data, toget, unique)


def get_hot_news(endpoint="hot", toget=10):
    def connect():
        c.execute(
            """CREATE TABLE IF NOT EXISTS hot_news
	             	(pid text PRIMARY KEY, ptitle text, ptext text, pauthor text, purl text, pups int)"""
        )

    connect()
    unique = set()
    data = dump(endpoint, toget)
    _news(data, toget, unique)


def reddit_get():
    conn = sqlite3.connect("reddit_news.db")
    c = conn.cursor()
    get_top_news()
    conn.commit()
    conn.close()
