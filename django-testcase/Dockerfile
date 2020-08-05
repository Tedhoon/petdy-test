FROM python:3.6

RUN apt-get update \ 
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

COPY . /app

WORKDIR /app/testbackend/
# 요놈은 CMD 관련이네!

RUN pip install -r /app/requirements.txt  

EXPOSE 80
EXPOSE 443  
EXPOSE 8000  

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
