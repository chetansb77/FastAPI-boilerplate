# Dockerfile

# pull the official docker image
FROM python:3.9

# set work directory
WORKDIR /code

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirement.txt /code/requirement.txt

# Prerequisuits for ODBC drivers for SQL server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
#Debian 11
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
# optional: for bcp and sqlcmd
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
# Required for installing pyodbc
RUN apt-get update
RUN apt-get --assume-yes install g++ unixodbc-dev

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirement.txt

# copy project
COPY . /code