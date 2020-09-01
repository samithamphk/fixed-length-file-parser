FROM python:3

WORKDIR ./home/wd

ADD lati-data-sam.tar.gz ./home/wd/

WORKDIR ./home/wd/lati-data-sam/app/

#RUN python -m lati-sam-app.py