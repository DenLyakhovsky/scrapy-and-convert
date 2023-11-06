import json
import re
from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium import webdriver
from functions import headers, iteration, remove_symbols

# Збережені посилання на товар
goods_url = []


def collect_urls(page):
    """
    Функція збиває посилання карток
    :param page: кількість сторінок
    :return:
    """

    count = 1
    for pg in range(page):
        url = f'https://elomus-theme.myshopify.com/collections/all?page={pg}&sort_by=created-ascending'
        request = requests.get(url, headers=headers).text
        soup = BeautifulSoup(request, 'lxml')

        drones = soup.find_all(class_='product-thumb')
        for drone in drones:
            aa = drone.find(class_='item-inner').find(class_='caption').find(class_='product-name').find('a').get(
                'href')
            goods_url.append(f"https://elomus-theme.myshopify.com{aa}")
            sleep(2)
            print(f'Посилання готове: {count}')
            count += 1


# Усі дані з картки
goods_data = []


def collect_data(goods_url, page):
    """
    Функція, яка збирає необхідні дані в список "goods_data"
    :param goods_url: перемінна, яка містить посилання на картки товарів
    :param page: кількість сторінок
    :return:
    """

    driver = webdriver.Safari()

    count = 1

    # Збір даних в середині картки
    for url in goods_url:
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'lxml')

        title = soup.find(id='content').find(class_='col-sm-6 product-info-main').find('h2').text
        image = soup.find(id='product-product').find(id='content').find(id='wrap').find('a').get('href')
        tags = soup.find(id='product-product').find(class_='product-info-detailed').find(class_='tags').find_all('a')

        sleep(1.5)
    driver.quit()

    # Збір даних на сторінці з категоріями
    for pg in range(page):
        url = f'https://elomus-theme.myshopify.com/collections/all?page={pg}&sort_by=created-ascending'
        request = requests.get(url, headers=headers).text
        soup = BeautifulSoup(request, 'lxml')

        drones = soup.find_all(class_='item-inner')

        for drone in drones:
            data = drone.find(class_='button-group action-links').find(class_='button btn-quickview quickview').get(
                'data-productinfo')

            sleep(2)

            # Збираю id та options
            idd = re.search(r'"id":(\d+)', data).group()[5:]
            options = re.findall(r'"options":\s*\[([^\]]+)\]', data)

            print(f'Картка готова: {count}')
            count += 1

            # Додаю все у список
            goods_data.append({
                'ID': idd,
                'title': title,
                'img': f'https:{image}',
                'tags': [i.text for i in tags],
                'published_at': iteration(data, 'published_at'),
                'created_at': iteration(data, 'created_at'),
                'updated_at': iteration(data, 'updated_at'),
                'vendor': iteration(data, 'vendor'),
                'options': remove_symbols(options),
            })


if __name__ == '__main__':
    collect_urls(1)
    collect_data(goods_url, 1)

# Збереження даних в JSON формат
with open('data.json', 'w', encoding='UTF-8') as file:
    json.dump(goods_data, file, indent=2, ensure_ascii=False)
