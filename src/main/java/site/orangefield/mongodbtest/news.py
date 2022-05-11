import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.cursor import CursorType

# 1. 뉴스 20건 크롤링하기
# 2. 크롤링한 데이터 딕셔너리에 넣어주기

news_list = []

for a in range(1, 21):
    aid = str(a).zfill(10)

    news_dict = dict()
    # print(type(news_dict))

    try:
        html = requests.get(
            f"https://n.news.naver.com/mnews/article/005/{aid}?sid=100")

        # print(html.url.startswith('e', 8))

        if(html.status_code == 200):
            soup = BeautifulSoup(html.text, 'html.parser')

            if(html.url.startswith('n', 8)):

                title = soup.select_one(
                    ".media_end_head_title .media_end_head_headline").text
                createdAt = soup.select_one(
                    ".media_end_head_info_datestamp .media_end_head_info_datestamp_bunch .media_end_head_info_datestamp_time").text
                company = "국민일보"

            elif(html.url.startswith('e', 8)):

                title = soup.select_one(
                    ".end_ct_area .end_tit").text
                createdAt = soup.select_one(
                    ".article_info .author >em").text
                company = "국민일보"

            # 딕셔너리로 저장 완료인데 뭔가 이상하다. 된건가? 됐나보다. 됐다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            news_dict = {"title": title,
                         "company": company, "createdAt": createdAt}
            news_list.append(news_dict)
            print(type(title))

    except Exception as e:
        pass


#################################################################################################
def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


# Mongo 연결
mongo = MongoClient("localhost", 20000)

mongo_save(mongo, news_list, "emp", "navers")
