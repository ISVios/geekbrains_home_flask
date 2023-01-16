FROM python:3.10.8

WORKDIR /app

RUN pip3 install -U pip

# poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN ln -s /root/.local/bin/poetry /usr/bin/poetry

COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install --without=dev --no-root

# ~poetry

COPY wsgi.py wsgi.py

EXPOSE 5000

COPY docker/entrypoint.sh .

ENTRYPOINT [ "./entrypoint.sh" ]
