# Инструкция по запуску
1. Создать docker контейнер командой
```shell
docker run -p 6379:6379 -d redis:5
```
2. Скачать все зависимости в виртуальное окружение

```shell
pip install -r requirements.txt
```

3. Запустить проект командой

```shell
python3 manage.py runserver
```
