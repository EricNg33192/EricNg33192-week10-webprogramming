from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

def log_visitor():
    current_time = datetime.now().strftime("%a %b %d %Y %H:%M")
    with open("access_log.txt", "a") as log_file:
        log_file.write(f"{current_time}\n")

def read_access_log():
    try:
        with open("access_log.txt", "r") as log_file:
            access_times = log_file.readlines()
        return access_times
    except FileNotFoundError:
        return []

@app.route('/')
def index():
    log_visitor()
    access_times = read_access_log()
    return render_template('index.html', access_times=access_times)

if __name__ == '__main__':
    app.run(debug=True)
