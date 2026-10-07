from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "students.json")


def read_students():
    with open(DATA_FILE, "r", encoding="utf-8-sig") as f:
        return json.load(f)


def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8-sig") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)


@app.route("/")
def home():
    students = read_students()
    return render_template("index.html", students=students)


@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "student": os.environ.get("MSSV", "2412111047")
    })


@app.route("/api/students", methods=["GET"])
def get_students():
    students = read_students()
    lop = request.args.get("lop")

    if lop:
        students = [s for s in students if s["lop"] == lop]

    return jsonify(students)


@app.route("/api/students/<int:student_id>")
def get_student(student_id):
    students = read_students()

    for student in students:
        if student["id"] == student_id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404

@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.get_json()

    required = ["mssv", "ho_ten", "lop", "diem"]

    if not data or any(field not in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    if any(str(data[field]).strip() == "" for field in ["mssv", "ho_ten", "lop"]):
        return jsonify({"error": "Fields must not be empty"}), 400
    try:
        diem = float(data["diem"])
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid score"}), 400

    if diem < 0 or diem > 10:
        return jsonify({"error": "Score must be between 0 and 10"}), 400

    students = read_students()

    new_id = max([s["id"] for s in students], default=0) + 1

    student = {
        "id": new_id,
        "mssv": data["mssv"],
        "ho_ten": data["ho_ten"],
        "lop": data["lop"],
        "diem": diem
    }

    students.append(student)
    save_students(students)

    return jsonify(student), 201


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
