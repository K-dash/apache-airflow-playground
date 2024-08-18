FROM apache/airflow:2.10.0

USER root

RUN apt-get update && apt-get install -y \
    git \
    vim \
    make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /opt/airflow

USER airflow

RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN cd /opt/airflow && poetry install --no-interaction --no-ansi
