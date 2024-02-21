#-------------------------------------------------------------------------------------------------------
#
# Author:      King David Consulting LLC
#
# Description: This is a Dockerfile for a Python application. It is a multi-stage build.
#
# docker run -e APP_SCRIPT=./new_script.py -e REQ_NAME=new_requirements.txt your_image_name
#-------------------------------------------------------------------------------------------------------

FROM python:3.11-slim-buster  

ENV APP_SCRIPT ./web.py
ENV REQ_NAME requirements.txt

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends  \
    apt-utils \
    unixodbc-dev \
    tk-dev \
    gnupg \
    curl \
    ca-certificates \
    libmagic-mgc \
    libmagic1 

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/* 
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql18

WORKDIR /usr/src/app

COPY ${REQ_NAME} .

RUN pip install --upgrade pip && pip install --no-cache-dir -r ${REQ_NAME}

COPY /src/ .

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the command to start the Streamlit server
ENTRYPOINT ["streamlit", "run", "${APP_SCRIPT}", "--server.port=8501", "--server.address=0.0.0.0"]
