FROM python:3.9

ARG PORT
ENV PYTHONUNBUFFERED True


#---setup workspace---#
ADD / /app
WORKDIR /app

RUN apt-get update && apt-get install -y libmagickwand-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get -y install ghostscript && apt-get clean
RUN ghostscript --version
RUN apt-get -y install libzbar-dev
RUN apt-get -y install libjpeg-dev
RUN apt-get -y install build-essential libpoppler-cpp-dev pkg-config

RUN pip --no-cache-dir --trusted-host pypi.python.org install -r /app/requirements.txt

#---run all---#
#CMD ["uvicorn", "wsgi:app", "--host", "0.0.0.0", "--port", "80"]
CMD uvicorn wsgi:app --host "0.0.0.0" --port $PORT --workers 1 --reload --ws 'auto' --loop 'auto'

#CMD exec gunicorn --bind :80 --workers 1 wsgi:app --worker-class uvicorn.workers.UvicornH11Worker