from flask import render_template, abort
import requests
import json

def home_page_process():

    response = requests.get("http://127.0.0.1:5051/home")
    return_data = json.loads(response.content.decode("utf-8"))

    if return_data["result"]:
        data = return_data['data']
        return render_template("home.html", data=data)
    else:
        abort(400)

