import json
from urllib import request

import re


def write(content):
    with open('myresult.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def parse_one_page(html):
    pre = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?name.*?a.*?>(\w+)</a>.*?star.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.RegexFlag.S)
    html = html.decode('utf-8')
    print(html)
    items = re.findall(pre, html)
    for item in items:
        yield{
            'index':item[0],
            'title': item[1],
            'actor': item[2].strip()[3:],
            'score': item[3] + item[4]
        }
if __name__ == "__main__":
    l=[x * 10 for x in range(10)]
    for i in l:
        response = request.urlopen("http://maoyan.com/board/4?offset="+str(i))
        html = response.read()
        for item in parse_one_page(html):
            print(item)
            write(item)