# add_sample_data.py
from datetime import datetime
from database import session
from models import Department, Employee

def add_sample_data():
    try:
        # Add sample departments
        hr_department = Department(name="HR", manager_id=1)
        engineering_department = Department(name="Engineering", manager_id=2)
        session.add(hr_department)
        session.add(engineering_department)
        session.commit()

        # Add sample employees
        employees = [
            Employee(name="John Doe", hire_date=datetime(2023, 1, 1), salary=50000, department_id=1),
            Employee(name="Jane Smith", hire_date=datetime(2022, 1, 1), salary=70000, department_id=1),
            Employee(name="Alice Brown", hire_date=datetime(2023, 5, 1), salary=60000, department_id=2),
            Employee(name="Bob White", hire_date=datetime(2023, 6, 1), salary=65000, department_id=2),
        ]
        session.add_all(employees)
        session.commit()

        # Update department managers
        hr_department.manager_id = 2  # Jane Smith is the manager of HR
        engineering_department.manager_id = 4  # Bob White is the manager of Engineering
        session.commit()

        print("Sample data added successfully!")
    except Exception as e:
        session.rollback()
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    add_sample_data()