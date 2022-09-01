# Приложение To-Do List #

## Необходимый софт

1. Firefox - веб браузер
1. Git - система управлениями версиями 
1. `virtualenv` - инструмент среда окружения Python
    1. django
    1. selenium
1. <a href='https://github.com/mozilla/geckodriver/releases'>Geckodriver</a> - драйвер позволяющий удаленно управлять Firefox через Selenium. Скачать, распаковать, переместить (linux) в `~/.local/bin`; (Win) в папку Python `'Scripts'`
проверить 
```
geckodriver --version
```

## Настройка виртуальной среды virualenv

virualenv - это то как настраивается програмная среда для различных проектов Python.
- Windows
```
pip install virtualenvwrapper
```
- Linux
```
pip install --user virtualenvwrapper
# далее дать Bash загружать автоматически virtualenvwrapper
echo "source virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
```

Все виртуальные среды будут храниться в одном месте, что обеспечивает активацию и деаетивацию нужных инструментов.
- Linux
```
# создать виртуальную среду superlist
mkvirtualenv --python=python3.8 superlists

superlists
```

- Widows 
```
# создать виртуальную среду superlist
mkvirtualenv --python=python3.8 superlists
mkvirtualenv --python=`py -3.8 -c"import sys; print(sys.executable)"`

superlists
```

- Проверка запуска какая запущена виртуальная среда
```
which python3
```

- деактивация виртуальной среды
```
deactive
```

- Активация виртуальной среды 
```
workon superlists
```

## Настройка виртуальной среды venv
- Создание
```commandline
python3 -m venv venv
```
     - `-m` указание Python запускать *venv* как исполняемый модуль
- Активация
- 
      *  для Windows
```commandline
venv\Scripts\activate.bat 
```
      - для Linux
```commandline
source venv/bin/activate
```
- Также новый путь до библиотек можно увидеть выполнив команду:
```commandline
python3 -c "import site; print(site.getsitepackages())"
```


### Установка Django and Selenium
```
pip install "django=1.12" "selenium<4"
````
- просмотр установленных инструментов

```
pip list
```

## Создание приложения ToDoList
* Создать директорию приложения с конфигурационными файлами 
```commandline
python-admin startproject todo_list
```
# Просмотреть дерево проекта
```commandline
tree todo_app
```
**`manage.py`** - швейцарский нож, часть из его функций заключается в выполнении сервера разработки

```commandline
python3 manage.py runserver
```
or
```commandline
python3 manage.py runserver 9000 # запуск на localhost:9000
```

```commandline
python3 functional_tests.py # 
```

**`db.sqlite3`** - файл базы данных.Его не надо отслеживать в vcs
**`geckodriver.log`** - журнал сообщений от Selenium
- добавление файлов в список игнорированных файлов
```commandline
echo "db.sqlite3" >> .gitignore
echo "geckodriver.log" >> .gitignore
```
- удаление файлов из отслеживаемых
```git
git rm -r --cashed todo_app/__pycache__
```
and add in the .gitignore file

```commandline
echo "__pycache __"  >> .gitignore
echo "*.pyc" >> .gitignore
```
___

- Подготовка зависимостей
1. Активировать виртуальное окружение
2. Записать используемые библиотеки в файл
```commandline
pip freeze > requirements.txt
```
3. Добавить `requirements.txt` в отслеживаемые

   *  Развертывание необходимых библиотек для работы с приложением
```commandline
pip install -r requirements.txt
```
   * Просмотр установленных библиотек 

```commandline
pip list
```