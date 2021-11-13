from app import app
from flask import render_template
from flask import request

#user data
@app.route("/user")
def print_users():
    if "user" in request.cookies:
        print(request.cookies)
        return render_template("public/EstateAgency/agent-single.html",name=request.cookies['user'])
    else:
        print(request.cookies)
        return render_template("public/index.html",name='auth_token')

#display user data
@app.route("/user/<user_name>")
def print_user(user_name):
    if "user" in request.cookies:
        print(request.cookies)
        return render_template("public/EstateAgency/agent-single.html",name=request.cookies['user'])
    else:
        print(request.cookies)
        return render_template("public/index.html",name='auth_token')

