#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from datetime import datetime
from time import sleep, localtime
from gpiozero import LED


def lamp():
    led = LED(25)
    temp = localtime().tm_min
    while temp + 2 != localtime().tm_min:
        led.on()
        sleep(1)
        led.off()
        sleep(1)


def extract_jobs():
    """ Парсер """
    professional_role = ''
    text_profession = '&text=DevOps'
    area = '113'
    url = ('https://api.hh.ru/vacancies?clusters=true&enable_snippets=true&st'
           '=searchVacancy&only_with_salary=false' + str(professional_role) +
           str(text_profession) + '&per_page=100&area=' + str(area))

    headers = {
        'Host': 'api.hh.ru',
        'User-Agent': 'Safari',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    try:
        print('Headhunter: парсинг страницы')
        result = requests.get(url, headers)
        results = result.json()
        print('Найдено результатов:', results.get('found'))
        print('\n' + '*' * 150 + '\n')
        with open('_vacancies.txt', 'w', encoding='utf-8') as text:
            text.write(
                'Найдено результатов:' + str(results.get('found')) + '\n\n')
        items = results.get('items', {})
        for index in items:
            company = index['employer']['name']
            name = index['name']
            link = index["alternate_url"]
            types = index['type']['name']
            date = index['published_at'][:10]
            address = index['area']['name']
            if index['address']:
                address = index['address']['raw']
            salary = index['salary']
            text = open('_vacancies.txt', 'a', encoding='utf-8')
            if salary:
                from_salary = salary['from']
                to_salary = salary['to']
                output = ('  ' + str(company) + '  '.center(107, '*') +
                          '\n\n   Профессия: ' + str(name) + '\n   Зарплата: '
                          + str(from_salary) + ' - ' + str(to_salary) +
                          '\n   Ссылка: ' + str(link) + '\n   /' + str(types)
                          + '/ дата публикации: ' + str(date) +
                          '\n   Адрес: ' + str(address) + '\n')
                print(output)
                text.write(output.center(120, '*') + '\n')
            else:
                output = ('  ' + str(company) + '  '.center(107, '*') +
                          '\n\n   Профессия: ' + str(name) +
                          '\n   Зарплата:  не указана\n   Ссылка: ' +
                          str(link) + '\n   /' + str(types) +
                          '/ дата публикации: ' + str(date) +
                          '\n   Адрес: ' + str(address) + '\n')
                print(output)
                text.write(output.center(120, '*') + '\n')
            text.close()
            if (date == str(datetime.today())[:10]) and (
                    name.find('DevOps'.lower()) != -1):
                lamp()
                break
    except OSError as error:
        print(f'Статус: проблемы с доступом в интернет\n{error}')


extract_jobs()
