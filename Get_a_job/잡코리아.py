from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
# 데이터를 받을 리스트
title_t = []
company_t = []
addr_t = []
link_t = []

# 5페이지까지 크롤링
for i in range(1, 6):
    # 데이터 엔지니어 직무 크롤링
    url = f'https://www.jobkorea.co.kr/Search/?stext=%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4&tabType=recruit&Page_No={i}'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    request = Request(url, headers=headers)
    response = urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    # 제목
    title = soup.select('.post-list-info > a')
    for t in title:
        title_t.append(t.text.strip())
    # 회사명
    company = soup.select('.post-list-corp > a')
    for t in company:
        company_t.append(t.text.strip())
    # print(company_t)
        

    # 회사 위치
    addr = soup.select('.post-list-info > p > .loc.long')
    for t in addr:
        addr_t.append(t.text)

    # 채용 공고 링크
    link = soup.select('.post-list-corp > a')
    'https://www.jobkorea.co.kr/' + link[0]['href']
    for l in link:
        link_t.append('https://www.jobkorea.co.kr/' + l['href'])

# 데이터 저장
col = ['기업명', '제목', '주소', '링크']
data = pd.DataFrame(list(zip(company_t, title_t, addr_t, link_t)), columns=col)
data.to_csv('jobkorea.csv', index=False)
print("크롤링 완료")