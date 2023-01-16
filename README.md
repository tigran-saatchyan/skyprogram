# Курсовая работа 3
![alt text](https://img.shields.io/badge/Python-v3.10.6-blue?style=for-the-badge&logo=appveyor "Python")
![alt text](https://img.shields.io/badge/Flask-v2.2.2-green?style=for-the-badge&logo=appveyor "Flask")
![alt text](https://img.shields.io/badge/Jinja2-v3.1.2-yellow?style=for-the-badge&logo=appveyor "Jinja2")
<hr>


## Критерии выполнения  задания:

- [x]  Обработка данных их формы выполняется корректно
- [x]  Вывод нефильтрованного списка выполняется корректно
- [x]  Вывод фильтрованного списка выполняется корректно
- [x]  Работа с данными вынесена в функции или отдельный класс
- [x]  Данные фильтруются до передачи в шаблон, лишние данные в шаблон не передаются


### Структура проекта:

```
.
├── api
│   ├── api.py
│   └── __init__.py
├── app.py
├── config.py
├── data
│   ├── bookmarks.json
│   ├── comments.json
│   └── posts.json
├── logs
│   ├── api.log
│   └── main.log
├── main
│   ├── __init__.py
│   ├── main.py
│   ├── post_handler.py
│   ├── static
│   │   ├── css
│   │   │   ├── sky.css
│   │   │   ├── styles.min.css
│   │   │   └── styles.min.css.map
│   │   └── img
│   │       ├── 404.jpg
│   │       ├── 500.gif
│   │       ├── ava1.png
│   │       ├── ava2.png
│   │       ├── bookmark.png
│   │       ├── eye.png
│   │       ├── heart.png
│   │       ├── no_ava.png
│   │       ├── no_pic.webp
│   │       ├── post10.jpg
│   │       ├── post1.jpg
│   │       ├── post2.jpg
│   │       ├── post3.jpg
│   │       ├── post4.jpg
│   │       ├── post5.jpg
│   │       ├── post6.jpg
│   │       ├── post7.jpg
│   │       ├── post8.jpg
│   │       └── post9.jpg
│   ├── templates
│   │   ├── 404.html
│   │   ├── 500.html
│   │   ├── bookmarks.html
│   │   ├── index.html
│   │   ├── post.html
│   │   ├── search.html
│   │   ├── tag.html
│   │   └── user-feed.html
│   └── utils.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── test_api.py
    └── test_post_handler.py

9 directories, 48 files
```
