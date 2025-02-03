# queries.py
from sqlalchemy import func
from database import session
from models import Department, Employee

def get_employees_by_department(department_name):
    try:
        employees = session.query(Employee).join(
            Department, Employee.department_id == Department.id
        ).filter(Department.name == department_name).all()
        
        if not employees:
            return "No employees found in this department."
        return [emp.name for emp in employees]
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_department_manager(department_name):
    try:
        department = session.query(Department).filter(Department.name == department_name).first()
        if department and department.manager:
            return department.manager.name
        return "No manager found for this department."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_employees_hired_after(date):
    try:
        employees = session.query(Employee).filter(Employee.hire_date > date).all()
        if not employees:
            return "No employees hired after this date."
        return [emp.name for emp in employees]
    except Exception as e:
        return f"An error occurred: {str(e)}"

def get_total_salary_expense(department_name):
    try:
        total = session.query(func.sum(Employee.salary)).join(
            Department, Employee.department_id == Department.id
        ).filter(Department.name == department_name).scalar()
        return total or 0
    except Exception as e:
        return f"An error occurred: {str(e)}"