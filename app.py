from flask import Flask , jsonify,request,json
import jwt
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///pro.db'
app.config['SECRET_KEY']="this_is_key"

db = SQLAlchemy(app)

# schema defination
class users(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100),nullable=False,unique=True)
    password = db.Column(db.String(100),nullable=False)



@app.route('/')
def f():
    return " hiii"


# register user
@app.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    username=data['username']
    password=data['password']

    if not username  or not password :
        return jsonify({"message":"username ans password are required"})
    dbuser = users.query.filter_by(username=username).first()

    if dbuser :
        return jsonify({"message":"username allready exist try another"})
    new_user=users(username=username,password=password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"massage":"user registered successfully"})


# login user
@app.route('/login',methods=['POST'])
def login():
    data = request.get_json()

    username = data['username']
    password = data['password']

    if not username or not password:
        return jsonify({"message":"username and password are required"})
    
    db_data=users.query.filter_by(username=username).first()

    if not db_data:
        return jsonify({"message":"user not found"})
    
    if password != db_data.password:
        return jsonify({"message":"invalid password"})
    
    expiration = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
    
    #token creation 
    token = jwt.encode({'username':username,'exp':expiration},app.config['SECRET_KEY'],algorithm='HS256')
    
    return jsonify({'token':token})

@app.route('/verify',methods=['POST'])
def verify():
    data = request.get_json()
    token = data['token']
    
    if not token:
        return jsonify({"message":"token is missing"}),404
    
    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        
    except Exception :
        return jsonify({"message":"somethoing went wrong"})
    return jsonify({'username':decoded['username'],"message":"token is valid","status":"user login successfully"})


if __name__ == "__main__":

    with app.app_context():
        db.create_all()
    app.run(debug=True)
