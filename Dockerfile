FROM python:latest

ARG TOKEN
ENV TOKEN=$TOKEN

ADD sample_api.py .

ENTRYPOINT ["python3","sample_api.py"]