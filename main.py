from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session

from models.base import engine
from models.courses import Course
from models.users import User


# Base.metadata.create_all(engine)

# with Session(engine) as session:
#     data = [
#         {
#             'id': 1,
#             'name': 'Texnika',
#             'slug': 'texnika'
#         }
#     ]
#     query = insert(Category).values(data)
#     session.execute(query)
#     session.commit()

with Session(engine) as session:
    while True:
        print("""
    1.Kurs qo'shish
    2.Kurs o'chirish
    3.Kursni o'zgartirish
    4.Kurslarni ko'rish
    5.Student qo'shish
    6.Student o'chirish
    7.Studentni o'zhartirish
    8.Studentlarni ko'rish
    0.Exit
    """)

        t = input('Tanlang: ')
        if t == '1':
            name = input('Kursning nomi: ')
            session.execute(insert(Course).values({"name": name}))
            session.commit()

        elif t == '2':
            _id = int(input("O‘chiriladigan kurs id: "))
            session.execute(delete(Course).filter(Course.id == _id))
            session.commit()

        elif t == '3':
            _id = int(input("O'zgartiriladigan kurs id: "))
            new_name = input("Kursning yangi nomi: ")
            query = update(Course).filter(Course.id == _id).values({"name": new_name})
            session.execute(query)
            session.commit()

        elif t == '4':
            courses = session.execute(select(Course.id, Course.name).order_by(Course.id))
            for course in courses:
                print(f"{course.id}. {course.name}")

        elif t == '5':
            name = input('Studentning ismi: ')
            phone = input('Studentning phone ni: ')
            session.execute(insert(User).values({"first_name": name, "phone": phone}))
            session.commit()

        elif t == '6':
            _id = int(input("O‘chiriladigan studentning id si: "))
            session.execute(delete(User).filter(User.id == _id))
            session.commit()

        elif t == '7':
            _id = int(input("O'zgartiriladigan studentning id si: "))
            new_name = input("Studentning yangi ismi: ")
            new_phone = input("Studentning yangi phone ni: ")
            session.execute(update(User).filter(User.id == _id).values({"first_name": new_name, "phone": new_phone}))
            session.commit()

        elif t == '8':
            students = session.execute(select(User.id, User.first_name, User.phone).order_by(User.id))
            for student in students:
                print(f"{student.id}. {student.first_name} ({student.phone})")

        elif t == '0':
            break













