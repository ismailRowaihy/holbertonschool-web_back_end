#!/usr/bin/env python3
""" this module provides some stats about nginx logs """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    list_data = list(collection.find())

    m_get = 0
    m_post = 0
    m_put = 0
    m_patch = 0
    m_delete = 0
    s_check = 0

    for i in list_data:
        if i.get("method") is None:
            continue
        elif i.get("method") == "GET":
            m_get += 1
            if i.get("path") == "/status":
                s_check += 1
        elif i.get("method") == "POST":
            m_post += 1
        elif i.get("method") == "PUT":
            m_put += 1
        elif i.get("method") == "PATCH":
            m_patch += 1
        elif i.get("method") == "DELETE":
            m_delete += 1

    logs = len(list_data)
    print(f"{logs} logs")
    print(
        f"Methods:\n\tmethod GET: {m_get}\
    \n\tmethod POST: {m_post}\n\tmethod PUT: {m_put}\
    \n\tmethod PATCH: {m_patch}\n\tmethod DELETE: {m_delete}"
    )
    print(f"{s_check} status check")
