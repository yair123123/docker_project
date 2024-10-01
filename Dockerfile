FROM python:3.12-slim
WORKDIR /app
COPY requieremnts.txt . 
RUN pip install --no-cache-dir -r requieremnts.txt
COPY . .
CMD [ "python","app.py" ]