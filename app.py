from flask import Flask, render_template, request, session
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'    
with open('config.json', 'r') as c:
    params = json.load(c)["params"]


@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if "user" in session and session["user"] == params["user-name"]:
        return render_template("main.html")
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == params["user-name"] and password == params["user-pass"]:
            session["user"] = username
            return render_template("main.html")
    return render_template("index.html")


@app.route('/main')
def main():
    return render_template("main.html")


app.run(debug=True)
