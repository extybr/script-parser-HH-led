from db_connection import redis_connection


class Database:
    count_vacancies = 0

    @staticmethod
    def delete_keys() -> None:
        """
        Удаление данных.
        :return: None
        """
        redis_connection.flushdb()  # удаление всех ключей в текущей базе
        redis_connection.flushall()  # убрать все ключи во всех БД

    def insert_database(self, count_vacancies: int, count: int, company: str,
                        name: str, from_salary: int | float | str,
                        to_salary: int | float | str, link: str, types: str,
                        date: str, schedule: str, address: str) -> None:
        """
        Добавление в базу данных.
        :param count_vacancies: int
        :param count: int
        :param company: str
        :param name: str
        :param from_salary: int or float or str
        :param to_salary: int or float or str
        :param link: str
        :param types: str
        :param date: str
        :param schedule: str
        :param address: str
        :return: None
        """
        self.count_vacancies = count_vacancies
        head = {'company': str(company), 'name': str(name),
                'from_salary': str(from_salary),
                'to_salary': str(to_salary), 'link': str(link),
                'types': str(types), 'date': str(date),
                'schedule': str(schedule), 'address': str(address)}
        redis_connection.hset(str(count), mapping=head)

    def read_database(self) -> str:
        """
        Передача данных с базы данных.
        :return: str
        """
        for number in range(1, self.count_vacancies + 1):
            result = redis_connection.hgetall(name=str(number))
            if result:
                yield (f'  {result["company"]}  '.center(107, '*') +
                       f'\n\n🚮   Профессия: {result["name"]}'
                       f'\n😍   Зарплата: {result["from_salary"]}'
                       f' - {result["to_salary"]}'
                       f'\n⚜   Ссылка: {result["link"]}'
                       f'\n🐯   /{result["types"]}/   -🌼-   дата публикации: '
                       f'{result["date"]}   -🌻-   график работы: '
                       f'{result["schedule"]}'
                       f'\n🚘   Адрес: {result["address"]}\n')


database = Database()
