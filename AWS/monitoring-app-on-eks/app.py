import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_persent = psutil.cpu_percent(interval=1) 
    mem_persent = psutil.virtual_memory().percent
    Message = None
    if cpu_persent > 80 or mem_persent > 80:
        Message = "Attention!!! High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_metric=cpu_persent, mem_metric=mem_persent, message=Message)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')