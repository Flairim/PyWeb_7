from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from models import Student, Group, Teacher, Subject, Grade, SessionLocal

def select_1(session: Session):
    return session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                  .join(Grade).group_by(Student.id)\
                  .order_by(desc('avg_grade')).limit(5).all()

def select_2(session: Session):
    subject_name = 'Математичний аналіз'
    return session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                  .select_from(Student)\
                  .join(Grade, Student.id == Grade.student_id)\
                  .join(Subject, Subject.id == Grade.subject_id)\
                  .filter(Subject.name == subject_name)\
                  .group_by(Student.id).order_by(desc('avg_grade')).first()

def select_3(session: Session):
    subject_name = 'Математичний аналіз'
    return session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                  .select_from(Group)\
                  .join(Student, Group.id == Student.group_id)\
                  .join(Grade, Grade.student_id == Student.id)\
                  .join(Subject, Subject.id == Grade.subject_id)\
                  .filter(Subject.name == subject_name)\
                  .group_by(Group.id).all()

def select_4(session: Session):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).all()

def select_5(session: Session):
    teacher_name = 'Хома Пелех'
    return session.query(Subject.name).join(Teacher).filter(Teacher.name == teacher_name).all()

def select_6(session: Session):
    group_name = 'Група 1'
    return session.query(Student.name).join(Group).filter(Group.name == group_name).all()

def select_7(session: Session):
    group_name = 'Група 1'
    subject_name = 'Математичний аналіз'
    return session.query(Student.name, Grade.grade)\
                  .join(Grade, Grade.student_id == Student.id)\
                  .join(Group, Group.id == Student.group_id)\
                  .join(Subject, Subject.id == Grade.subject_id)\
                  .filter(Group.name == group_name, Subject.name == subject_name).all()

def select_8(session: Session):
    teacher_name = 'Хома Пелех'
    return session.query(Teacher.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                  .join(Subject, Subject.teacher_id == Teacher.id)\
                  .join(Grade, Grade.subject_id == Subject.id)\
                  .filter(Teacher.name == teacher_name)\
                  .group_by(Teacher.id).all()

def select_9(session: Session):
    student_name = 'Олександр Ґоляш'
    return session.query(Subject.name)\
                  .join(Grade, Grade.subject_id == Subject.id)\
                  .join(Student, Student.id == Grade.student_id)\
                  .filter(Student.name == student_name).distinct().all()

def select_10(session: Session):
    student_name = 'Олександр Ґоляш'
    teacher_name = 'Анжела Овчаренко'
    return session.query(Subject.name)\
                  .select_from(Subject)\
                  .join(Grade, Grade.subject_id == Subject.id)\
                  .join(Student, Student.id == Grade.student_id)\
                  .join(Teacher, Teacher.id == Subject.teacher_id)\
                  .filter(Student.name == student_name, Teacher.name == teacher_name)\
                  .distinct().all()



