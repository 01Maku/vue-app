FROM python:3.9-slim
WORKDIR /app
RUN pip install pipenv
COPY ./backend/requirements.txt /app/
RUN apt-get update && apt-get install -y libpq-dev && apt-get clean
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY  ./backend /app/
ENV FLASK_APP=app
ENV FLASK_ENV=development
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]