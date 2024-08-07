<h3 align="center">Проект DRF</h3>

<details>
  <summary>Оглавление</summary>
  <ol>
    <li>О проекте</li>
    <li>Технологии</li>
    <li>Настройка проекта</li>
    <li>Использование</li>
    <li>Контакты</li>
  </ol>
</details>



## О проекте


## Технологии
- Django
- PostgreSQL
- DRF
- Celery
- Redis
- Docker


## Настройка проекта

Для работы с проектом произведите базовые настройки.

### 1. Клонирование проекта

Клонируйте репозиторий используя следующую команду.
  ```sh
  git clone https://github.com/UserSemDev/Django_DRF.git
  ```


### 2. Настройка виртуального окружения и установка зависимостей

- Инструкция для работы через виртуальное окружение - poetry: 
```text
poetry init - Создает виртуальное окружение
poetry shell - Активирует виртуальное окружение
poetry install - Устанавливает зависимости
```

- Инструкция для работы через виртуальное окружение - pip:

Создает виртуальное окружение:
```text
python3 -m venv venv
```

Активирует виртуальное окружение:
```text
source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate.bat         # для Windows
```

Устанавливает зависимости:
```text
pip install -r requirements.txt
```

### 3. Редактирование .env.sample:

- В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:
    ```text
    # Postgresql
    POSTGRES_ENGINE="postgresql_psycopg2" - используем psycopg2
    POSTGRES_NAME="db_name" - название вашей БД
    POSTGRES_PGUSER="postgres" - имя пользователя БД
    POSTGRES_PASSWORD="secret" - пароль пользователя БД
    POSTGRES_HOST="host" - можно указать "localhost" или "127.0.0.1"
    POSTGRES_PORT=port - указываете порт для подключения по умолчанию 5432
    
    # Django
    SECRET_KEY=secret_key - секретный ключ django проекта
    DEBUG=True - режим DEBUG
  
    # API Stripe
    STRIPE_API_KEY=secret_key - секретный ключ от API stripe.com
  
    # Mailing
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=
    
    # Redis
    REDIS=
    ```

### 4. Настройка БД:

- Примените миграции:
  ```text
  python manage.py migrate
  ```

 
- Загрузка данных из фикстур:
  ```text
  python manage.py loaddata fixtures/*.json
  ```

## Использование

#### Для запуска локально проекта наберите в терминале команду:
  ```text
  python manage.py runserver
  ```
  перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)


#### Для запуска проекта через Docker:
- установите Docker себе в систему, перейдя по [ссылке](https://docs.docker.com/engine/install/)
- для сборки проекта и запуска введите команду:
  ```text
  docker-compose up -d --build
  ```
- перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Контакты

Ссылка на репозиторий: [https://github.com/UserSemDev](https://github.com/UserSemDev)