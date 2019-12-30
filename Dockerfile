FROM python:3.8
MAINTAINER Max Aleynikov <max.aleyinikov@gmail.com>

WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install -y ruby
RUN gem install foreman

COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
CMD ["foreman", "start"]
