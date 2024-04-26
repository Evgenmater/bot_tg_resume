### Телеграм Бот для составления резюме
Бот предназначен для составления резюме, чем точнее и яснее будешь давать информацию о резюме, тем более точней он его составляет. Бот принимает голосовые и текстовые сообщения! Если не нравится резюме, то есть возможность составить его заново.

### Как запустить проект:

* Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Evgenmater/bot_tg_resume.git
```

```
cd bot_tg_resume
```

* Cоздать и активировать виртуальное окружение:

* Если у вас Linux/macOS
    ```
    python3 -m venv venv
    ```

    ```
    source venv/bin/activate
    ```

* Если у вас windows
    ```
    python -m venv venv
    ```

    ```
    source venv/scripts/activate
    ```

* Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

* Перед запуском бота надо создать файл .env и внести данные:

```
TELEGRAM_TOKEN = Телеграм токен
KEY_ID = KeyId для speechflow
KEY_SECRET = KeySecret для speechflow
AUTHORIZATION = authorization_data для Gigachata

```

* Запустить бота:

```
python main.py
```


### Автор:  
Хлебнев Евгений Юрьевич<br>
**email**: hlebnev@yandex.ru<br>
**telegram** @Evgen0991