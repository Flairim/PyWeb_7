from sqlalchemy.orm import Session
from faker import Faker
from datetime import datetime, timedelta
import random
from models import Student, Group, Teacher, Subject, Grade, SessionLocal

fake = Faker('uk_UA')

def create_groups(session, n=4):
    for _ in range(n):
        group = Group(name=f'Група {_ + 1}')
        session.add(group)
    session.commit()

def create_teachers(session, n=5):
    for _ in range(n):
        teacher = Teacher(name=fake.name())
        session.add(teacher)
    session.commit()

def create_students(session, n=40):
    groups = session.query(Group).all()
    for _ in range(n):
        student = Student(name=fake.name(), group=random.choice(groups))
        session.add(student)
    session.commit()

def create_subjects(session, n=8):
    teachers = session.query(Teacher).all()
    subject_names = [
        'Математичний аналіз', 'Фізика', 'Історія України', 'Інформатика',
        'Англійська мова', 'Економіка', 'Біологія', 'Географія'
    ]
    for name in subject_names[:n]:
        subject = Subject(name=name, teacher_id=random.choice(teachers).id)
        session.add(subject)
    session.commit()

def create_grades(session, n=40):
    students = session.query(Student).all()
    subjects = session.query(Subject).all()
    for _ in range(n):
        grade = Grade(student_id=random.choice(students).id, subject_id=random.choice(subjects).id, grade=random.randint(60, 100), date=fake.date_between(start_date='-1y', end_date='today'))
        session.add(grade)
    session.commit()

if __name__ == '__main__':
    session = SessionLocal()
    create_groups(session)
    create_teachers(session)
    create_students(session)
    create_subjects(session)
    create_grades(session)
