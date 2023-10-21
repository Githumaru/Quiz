# Используем образ Python в качестве базового образа
FROM python:3.8

# Создаем и переходим в директорию /code
WORKDIR /code

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Копируем все файлы проекта в текущую директорию /code
COPY . /code/
