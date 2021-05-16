FROM python:3.9

ARG PORT
ENV PYTHONUNBUFFERED True


#---setup workspace---#
ADD / /app
WORKDIR /app

RUN pip --no-cache-dir --trusted-host pypi.python.org install -r /app/requirements.txt

CMD uvicorn wsgi:app --host "0.0.0.0" --port $PORT --workers 1 --reload --ws 'auto' --loop 'auto'