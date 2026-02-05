FROM python:3.13-alpine3.22  

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
RUN pip install --upgrade pip 
 
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . /app/
 
EXPOSE 8002
 
# Run as root (simpler for development)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]