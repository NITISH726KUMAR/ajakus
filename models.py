# models.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    manager_id = Column(Integer, ForeignKey('employees.id'))

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hire_date = Column(Date, nullable=False)
    salary = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))