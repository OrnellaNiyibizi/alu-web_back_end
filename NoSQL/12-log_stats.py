#!/usr/bin/env python3
'''Task 12: Log stats
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.
    '''
    try:
        print('{} logs'.format(nginx_collection.count_documents({})))
        print('Methods:')
        methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
        for method in methods:
            req_count = nginx_collection.count_documents({'method': method})
            print('\tmethod {}: {}'.format(method, req_count))
        status_checks_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
        print('{} status check'.format(status_checks_count))
    except Exception as e:
        print("An error occurred:", e)


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        nginx_collection = client.logs.nginx
        print_nginx_request_logs(nginx_collection)
    except Exception as e:
        print("Failed to connect to MongoDB:", e)


if __name__ == '__main__':
    run()
