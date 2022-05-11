import requests
from bs4 import BeautifulSoup

html = requests.get(
    f"https://n.news.naver.com/mnews/article/005/0000000001?sid=100")

news_dict = dict()


if(html.status_code == 200):
    soup = BeautifulSoup(html.text, 'html.parser')

    # 제목 나온다! -
    title = soup.select_one(
        ".media_end_head_title .media_end_head_headline")

    # 기사 작성일 나온다!
    createdAt = soup.select_one(
        ".media_end_head_info_datestamp .media_end_head_info_datestamp_bunch .media_end_head_info_datestamp_time")

    # 회사명은 그냥 심어줬다!
    company = "국민일보"

    # 아 딕셔너리 만들어졌네!
    news_dict["title", "createdAt, company"] = title, createdAt, company
    print(news_dict)
