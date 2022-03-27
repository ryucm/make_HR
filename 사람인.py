from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
# 데이터를 받을 리스트
title_t = []
company_t = []
addr_t = []
link_t = []



# 5페이지까지 크롤링
for i in range(1,6):
    # 데이터 엔지니어 직무 크롤링
    url = f'https://www.saramin.co.kr/zf_user/search/recruit?searchword=%EB%8D%B0%EC%9D%B4%ED%84%B0+%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4&go=&flag=n&searchMode=1&searchType=auto&search_done=y&search_optional_item=n&recruitPage={i}&recruitSort=relation&recruitPageCount=40&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&show_applied=&quick_apply=&except_read=&mainSearch=n'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    request = Request(url, headers=headers)
    response = urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    # 제목
    title = soup.select('#recruit_info_list > div.content > div > div.area_job > h2 > a > span')
    for t in title:
        title_t.append(t.text)

    # 회사명
    company = soup.select('#recruit_info_list > div.content > div > div.area_corp > strong > a > span')
    for t in company:
        company_t.append(t.text)

    # 회사 위치
    addr = soup.select('#recruit_info_list > div.content > div > div.area_job > div.job_condition > span:nth-child(1)')
    for t in addr:
        addr_t.append(t.text)

    # 채용 공고 링크
    link = soup.select('#recruit_info_list > div.content > div > div.area_job > h2 > a')
    'https://www.saramin.co.kr' + link[0]['href']
    for l in link:
        link_t.append('https://www.saramin.co.kr' + l['href'])

# 데이터 저장
col = ['기업명', '제목', '주소', '링크']
data = pd.DataFrame(list(zip(company_t, title_t, addr_t, link_t)), columns=col)
data.to_csv('saramin.csv', index=False)
print("크롤링 완료")