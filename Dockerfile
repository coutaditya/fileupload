FROM python:3.11.4

WORKDIR /RapidFort

COPY . /RapidFort

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "fileupload.py"]