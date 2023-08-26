FROM python:3.11.4

WORKDIR /RapidFort

COPY . /RapidFort

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "fileupload.py"]