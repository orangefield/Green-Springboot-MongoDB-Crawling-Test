import requests
from bs4 import BeautifulSoup

# html과 html_re를 합쳐야 한다! -> 합쳤다!!!

for a in range(1, 21):
    aid = str(a).zfill(10)

    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{aid}?sid=100")

        html_re = requests.get(
            f"https://entertain.naver.com/read?oid=005&aid={aid}")

        # print(html.url.startswith('e', 8))

        if(html.status_code == 200):
            soup = BeautifulSoup(html.text, 'html.parser')

            if(html.url.startswith('n', 8)):

                # 제목 나온다!
                title = soup.select_one(
                    ".media_end_head_title .media_end_head_headline")

                # 기사 작성일 나온다!
                createdAt = soup.select_one(
                    ".media_end_head_info_datestamp .media_end_head_info_datestamp_bunch .media_end_head_info_datestamp_time")

                # 회사명은 그냥 심어줬다!
                company = "국민일보"

            elif(html.url.startswith('e', 8)):
                title = soup.select_one(
                    ".end_ct_area .end_tit"
                )

                createdAt = soup.select_one(
                    ".article_info .author >em"
                )

                company = "국민일보"

            print(title)

    except Exception as e:
        pass
