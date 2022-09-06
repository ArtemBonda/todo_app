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

python -m venv C:\path_to_project\name_venv
```
     - `-m` указание Python запускать *venv* как исполняемый модуль
- Активация
- 
      *  для Windows
```commandline
venv\Scripts\activate.bat 

# or in PowerShell
C:\path_to_project\name_venv\Scripts\Activate.ps1
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

### Памятка
___
*Модульные* тесты проверяют приложение изнутри – с точки зрения программиста.
*Функциональные* тесты проверяют приложение с внешней стороны – с точки зрения пользователя.

_Подход TDD, которому следуют, хочет, чтобы приложение было охвачено обоими типами тестов. Поток операций будет примерно таким:_
1. Мы начинаем с написания функционального теста, описывающего новую функциональность с точки зрения пользователя.
2. Когда у нас есть функциональный тест, который не срабатывает, мы начинаем думать о том, как написать код, который может заставить 
его пройти успешно (или по крайней мере заставить перешагнуть через текущую неполадку). Мы теперь используем один или несколько 
модульных тестов, чтобы выработать поведение кода, которого мы хотим добиться. Смысл в том, что каждая строка производственного 
программного кода, которую мы пишем, должна быть протестирована по крайней мере одним из наших модульных тестов.
3. Когда у нас есть неработающий модульный тест, мы пишем минимально возможный объем прикладного кода – ровно столько, чтобы 
модульный тест прошел успешно. Мы можем несколько раз итеративно переключаться между шагами 2 и 3, пока не убедимся, что 
функциональный тест продвинулся чуть дальше.
4. Теперь мы можем выполнить функциональные тесты повторно и убедиться, что они проходят или продвинулись немного дальше. 
Этот этап может нас побудить написать немного новых модульных тестов и нового исходного кода и т. д