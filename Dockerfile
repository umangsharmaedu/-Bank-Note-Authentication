FROM python:3.7-slim
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirement.txt
CMD python flasgger_ui.py
