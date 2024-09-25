import os
from flask import *
from auth_config import*
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from functools import wraps
from datetime import datetime
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY')
bcrypt = Bcrypt(app)

def _required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' in session:
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    if 'user' in session:
        return render_template('index.html',user=True)
    date = datetime.now().strftime('%d-%m-%Y')
    return render_template('index.html',user=False,date=date)

@app.route('/profile')
def profile():
    if 'user' in session:
        userdata=db.child("users").child(session["user"]).get().val()
        return render_template('profile.html',userdata=userdata,user=True)
    return redirect(url_for('index'))

@app.route('/login',methods=['GET', 'POST'])
@_required 
def login():
    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        try:
            user = Auth.sign_in_with_email_and_password(email, password)
            session['user'] = user['localId']
            return redirect(url_for('index'))
        except:
            return "there is error"
    return render_template('login.html')

@app.route('/register',methods=['GET', 'POST'])
@_required 
def regiser():
    if request.method=='POST':
        name=request.form['name']
        phone=request.form['phone']
        email = request.form['email']
        password = request.form['password']
        try:
            user = Auth.create_user_with_email_and_password(email, password)
            db.child("users").child(user['localId']).set({'name':name,'phone':phone,'email':email})
            session['user'] = user['localId']  
            return redirect(url_for('index'))
        except Exception as e:
            return str(e)
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.after_request
def add_no_cache(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 