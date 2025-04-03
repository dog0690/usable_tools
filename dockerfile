FROM python:slim
ADD main.py .
CMD ["python", "./main.py"]