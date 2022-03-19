from sys import stdin
import re

URLs = re.compile(r"(\w+)://([\w\d\.\_-]+)(:\d+)?(/.+)?")
DEFAULT = " <default>"

def urlParsing(url):
    protocol, host, port, path = URLs.match(url).groups()
    if port is None:
        port = DEFAULT
    if path is None:
        path = DEFAULT
    return {
        "Protocol": protocol,
        "Host": host,
        "Port": port[1:],
        "Path": path[1:],
    }
num_of_urls = int(stdin.readline())

for i in range(num_of_urls):
    url = stdin.readline().rstrip()
    result = urlParsing(url)
    
    print(f'URL #{i+1}')
    
    for j in result:
        print(f'{j:8} = {result[j]}')
    print()