from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/mydatabase'
db = SQLAlchemy(app)

# Define Models
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # income or expense
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    date = db.Column(db.Date, nullable=False)

# Create Transaction Endpoint
@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.json
    new_transaction = Transaction(
        type=data['type'],
        amount=data['amount'],
        category=data['category'],
        description=data.get('description', ''),
        date=data['date']
    )
    db.session.add(new_transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction added!'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
