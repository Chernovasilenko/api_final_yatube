# api_final

### Описание проекта:
Yatube — это платформа для блогов. В данном проекте реализовано API для этой платформы.

С помощью API можно запрашивать данные о постах, сообществах, подписках и комментариях в Yatube. 

### Установка проекта:

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:Chernovasilenko/api_final_yatube.
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```
Выполнить миграции:

```bash
python3 manage.py migrate
```

Запустить проект:

```bash
python3 manage.py runserver
```

### Примеры запросов:

Получить список всех постов (GET):

```
http://127.0.0.1:8000/api/v1/posts/
```

Получить определённый пост (GET):

```
http://127.0.0.1:8000/api/v1/posts/1/
```

Получить коментарии определённого поста (GET):

```
http://127.0.0.1:8000/api/v1/posts/1/comments/
```

Получить список всех групп (GET):

```
http://127.0.0.1:8000/api/v1/groups/
```

Подробная документация со всеми примерами запросов будет доступна после запуска проекта по адресу:

```
http://127.0.0.1:8000/redoc/
```