from flask import render_template
import requests

def home_page_process():

    response = requests.get("http://127.0.0.1:5000/test")
    aaa = response.content.decode("utf-8")

    return render_template("home.html", tb_test=aaa)