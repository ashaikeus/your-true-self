from random import choice

first = ['Свято', 'Яро', 'Влади', 'Бого', 'Любо', 'Мило',
         'Свето', 'Миро', 'Добро', 'Бело', 'Брони', 'Изя']
second = ['слав', 'полк', 'мир', 'люб', 'рад', 'мил', 'волод', 'мир', 'мысл',
          'бор', 'зар', 'дан', 'став', 'гост', 'вид', 'во́да', 'ус', 'быт',
          'яр', 'свят', 'бой', 'гнев', 'мудр', 'лик', 'свет', 'нега', 'гор',
          'взор', 'слав', 'полк']
title = ['Мудрый', 'Грозный', 'Великий', 'Окаянный', 'Правосуд', 'Красный',
         'Тишайший', 'Милостивый', 'Кровавый', 'Солнышко', 'Боголюбский',
         'Калита', 'Большое Гнездо', 'Осмомысл', 'Блаженный', 'Вещий',
         'Завоеватель', 'Храбрый', 'Славный', 'Сильный', 'Хитрый', 'Креститель',
         'Мономах', 'Долгорукий', 'Гордый', 'Тёмный', 'Косой']

print(choice(first) + choice(second), choice(title))

