import requests,re
from bs4 import BeautifulSoup

# 播放列表链接的URL
url = 'https://www.youtube.com/playlist?list=PLNm8RwrZU5PBSl8KrNGoPTe4jNVtSM8qu'

def get_v_url():
    # 发送HTTP GET请求并获取页面内容
    response = requests.get(url)
    # 获取页面的HTML代码
    html_content = response.text
    pattern = r"(?<=watch\?v=).*?(?=\")"
    # 使用re.findall获取所有匹配的字符串
    matches = re.findall(pattern, html_content)

    # 打印匹配结果
    for match in matches:
        print('https://www.youtube.com/watch?v='+match.split('\\')[0])


def get_v(url = 'https://www.youtube.com/watch?v=qFO7qLJZENQ'):
    go_url = 'https://service.iiilab.com/video/download'

    