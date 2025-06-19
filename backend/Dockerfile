FROM python:3.12.2
RUN pip install --upgrade pip

# Установка переменного окружения
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYCODE 1

#Установка рабочей директории
WORKDIR /app/backend

# Корпирование проекта
COPY /. /app/backend/

# Установка пакетов
RUN pip install uv
RUN uv sync --locked

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app/backend/brand_project/

RUN python -m alembic revision --autogenerate -m 'Init'
