#!/usr/bin/python3
"""
This task sends a request to the URL and displays the value of X-Request-Id
in the response header 
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
