FROM python:3.8.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_VERSION=1.1.13

RUN pip install --upgrade pip
RUN pip install "poetry==$POETRY_VERSION"
# RUN apk --update add
# RUN apk add gcc libc-dev 
# RUN apk add postgresql-dev

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry install

# RUN pip install --upgrade pip
# RUN poetry export --dev --without-hashes --no-interaction --no-ansi -f requirements.txt -o requirements.txt
# RUN pip install --prefix=/runtime --force-reinstall -r requirements.txt


COPY . .

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
