from flask import Flask, render_template, request, session
from dbAccess import DB_Access


db_file_location = "app_db.db"

Medical_app = Flask(__name__ )
Medical_app.secret_key = 'super secret key'



db = DB_Access(db_file_location="app_db.db")

@Medical_app.route('/')
def index():
    return render_template('index.html')


@Medical_app.route('/register') 
def register():
    return render_template('register.html')

@Medical_app.route('/registerchk', methods=["POST"])
def registerchk():
    if request.method == "POST":

        name = request.form.get("name")
        password = request.form.get("pwd")
        address = request.form.get("addrs")
        phone = request.form.get("phone")
        email = request.form.get("email")

        result = db.insert_new_registration_data(
            names=name, passwords=password, phones=phone, emails=email, addresss=address
        )

        if result:
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

        result = db.check_login_data(emails=username, passwords=password)

        session['user_mail'] = username

        if result:
            return render_template('home.html')
        else:
            return render_template('error.html')


@Medical_app.route('/appointment')
def appointment():
    return render_template('appointment.html')



@Medical_app.route('/chatbox')
def chatbox():
    ls = db.get_all_user_email()
    ls = [x[0] for x in ls]
    ls.remove(session['user_mail'])
    session['all_mails'] = ls
    temp = db.get_all_message(receiver=session['user_mail'])
    temp = [
        f" Sender:{x[0]} Time:{x[3]} Message:{x[2]}" for x in temp
    ]
    session['all_msg'] = temp

    return render_template('chatbox.html', data={"all_mails":  session['all_mails'], "all_msg": session['all_msg']})


@Medical_app.route('/msgsend', methods=["POST"])
def msgsend():
    if request.method == "POST":

        sender = session['user_mail']
        receiver = request.form.get("recipient")
        message= request.form.get("msg")

        result = db.insert_new_message_data(
            senders=sender, receivers=receiver, messages=message,
        )
        if result:
            return render_template('chatbox.html', data={"all_mails":  session['all_mails'], "all_msg": session['all_msg']})
        else:
            return render_template('error.html')
@Medical_app.route('/logout', methods=["POST", "GET"])
def logout():
    session['all_mails'] = []
    session['user_mail'] = []
    session['all_msg'] = []
    return render_template('index.html')


if __name__ == '__main__':

    Medical_app.run()
