from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@db:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Backend API is running!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
