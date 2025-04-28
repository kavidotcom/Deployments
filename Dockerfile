FROM python:3.13.3-bookworm

WORKDIR /practice

COPY artefacts/requirements.txt .

RUN pip install -r requirements.txt

COPY . /practice/

CMD ["python", "-m", "flask", "--app", "hello.py", "run", "--host=0.0.0.0", "--port=8000"]