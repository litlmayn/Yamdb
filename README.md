### Проект Yamdb - это проект, направленный на оценку любых произведений!

```
С помощью данной плотформы люди могут обмениваться отзывами о произведениях, комментировать отзывы других участников.
```

### Мы использовали данный стек технологий для проектирования проекта:
```
Django
DRF
Pethon
```
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:litlmayn/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
