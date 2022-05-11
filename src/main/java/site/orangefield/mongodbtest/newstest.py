import requests
from bs4 import BeautifulSoup

for a in range(1, 4):
    aid = str(a).zfill(10)

    html = requests.get(
        f"https://n.news.naver.com/mnews/article/005/{aid}?sid=100")
    html_re = requests.get(
        f"https://entertain.naver.com/read?oid=005&aid={aid}")

    # 여기선 되는데 왜 news.py에서는 안되나? if문의 문제인가
    if(html_re.status_code == 200):
        soup = BeautifulSoup(html_re.text, 'html.parser')

        title = soup.select_one(
            ".end_ct_area .end_tit")
        print(title)
