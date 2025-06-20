FROM python:3.12.2
RUN pip install --upgrade pip

ENV DB_HOST='db'
ENV DB_PORT='5432'
ENV DB_NAME='branddb'
ENV DB_USER='postgres'
ENV DB_PASSWORD='123'

#Установка рабочей директории
WORKDIR /app/backend

# Корпирование проекта
COPY /. /app/backend/

# Установка пакетов
RUN pip install uv

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

RUN uv sync --no-dev

ENV PATH="/app/backend/.venv/bin:$PATH"

ENV PYTHONPATH=/app/backend/

ENTRYPOINT []

WORKDIR /app/backend/brand_project/
