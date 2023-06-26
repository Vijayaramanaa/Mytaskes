from python:3.10
workdir /app
add ./app
copy requirements.txt/app
run python3-m pip install -r requirements.txt
expose 5000
cmd["python","app.py"]