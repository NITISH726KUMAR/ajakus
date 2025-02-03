# app.py
from flask import Flask, request, jsonify, render_template
from queries import (
    get_employees_by_department,
    get_department_manager,
    get_employees_hired_after,
    get_total_salary_expense
)
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    query_type = data.get('type')
    parameters = data.get('parameters', {})

    try:
        if query_type == 'employees_by_department':
            department = parameters.get('department')
            employees = get_employees_by_department(department)
            return jsonify(employees)

        elif query_type == 'department_manager':
            department = parameters.get('department')
            manager = get_department_manager(department)
            return jsonify(manager)

        elif query_type == 'employees_hired_after':
            date = datetime.strptime(parameters.get('date'), '%Y-%m-%d').date()
            employees = get_employees_hired_after(date)
            return jsonify(employees)

        elif query_type == 'total_salary_expense':
            department = parameters.get('department')
            total = get_total_salary_expense(department)
            return jsonify(total)

        else:
            return jsonify({"error": "Unsupported query type"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)