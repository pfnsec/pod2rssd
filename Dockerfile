FROM python:3.11-alpine as base

WORKDIR /app

# RUN apk add --no-cache postgresql-libs libpq postgresql-dev 
RUN apk add --no-cache build-base

COPY setup.py .

RUN python -m venv env/

RUN env/bin/python setup.py install
# RUN env/bin/python -m pip install importlib_metadata psycopg_binary

FROM python:3.11-alpine as runner

WORKDIR /app

# RUN apk add --no-cache postgresql-libs libpq

COPY --from=builder /app/env/ ./env
COPY . . 

# EXPOSE 8000

CMD "/bin/sh -c 'trap exit TERM; while :; do ./env/python scandir.py; sleep 10m & wait $${!}; done;'"
