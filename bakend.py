from flask import Flask, render_template, request
from dbAccess import insert_new_registration_data #check_login_data

Medical_app = Flask(__name__ )

@Medical_app.route('/')
def home():
    return 'Medical App'

@Medical_app.route('/register') 
def register():
    return render_template('register.html')


@Medical_app.route('/about')
def about():
    return render_template('about.html')






@Medical_app.route('/registerchk', methods=["POST"])
def registerchk():
    if request.method == "POST":

        name = request.form.get("name")
        password = request.form.get("pwd")
        address = request.form.get("addrs")
        phone = request.form.get("phone")
        email = request.form.get("email")

        result = insert_new_registration_data(table_name="userDetail.csv", names=name, passwords=password, phones=phone, emails=email, addresss=address)

        if result == 1:
            return render_template('login.html')
        else:
            return render_template('error.html')


@Medical_app.route('/login')
def login():
    return render_template('login.html')


@Medical_app.route('/loginchk', methods=["POST"])
def loginchk():
    if request.method == "POST":
        username = request.form.get("usr")
        password = request.form.get("pwd")

        result = check_login_data(table_name="userDetail.csv", emails=username, passwords=password)

        if result == 1:
            return render_template('home.html')
        else:
            return render_template('error.html')


if __name__ == '__main__':
    Medical_app.run()