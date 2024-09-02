# Используем базовый образ с Python
FROM python:3.12

# Устанавливаем Poetry
ENV POETRY_VERSION=1.4.2
RUN pip install "poetry==$POETRY_VERSION"

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Копируем все файлы проекта в контейнер
COPY . .

# Устанавливаем Nginx и Supervisord
RUN apt-get update && apt-get install -y nginx supervisor


# Копируем конфигурацию Supervisord
COPY supervisord.ini /etc/supervisor/conf.d/supervisord.ini

# Запуск Supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.ini"]
