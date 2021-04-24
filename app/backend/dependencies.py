import os
import urllib3
import json


'''
Creates a HTTP client for our backend to communicate with the GraphQL API
'''


def prepare(query):
    url = 'https://api.plantjammer.com/graphql'
    http = urllib3.PoolManager()
    headers = {
        "Authorization": os.environ.get("API_KEY")}
    r = http.request('POST', url, fields=query, headers=headers)
    data = json.loads(r.data.decode('utf-8'))
    return data
