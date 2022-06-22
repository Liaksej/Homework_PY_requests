import requests


class SuperHeroes:
    def __init__(self, *sueperheroes):
        self.superheroes = sueperheroes

    def superheroes_list(self):
        url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
        response = requests.get(url=url)
        return response.json()

    def sueperheroest_special_list(self):
        our_heroes_list = []
        for item in self.superheroes_list():
            name = item['name']
            if name in self.superheroes:
                our_heroes_list.append(item)
        return our_heroes_list

    def cleverest_super_heroe(self):
        """Функция определяет, кто из выбранных супергероев самый умный.

        Можно добавлять в качестве аргументов сколько угодно героев. В случае одинаковых показателей
         будут выводиться все герои, имеющие наивысший одинаковый показатель."""
        sorted_ours_heroes_list = sorted(self.sueperheroest_special_list(),
                                         key=(lambda x: x['powerstats']['intelligence']), reverse=True)
        list_cleverest_superheroes = [sorted_ours_heroes_list[0]['name']]
        for hero in sorted_ours_heroes_list[1:]:
            if hero['powerstats']['intelligence'] == sorted_ours_heroes_list[0]['powerstats']['intelligence']:
                list_cleverest_superheroes.append(hero['name'])
                return (f'Самыми умными супергероями из {len(self.superheroes)} героев {self.superheroes} '
                        f'являются {", ".join(list_cleverest_superheroes).upper()}. \nПоказатели их умственных '
                        f'спообностей - {sorted_ours_heroes_list[0]["powerstats"]["intelligence"]} из 100.')
        else:
            return (f'Самым умным супергероем из {len(self.superheroes)} героев {self.superheroes} '
                    f'является {(sorted_ours_heroes_list[0]["name"]).upper()}, \nпоказатель его умственных '
                    f'спообностей - {sorted_ours_heroes_list[0]["powerstats"]["intelligence"]} из 100.')


if __name__ == '__main__':
    search = SuperHeroes('Thor', 'Captain America', 'Iron Man')
    print(search.cleverest_super_heroe())
