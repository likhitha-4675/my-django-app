from flask import Flask, jsonify, request
app=Flask(__name__)

students=[
    {"id": 1, "name": "ABC", "age":21},
    {"id": 2, "name": "XYZ", "age":22},
    {"id": 3, "name": "PQR", "age":23},
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404


@app.route('/students',methods=['POST'])
def add_student():
    new_student=request.get_json()
    new_student[id]=student[-1]['id']+ 1 if student else 1
    students.append(new_student)
    return jsonify(new_student) , 201

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    # Find the student by ID
    student = next((s for s in students if s['id'] == student_id), None)

    if student:
        # Remove from the list
        students = [s for s in students if s['id'] != student_id]
        return jsonify({"message": "Student deleted"}), 200
    else:
        return jsonify({"error": "Student not found"}), 404




if __name__=='__main__':
    app.run(debug=True)