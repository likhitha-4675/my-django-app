from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Step 2: Configure Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Step 3: Initialize SQLAlchemy
db = SQLAlchemy(app)

# Step 4: Define the Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Step 5: Create the database
with app.app_context():
    db.create_all()

# Step 6: Routes

# GET all students
@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    result = []
    for student in students:
        result.append({
            'id': student.id,
            'name': student.name,
            'age': student.age
        })
    return jsonify(result)

# POST new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student added successfully'}), 201

# GET student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if student:
        return jsonify({
            'id': student.id,
            'name': student.name,
            'age': student.age
        })
    return jsonify({'error': 'Student not found'}), 404

# DELETE student by ID
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'message': 'Student deleted'})
    return jsonify({'error': 'Student not found'}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
