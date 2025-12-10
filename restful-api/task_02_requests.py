#!/usr/bin/python3
"""
Task: Consuming and processing data from an API using Python.
"""
import requests
import csv
API_URL = "https://jsonplaceholder.typicode.com/posts"
def fetch_and_print_posts():
    response = requests.get(API_URL)
    print(f"Status code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))
def fetch_and_save_posts():
    response = requests.get(API_URL)
    if response.status_code == 200:
        posts = response.json()
        data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
