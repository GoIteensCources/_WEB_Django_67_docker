
# Deploy project in docker container

## install dependencies
`pip install gunicorn whitenoise`


## run server
`gunicorn dev_portfolio.wsgi:application --bind 0.0.0.0:8000 --workers 3 --log-level=debug`


# dockerfile
```
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
ENV DJANGO_SETTINGS_MODULE=dev_portfolio.settings
ENV SECRET_KEY="@(2elv+fb!dki3-x5tc76l!ezu-3ll+o+cr6eo%16pqyb-^uir"
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```