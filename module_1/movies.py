import pandas as pd
import chardet
import numpy as np
from collections import Counter

movies = pd.read_csv('C:/Users/Sergei/Downloads/movie_bd_v5.csv', delimiter=',')

# columns: 'imdb_id', 'budget', 'revenue', 'original_title', 'cast', 'director',
#        'tagline', 'overview', 'runtime', 'genres', 'production_companies',
#        'release_date', 'vote_average', 'release_year

# Вопрос 1. У какого фильма из списка самый большой бюджет?
# каждый ответ дан вместе с функцией print(), но она удалена, чтобы всё не перемешивалось в консоле
movies[movies.budget == movies.budget.max()].original_title

# Вопрос 2. Какой из фильмов самый длительный (в минутах)?
movies[movies.runtime == movies.runtime.max()].original_title

# Вопрос 3. Какой из фильмов самый короткий (в минутах)?
movies[movies.runtime == movies.runtime.min()].original_title

# Вопрос 4. Какова средняя длительность фильмов?
round(movies.runtime.mean())

# Вопрос 5. Каково медианное значение длительности фильмов?
round(movies.runtime.median())

# Внимание! Здесь и далее под «прибылью» или «убытками» понимается разность между сборами и бюджетом фильма.
# Прибыль = сборы - бюджет (profit = revenue - budget).

# Вопрос 6. Какой фильм самый прибыльный?
movies['profit'] = movies['revenue'] - movies['budget']
movies[movies.profit == movies.profit.max()].original_title


# Вопрос 7. Какой фильм самый убыточный?
movies[movies.profit == movies.profit.min()].original_title

# Вопрос 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?
len(movies[movies.profit > 0].value_counts())

# Вопрос 9. Какой фильм оказался самым кассовым в 2008 году?
movies_2008 = movies[movies.release_year == 2008]
movies_2008[movies_2008.revenue == movies_2008.revenue.max()].original_title

# Вопрос 10. Самый убыточный фильм за период с 2012 по 2014 годы (включительно)?
#print(movies.query('(2012 <= release_year <= 2014) & (profit == profit.min())'))
movies_1214 = movies.query('2012 <= release_year <= 2014')
movies_1214[movies_1214.profit == movies_1214.profit.min()].original_title

# Вопрос 11. Какого жанра фильмов больше всего?
#def genres_count(genres):
#    genres_ = {
#        'Comedy': 0, 'Drama': 0, 'Romance': 0, 'Horror': 0, 'Thriller': 0, 'Action': 0, 'Adventure': 0
#    }
#    if genres.find('Comedy'):
#        genres_['Comedy'] += 1
#    elif genres.find('Drama'):
#        genres_['Drama'] += 1
#    elif genres.find('Romance'):
#        genres_['Romance'] += 1
#    elif genres.find('Horror'):
#        genres_['Horror'] += 1
#    elif genres.find('Thriller'):
#        genres_['Thriller'] += 1
#    elif genres.find('Action') >= 0:
#        genres_['Action'] += 1
#    elif genres.find('Adventure') >= 0:
#        genres_['Adventure'] += 1
#    return genres_

movies_genres = movies.genres.str.split('|')
movies_genres = movies_genres.explode()
#print(movies_genres.value_counts().max())

# Вопрос 12. Фильмы какого жанра чаще всего становятся прибыльными?
movies_profit = movies[movies.profit > 0].copy() # выбираем только прибыльные фильмы
movies_profit.genres = movies_profit.genres.str.split('|') # разделяем жарны на списки
movies_profit = movies_profit.explode('genres') # разделяем списки
movies_profit.genres.value_counts() # выводим список прибыльных жанров


# Вопрос 13. У какого режиссёра самые большие суммарные кассовые сборы?
movies_director = movies.copy()
movies_director.director = movies_director.director.str.split('|') # разделяем режиссёров на списки
movies_director = movies_director.explode('director') # разделяем списки
movies_director = movies_director.groupby(['director'])['revenue'].sum() # группируем режиссёров и сумму их сборов
movies_director.sort_values(ascending=False) # выводим список режиссёров и сумму их сборов

# Вопрос 14. Какой режиссер снял больше всего фильмов в стиле Action?
director_genres = movies[movies.genres.str.contains('Action')].copy() # создаём ДБ только с фильмами Action
director_genres.director = director_genres.director.str.split('|')
director_genres = director_genres.explode('director')
director_genres.director.value_counts() # выводим список режиссёров, снимавших такие фильмы

# Вопрос 15. Фильмы с каким актером принесли самые высокие кассовые сборы в 2012 году?
movies_cast = movies[movies.release_year == 2012].copy() # выбираем фильмы 2012 года
movies_cast.cast = movies_cast.cast.str.split('|') # разделяем актёров по спискам
movies_cast = movies_cast.explode('cast') # делим списки
movies_cast = movies_cast.groupby(['cast'])['revenue'].sum() # группируем сумму сборов по актёрам
movies_cast.sort_values(ascending=False) # выводим список актёров, сортируя по сумме сборов

# Вопрос 16. Какой актер снялся в большем количестве высокобюджетных фильмов?
# Примечание: в фильмах, где бюджет выше среднего по данной выборке.
cast_budget = movies[movies.budget > movies.budget.mean()].copy() # выбираем фильмы с высоким бюджетом
cast_budget.cast = cast_budget.cast.str.split('|') # разделяем актёров по спискам
cast_budget = cast_budget.explode('cast') # делим списки
cast_budget.cast.value_counts() # выводим сколько раз актёры снимались в таких фильмах

# Вопрос 17. В фильмах какого жанра больше всего снимался Nicolas Cage?
movies_cage = movies[movies.cast.str.contains('Nicolas Cage')].copy() # выбираем фильмы с Николасом
movies_cage.genres = movies_cage.genres.str.split('|') # делим жанры по спискам
movies_cage = movies_cage.explode('genres') # разбиваем списки жарнам
movies_cage.genres.value_counts() # выводим список жанров, в которых снимался Кейдж