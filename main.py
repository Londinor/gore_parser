from config import *
from text_editing import Format
import requests
from bs4 import BeautifulSoup as bs

headers = {"accept": "*/*",
           "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

#base_url = "https://lenta.ru/articles/2019/08/16/hole/"

#print(lets_start)  # функция лежит в конфиге
url = lets_start #Стартуем и показываем поле для ввода url
url = "".join(url.split())  # Избавляемся от неожиданных пробелов в полученном URL


#def tex_pars(base_url, headers): #было
def tex_pars(url, headers): #стало
    raw_text = []
    session = requests.Session()
    #request = session.get(base_url, headers=headers) #было
    request = session.get(url, headers=headers) #стало
    if request.status_code == 200:
        soup = bs(request.content, "html.parser")
        divs = soup.find_all("div", attrs={"class": "b-topic__content"})

        settings = cfg[0]
        tag, where = settings["where"]
        content = settings["text"]
        table = soup.find(tag, class_=where)

        for temp in content:  # Обработка ссылок:
            for row in table.find_all(temp):  # На данном этапе разработки ссылки мы просто удаляем,
                for item in row.find_all('a'):  # оставляя просто текст.
                    item = item.text  # Это можно исправить прямо в этой строчке, да..

        for temp in content:
            for row in table.find_all(temp):
                raw_text.append(row.text)


    sth = Format(raw_text, width)
    good_text = sth.done()

    save_file = open("parser_closed.txt", "w")
    for s in good_text:
        save_file.write(s + "\n")


        print("Иследование завершено")
    else:
        print("ERROR")



if __name__ == '__main__':
    tex_pars(url, headers)
