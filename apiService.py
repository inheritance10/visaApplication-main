from flask import Flask, jsonify, request, g
import jwt
import os
import datetime
import mysql.connector
from dotenv import load_dotenv
import excel_reader as er
import bcrypt
from flask_cors import CORS
load_dotenv()

app = Flask(__name__)

# Database configuration
db_config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'raise_on_warnings': True
}



app = Flask(__name__)
cors = CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Access-Control-Allow-Headers", "Authorization", "X-Requested-With"]
    }
})

def create_app(smsCode,data):
    print("start api")

    def token_required(f):
        def decorated(*args, **kwargs):
            token = None

            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']

            if not token:
                return jsonify({'message': 'Token is missing!'}), 401

            try:
                data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
                conn = mysql.connector.connect(**db_config)
                cursor = conn.cursor(dictionary=True)
                cursor.execute('SELECT * FROM company WHERE id = %s', (data['user_id'],))
                current_user = cursor.fetchone()
                cursor.close()
                conn.close()
            except Exception as e:
                return jsonify({'message': 'Token is invalid!'}), 401

            g.current_user = current_user
            return f(*args, **kwargs)

        decorated.__name__ = f.__name__
        return decorated

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        username = data.get('username')
        company_name = data.get('company_name')
        password = data.get('password')
        email = data.get('email')
        name = data.get('name')
        surname = data.get('surname')
        phone = data.get('phone')

        if not username or not password or not email:
            return jsonify({'error': 'Missing fields'}), 400

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        try:
            cursor.execute(
                'INSERT INTO company (username,company_name,password,email,name,surname,phone) VALUES (%s, %s, %s,%s, %s, %s, %s)',
                (username, company_name, hashed_password, email, name, surname, phone))
            conn.commit()
        except mysql.connector.IntegrityError:
            return jsonify({'error': 'User already exists'}), 400
        finally:
            cursor.close()
            conn.close()

        return jsonify({'message': 'User registered successfully'}), 201

    @app.route('/login', methods=['POST'])
    def login():

        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({'error': 'Missing fields'}), 400

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM company WHERE email = %s', (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and bcrypt.check_password_hash(user['password'], password):
            token = jwt.encode({
                'user_id': user['id'],
                'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
            }, os.getenv('SECRET_KEY'), algorithm='HS256')

            return jsonify({'message': 'Login successful', 'token': token}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 400

    @app.route('/payment-sms-code', methods=['POST'])
    def update_variable():
        print(request.json.get('code'))
        new_value = request.json.get('code')
        smsCode.value = new_value
        return {'status': 'success'}
    @app.route('/<id>', methods=['GET'])
    def test(id):
        print(id)
        return jsonify('YARRAK KAFA MERTO')

    @app.route('/sms-code', methods=['POST'])
    def getCodeVerificationCode():
        new_value = request.json.get('code')
        smsCode.value = new_value
        return jsonify(request.json.get('code'))

    @app.route('/approve', methods=['POST'])
    def visaApprove():
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400

        file = request.files['file']
        print(file)
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        try:
            # Read the file into a DataFrame
            df = er.read_excel(file)

            # İşlemin geri kalanını buraya ekleyin
            # ...

            return jsonify({'message': 'File processed successfully'})

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    @app.route('/<user_id>', methods=['GET'])
    def visaReject(user_id):
        return jsonify(user_id)

    return app

