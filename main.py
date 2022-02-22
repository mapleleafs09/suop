import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'когда', 'мне']

headers = {

'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Site': 'none',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36' }

url = 'https://habr.com/ru/all/'
base_ulr = 'https://habr.com'
res = requests.get(url, headers=headers)
# print(res.text)


soup = bs4.BeautifulSoup(res.text, 'html.parser')
articles = soup.find_all('article')
# print(articles)

result_set = set()

for article in articles:
    article_set = set()
    texts_v2 = article.find_all(class_="article-formatted-body article-formatted-body_version-2")

    link = article.find(class_="tm-article-snippet__title-link").attrs['href']
    name = article.find(class_='tm-article-snippet__title-link')
    data = article.find('time').attrs['title']
    for text in texts_v2:
        link = base_ulr + link
                # print(text.text)
        for key in KEYWORDS:
            if key in text.text.lower():


                article_set.add(name.text)
                article_set.add(data)
                article_set.add(link)
                # print(tuple(article_set))
                result_set.add(tuple(article_set))


# print(result_set)
for result in result_set:
    for final_result in result:
        print(final_result)




