import json
import sqlite3


def get_movie_by_title(title):
    con = sqlite3.connect("netflix.db")  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"""
               SELECT title, country, release_year, listed_in, description
               FROM netflix
               WHERE title LIKE  '%{title}%'
               ORDER BY title DESC
               LIMIT 1
    """
    data = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchone()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД

    result = {
        "title": data[0],
        "country": data[1],
        "release_year": data[2],
        "genre": data[3],
        "description": data[4]
    }

    with open('movie_by_title.json', 'w') as outfile:
        json.dump(result, outfile)

    with open('movie_by_title.json', 'r', encoding='utf-8') as file:
        movies_json = json.load(file)

        return movies_json


def get_movie_by_year(year_from, year_to):
    con = sqlite3.connect("netflix.db")  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"""
               SELECT title, release_year
               FROM netflix
               WHERE release_year BETWEEN {year_from} AND {year_to}
               ORDER BY title DESC
               LIMIT 100
    """
    data = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД

    result = []

    for item in data:
        result.append(
            {
                'title': item[0],
                'release_year': item[1],
            }
        )

    with open('movie_by_year.json', 'w') as outfile:
        json.dump(result, outfile)

    with open('movie_by_year.json', 'r', encoding='utf-8') as file:
        movies_json = json.load(file)

        return movies_json


def get_movie_by_rating(rating):
    con = sqlite3.connect("netflix.db")  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"""
               SELECT title, rating, description
               FROM netflix
            
    """
    if rating == 'children':
        sqlite_query += 'WHERE rating = "G"'
    elif rating == 'family':
        sqlite_query += 'WHERE rating = "G" OR rating = "PG" OR rating = "PG-13"'
    elif rating == 'adult':
        sqlite_query += 'WHERE rating = "R" OR rating = "NC-17"'
    else:
        return f"where is no movies with this rating"

    data = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД

    result = []

    for item in data:
        result.append(
            {
                'title': item[0],
                'rating': item[1],
                'description': item[2],
            }
        )

    with open('movie_by_rating.json', 'w') as outfile:
        json.dump(result, outfile)

    with open('movie_by_rating.json', 'r', encoding='utf-8') as file:
        movies_json = json.load(file)

        return movies_json


def get_movie_by_genre(genre):
    con = sqlite3.connect("netflix.db")  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"""
               SELECT title, description
               FROM netflix
               WHERE listed_in LIKE '%{genre}%'
               ORDER BY date_added DESC
               LIMIT 10

    """

    data = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД

    result = []

    for item in data:
        result.append(
            {
                'title': item[0],
                'description': item[1],
            }
        )

    with open('movie_by_genre.json', 'w') as outfile:
        json.dump(result, outfile)

    with open('movie_by_genre.json', 'r', encoding='utf-8') as file:
        movies_json = json.load(file)

        return movies_json


def get_movie_by_cast(act_one, act_two):
    con = sqlite3.connect("netflix.db")  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"""
               SELECT *
               FROM netflix
               WHERE netflix.`cast` LIKE '%{act_one}%' AND netflix.`cast` LIKE %{act_two}%'
               
    """

    data = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД

    cast = []
    final_cast = set()

    for item in data:
        for actor in item[0]:
            cast.append(actor)

    for actor in cast:
        if cast.count(actor) > 2:
            final_cast.add(actor)

    with open('movie_by_cast.json', 'w') as outfile:
        json.dump(final_cast, outfile)

    with open('movie_by_cast.json', 'r', encoding='utf-8') as file:
        cast_json = json.load(file)

        return cast_json


def get_movie_by_genre_type_release_year(type_movie, release_year, listed_in):
    con = sqlite3.connect("netflix.db")  # Подключаемся к БД
    cur = con.cursor()  # Запускаем курсор, с помощью которого мы будем получать данные из БД
    sqlite_query = f"""
               SELECT title, description
               FROM netflix
               WHERE "type" = '{type_movie}'
               AND release_year = {release_year}
               AND listed_in LIKE '%{listed_in}%'
 
    """

    data = cur.execute(sqlite_query)  # Выполняем запрос с помощью курсора
    data = cur.fetchall()  # С помощью этой функции получаем результат запроса в виде списка кортежей
    con.close()  # После выполнения запросов обязательно закрываем соединение с БД

    result = []

    for item in data:
        result.append(
            {
                'title': item[0],
                'description': item[1],
            }
        )

    with open('movie_by_type_release_year.json', 'w') as outfile:
        json.dump(result, outfile)

    with open('movie_by_type_release_year.json', 'r', encoding='utf-8') as file:
        movies_json = json.load(file)

        return movies_json


# print(get_movie_by_cast('Jack Black', 'Dustin Hoffman'))
