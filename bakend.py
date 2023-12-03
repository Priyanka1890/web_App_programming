from flask import Flask, render_template, request
from dbAccess import DB_Access
from flask_socketio import SocketIO, emit

Medical_app = Flask(__name__ )
db = DB_Access(db_file_location="./app_db")
socketio = SocketIO(Medical_app, cors_allowed_origins="*")


@socketio.on('connect')
def handle_message(data):
    emit('message', {'username': 'Student', 'message': data['message']}, broadcast=True)


@socketio.on('disconnect')
def disconnect():
    print('Client disconnected')



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
        if result:
            return render_template('home.html')
        else:
            return render_template('error.html')


@Medical_app.route('/appointment')
def appointment():
    return render_template('appointment.html')



@Medical_app.route('/chatbox')
def chatbox():
    return render_template('chatbox.html')

if __name__ == '__main__':

    Medical_app.run()
    socketio.run(Medical_app, debug=True)