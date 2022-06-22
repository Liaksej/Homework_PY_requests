import requests
import time


class SearchStackoverflow:

    def electionorder(self):
        print('Выберите порядок сортировки:\n')
        print('1 - по убыванию;')
        print('2 - по возрастанию;')
        print('любая клавиша - сортировка по умолчанию.')
        while True:
            order = input('\nВвести значение: ')
            print()
            if order == '2':
                order = 'asc'
                break
            else:
                order = 'desc'
                break
        return order

    def stackoverflow_list(self):
        url = 'https://api.stackexchange.com/2.3/search'
        order = self.electionorder()
        unix_day = 86400
        fromdate_time = (int(time.time()) - unix_day * 2)
        params = {'fromdate': fromdate_time,
                  'order': order,
                  'sort': 'creation',
                  'tagged': 'python',
                  'site': 'stackoverflow'}
        response = requests.get(url=url, params=params)
        return response.json()

    def titles_extractor(self):
        search_result = self.stackoverflow_list()
        print('Список вопросов из stackoverflow за день:\n')
        for item in search_result['items']:
            print(f'{item["title"]} - дата создания - '
                  f'{time.strftime("%d.%m.%Y", time.localtime(item["creation_date"]))}')
        print()
        print(f'Всего найдено вопросов за последние ДВА дня: {len(search_result["items"])} '
              f'(максимальное количеств выдачи для API - 30).')


if __name__ == '__main__':
    search = SearchStackoverflow()
    search.titles_extractor()   # Выдача может быть не более 30 значений
