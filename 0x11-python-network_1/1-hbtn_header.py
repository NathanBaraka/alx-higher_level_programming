#!/usr/bin/python3
"""
This taks we display the value of the X-Request-Id variable that is
found in the header of the response.
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
