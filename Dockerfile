FROM python:3.12.1 as build

WORKDIR /opt/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


FROM python:3.12.1

COPY --from=build . .