import os
from datetime import date
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')

import django

django.setup()

from librarySite.models import Book, Author, Genre

book_data = [("Властелин колец: Братство кольца", 576, 8000, "11111", "1954-07-29", "Джон Р.Р. Толкин", "images/default_image.png", ["Фэнтези", "Эпическая фантастика", "Приключения"]),
             ("1984", 336, 9000, "22222", "1949-06-08", "Джордж Оруэлл", "images/default_image.png", ["Антиутопия", "Дистопия", "Политическая фантастика"]),
             ("Маленький принц", 96, 15000, "33333", "1943-04-06", "Антуан де Сент-Экзюпери", "images/default_image.png", ["Детская литература", "Философская проза", "Поэзия"]),
             ("Три товарища", 448, 5000, "44444", "1936-09-22", "Эрих Мария Ремарк", "images/default_image.png", ["Исторический роман", "Драма", "Романтика"]),
             ("Мастер Замок", 256, 4000, "66666", "1922-01-01", "Франц Кафка", "images/default_image.png", ["Сюрреализм", "Метафизика", "Психология"]),
             ("Война миров", 256, 3500, "77777", "1898-01-01", "Герберт Уэллс", "images/default_image.png", ["Научная фантастика", "Постапокалипсис", "Приключения"]),
             ("Ромео и Джульетта", 416, 12000, "99999", "1597-01-01", "Уильям Шекспир", "images/default_image.png", ["Трагедия", "Романтика", "Лирика"]),
             ("Автостопом по галактике", 224, 5500, "223344", "1979-10-12", "Дуглас Адамс", "images/default_image.png", ["Научная фантастика", "Юмор", "Фантастический роман"]),
             ("Убить пересмешника", 416, 9000, "334455", "1960-07-11", "Харпер Ли", "images/default_image.png", ["Роман-антиутопия", "Социальный роман", "Юмор"]),
             ("Тёмные начала", 512, 6000, "445566", "1995-07-17", "Филипп Пулман", "images/default_image.png", ["Фэнтези", "Детская литература", "Научная фантастика"]),
             ("Игра Эндера", 352, 7500, "667788", "1985-01-15", "Орсон Скотт Кард", "images/default_image.png", ["Научная фантастика", "Эпическая фантастика", "Антиутопия"]),
             ("Американский психопат", 400, 3500, "778899", "1991-03-01", "Брет Истон Эллис", "images/default_image.png", ["Сатира", "Ужасы", "Драма"]),
             ("Королевская игра", 384, 4000, "889900", "1982-04-12", "Стэффорд Холмс", "images/default_image.png", ["Фантастический роман", "Триллер", "Научная фантастика"]),
             ("Лолита", 336, 12000, "445566", "1955-09-15", "Владимир Набоков", "images/default_image.png", ["Роман", "Психологический роман", "Сатира"]),
             ("451 градус по Фаренгейту", 208, 6500, "556677", "1953-10-19", "Рэй Брэдбери", "images/default_image.png", ["Научная фантастика", "Фантастический роман", "Драма"]),
             ("Тень горы", 224, 5500, "889900", "1955-09-01", "Грегори Дэвид Робертс", "images/default_image.png", ["Детектив", "Приключения", "Триллер"]),
             ("За богословской оградой", 608, 2500, "001122", "1996-01-01", "Дональд Картмилл", "images/default_image.png", ["Детектив", "Религиозная литература", "Триллер"]),
             ("Идиот", 704, 6000, "112233", "1869-01-01", "Федор Достоевский", "images/default_image.png", ["Роман", "Философский роман", "Драма"]),
             ("Пикник на обочине", 160, 5000, "334455", "1972-01-01", "Аркадий и Борис Стругацкие", "images/default_image.png", ["Научная фантастика", "Фантастический роман", "Приключения"]),
             ("Дракула", 416, 8000, "445566", "1897-05-18", "Брэм Стокер", "images/default_image.png", ["Ужасы", "Готический роман", "Фэнтези"]),
             ("Собачье сердце", 144, 9000, "556677", "1925-04-12", "Михаил Булгаков", "images/default_image.png", ["Аллегория", "Фантастический роман", "Сатира"]),
             ("Колыбельная для взрослых", 128, 2000, "667788", "1966-01-01", "Джонас Йонассон", "images/default_image.png", ["Юмористическая литература", "Детектив", "Комедия"]),
             ("Мартин Иден", 616, 3000, "778899", "1909-09-08", "Джек Лондон", "images/default_image.png", ["Роман", "Социальный роман", "Драма"]),
             ("Кувшин с чайной пылью", 320, 4000, "889900", "1905-01-01", "Маргарет Олдершоу", "images/default_image.png", ["Роман", "Социальный роман", "Психологический роман"]),
             ("Марсианин", 384, 7000, "990011", "2011-03-22", "Энди Вейр", "images/default_image.png", ["Научная фантастика", "Фантастический роман", "Приключения"]),
             ("Война и мир", 1216, 8000, "001122", "1869-01-01", "Лев Толстой", "images/default_image.png", ["Исторический роман", "Роман", "Драма"]),
             ("Повелитель мух", 224, 7000, "112233", "1954-09-17", "Уильям Голдинг", "images/default_image.png", ["Роман", "Психологический роман", "Аллегория"]),
             ("Шантарам", 864, 9000, "223344", "2003-01-01", "Грегори Дэвид Робертс", "images/default_image.png", ["Роман", "Приключения", "Драма"]),
             ("Гарри Поттер и Философский камень", 256, 12000, "445566", "1997-06-26", "Джоан Роулинг", "images/default_image.png", ["Фэнтези", "Детская литература", "Приключения"]),
             ("Час быка", 288, 6000, "556677", "1956-01-01", "Джеймс Болдуин", "images/default_image.png", ["Роман", "Социальный роман", "Антиутопия"]),
             ("Таинственный остров", 768, 4000, "667788", "1874-01-01", "Жюль Верн", "images/default_image.png", ["Научная фантастика", "Приключения", "Роман-приключение"]),
             ("Код да Винчи", 576, 15000, "778899", "2003-03-18", "Дэн Браун", "images/default_image.png", ["Триллер", "Детектив", "Мистика"]),
             ("Сага о ведьмаке", 1024, 10000, "889900", "1993-11-02", "Анджей Сапковский", "images/default_image.png", ["Фэнтези", "Приключения", "Эпическая фантастика"]),
             ("О дивный новый мир", 288, 8000, "990011", "1932-01-01", "Олдос Хаксли", "images/default_image.png", ["Научная фантастика", "Роман-антиутопия", "Социальный роман"]),
             ("Унесённые ветром", 1438, 4000, "001122", "1936-06-10", "Маргарет Митчелл", "images/default_image.png", ["Исторический роман", "Роман", "Драма"]),
             ("Атлант расправил плечи", 1168, 8000, "223344", "1957-10-10", "Айн Рэнд", "images/default_image.png", ["Философский роман", "Научная фантастика", "Политический роман"]),
             ("1984", 320, 9000, "334455", "1949-06-08", "Джордж Оруэлл", "images/default_image.png", ["Роман-антиутопия", "Философский роман", "Социальный роман"]),
             ("Лев, колдунья и платяной шкаф", 224, 6000, "445566", "1950-10-16", "Клайв Стейплз Льюис", "images/default_image.png", ["Фэнтези", "Детская литература", "Христианская литература"]),
             ("Джейн Эйр", 624, 5000, "556677", "1847-10-16", "Шарлотта Бронте", "images/default_image.png", ["Роман", "Женский роман", "Драма"]),
             ("Преступление и наказание", 544, 7000, "667788", "1866-01-01", "Федор Достоевский", "images/default_image.png", ["Роман", "Психологический роман", "Социальный роман"]),
             ("Анна Каренина", 864, 4000, "778899", "1878-01-01", "Лев Толстой", "images/default_image.png", ["Роман", "Литература Реализма", "Женский роман"]),
             ("Десять негритят", 256, 12000, "990011", "1939-03-06", "Агата Кристи", "images/default_image.png", ["Детектив", "Триллер", "Мистика"]),
             ("Изучаем Python", 300, 5421, "PY5421", "2022-01-15", "Марк Лутц", "images/default_image.png", ["Программирование", "Python", "Компьютеры"]),
             ("Основы электроники", 432, 1987, "EL1987", "2005-06-30", "Владимир Шумейко", "images/default_image.png", ["Электроника", "Техническая литература", "Учебник"]),
             ("Сто лет одиночества", 432, 8765, "SO8765", "1967-05-30", "Габриэль Гарсия Маркес", "images/default_image.png", ["Магический реализм", "Южноамериканская литература", "Роман"]),
             ("Улисс", 768, 5678, "UL5678", "1922-02-02", "Джеймс Джойс", "images/default_image.png", ["Современная классика", "Экспериментальная проза", "Роман"]),
             ("Мастер и Маргарита", 448, 4321, "MM4321", "1967-11-13", "Михаил Булгаков", "images/default_image.png", ["Фантастика", "Сатира", "Роман"]),
             ("Герой нашего времени", 224, 8765, "GH8765", "1839-03-06", "Михаил Лермонтов", "images/default_image.png", ["Русская классика", "Роман-экзистенциализм", "Поэма"]),
             ("Цветы для Элджернона", 320, 2345, "CE2345", "1966-04-28", "Дэниел Киз", "images/default_image.png", ["Научная фантастика", "Фантастический роман", "Психологический роман"]),
             ("Над пропастью во ржи", 320, 4567, "NP4567", "1951-07-16", "Джером Д. Сэлинджер", "images/default_image.png", ["Современная классика", "Постмодернизм", "Роман"]),
             ("Заводной апельсин", 192, 8901, "ZA8901", "1962-06-01", "Энтони Бёрджесс", "images/default_image.png", ["Научная фантастика", "Ужасы", "Роман"]),
             ("Мобильник", 384, 120000, "ISBN978-5-699-27059-7", "2006-01-01", "Стивен Кинг", "images/default_image.png", ["Ужасы", "Фантастика"]),
             ("Хроники Нарнии: Лев, Колдунья и платяной шкаф", 192, 87000, "ISBN978-5-699-12368-7", "1950-10-16", "Клайв Льюис", "images/default_image.png", ["Фэнтези"]),
             ("Зеленая миля", 400, 80000, "ISBN978-5-699-26802-0", "1996-04-01", "Стивен Кинг", "images/default_image.png", ["Ужасы", "Драма"]),
             ("Гарри Поттер и философский камень", 256, 150000, "ISBN978-5-389-01646-2", "1997-06-26", "Дж. К. Роулинг", "images/default_image.png", ["Фэнтези", "Магический реализм"]),
             ("Доктор Сон", 656, 95000, "ISBN978-5-699-95861-2", "2013-09-24", "Стивен Кинг", "images/default_image.png", ["Ужасы", "Фантастика"]),
             ("Гарри Поттер и тайная комната", 288, 120000, "ISBN978-5-17-025800-7", "1998-07-02", "Дж. К. Роулинг", "images/default_image.png", ["Фэнтези", "Магический реализм"]),
             ("Оно", 1376, 70000, "ISBN978-5-17-103523-7", "1986-09-15", "Стивен Кинг", "images/default_image.png", ["Ужасы"]),
             ("Гарри Поттер и узник Азкабана", 416, 100000, "ISBN978-5-17-021873-5", "1999-07-08", "Дж. К. Роулинг", "images/default_image.png", ["Фэнтези", "Магический реализм"]),
             ("Кэрри", 288, 60000, "ISBN978-5-17-077742-3", "1974-04-05", "Стивен Кинг", "images/default_image.png", ["Ужасы"]),
             ("Гарри Поттер и орден Феникса", 768, 90000, "ISBN978-5-17-049064-9", "2003-06-21", "Дж. К. Роулинг", "images/default_image.png", ["Фэнтези", "Магический реализм"]),
]



for book in book_data:
    title, pages_count, downloads_count, description, created_at, author_name, image_path, genre_names = book

    # create or get the author
    author, created = Author.objects.get_or_create(name=author_name)
    book = Book.objects.create(title=title, pages_count=pages_count, downloads_count=downloads_count,
                               description=description, created_at=date.fromisoformat(created_at), author=author,
                               image=image_path)

    # add genres to the book
    for genre_name in genre_names:
        genre, created = Genre.objects.get_or_create(name=genre_name.capitalize())
        book.genre.add(genre)

print('Finished populating the database with book data.')