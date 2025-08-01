FROM python:3.10.4-slim-bullseye

RUN apt update && apt upgrade -y && \
    apt install -y git curl python3-pip ffmpeg wget bash neofetch software-properties-common && \
    python3 -m pip install --upgrade pip

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt

# 👇 Add this line
RUN mkdir -p /app/sessions

WORKDIR /app
COPY . .

EXPOSE 5000

CMD ["bash", "-c", "flask run -h 0.0.0.0 -p 5000 & python3 -m devgagan"]
