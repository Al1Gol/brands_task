FROM python:3.11.3
RUN pip install --upgrade pip

# Установка переменного окружения
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYCODE 1

#Установка рабочей директории
WORKDIR /app/backend

# Корпирование проекта
COPY ./ /app/backend/

# Установка пакетов
RUN pip install uv
RUN uv sync

WORKDIR /app/backend/brand_project/