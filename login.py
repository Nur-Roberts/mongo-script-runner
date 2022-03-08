from flask import Flask, request, render_template
from flask_login import LoginManager, login_fresh, 

# GLobals
app = Flask(__name__)
# Set Login Manager
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_manager = LoginManager()
login_manager.init_app(app)

class User:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template(
            "login.html"
        )
    elif request.method == "POST":
        user_name = request.form['username']
        password = request.form['password']
        print(
            user_name,
            password
        )
        return render_template(
            "login.html"
        )


if __name__ == "__main__":
    app.run(debug=True)