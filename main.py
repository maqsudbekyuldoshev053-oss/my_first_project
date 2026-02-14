from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session

# from models.base import engine

# from models.courses import Course
# from models.users import User
from models.films import Film, Category

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
#
# with Session(engine) as session:
#     while True:
#         print("""
#     1.Kurs qo'shish
#     2.Kurs o'chirish
#     3.Kursni o'zgartirish
#     4.Kurslarni ko'rish
#     5.Student qo'shish
#     6.Student o'chirish
#     7.Studentni o'zhartirish
#     8.Studentlarni ko'rish
#     0.Exit
#     """)
#
#         t = input('Tanlang: ')
#         if t == '1':
#             name = input('Kursning nomi: ')
#             session.execute(insert(Course).values({"name": name}))
#             session.commit()
#
#         elif t == '2':
#             _id = int(input("O‘chiriladigan kurs id: "))
#             session.execute(delete(Course).filter(Course.id == _id))
#             session.commit()
#
#         elif t == '3':
#             _id = int(input("O'zgartiriladigan kurs id: "))
#             new_name = input("Kursning yangi nomi: ")
#             query = update(Course).filter(Course.id == _id).values({"name": new_name})
#             session.execute(query)
#             session.commit()
#
#         elif t == '4':
#             courses = session.execute(select(Course.id, Course.name).order_by(Course.id))
#             for course in courses:
#                 print(f"{course.id}. {course.name}")
#
#         elif t == '5':
#             name = input('Studentning ismi: ')
#             phone = input('Studentning phone ni: ')
#             session.execute(insert(User).values({"first_name": name, "phone": phone}))
#             session.commit()
#
#         elif t == '6':
#             _id = int(input("O‘chiriladigan studentning id si: "))
#             session.execute(delete(User).filter(User.id == _id))
#             session.commit()
#
#         elif t == '7':
#             _id = int(input("O'zgartiriladigan studentning id si: "))
#             new_name = input("Studentning yangi ismi: ")
#             new_phone = input("Studentning yangi phone ni: ")
#             session.execute(update(User).filter(User.id == _id).values({"first_name": new_name, "phone": new_phone}))
#             session.commit()
#
#         elif t == '8':
#             students = session.execute(select(User.id, User.first_name, User.phone).order_by(User.id))
#             for student in students:
#                 print(f"{student.id}. {student.first_name} ({student.phone})")
#
#         elif t == '0':
#             break

#
# with Session(engine) as session:
#     while True:
#         print("""
#     Menyular
#         1. kurs qo'shish
#         2. kurs o'chirish
#         3. kursni o'zgartirish
#         4. kurslarni ko'rish
#         5. student qo'shish
#         6. student o'chirish
#         7. studentni o'zgartirish
#         8. kursga student qo'shish
#         9. kursdan studentni o'chirish
#         10. kursdan kursga ko'chirish
#         0.Exit
#     """)
#
#         t = input('Tanlang: ')
#         if t == '1':
#             name = input('Kursning nomi: ')
#             session.execute(insert(Course).values({"name": name}))
#             session.commit()
#
#         elif t == '2':
#             _id = int(input("O‘chiriladigan kurs id: "))
#             session.execute(delete(Course).filter(Course.id == _id))
#             session.commit()
#         elif t == '3':
#             _id = int(input("O'zgartiriladigan kurs id: "))
#             new_name = input("Kursning yangi nomi: ")
#             query = update(Course).filter(Course.id == _id).values({"name": new_name})
#             session.execute(query)
#             session.commit()
#
#         elif t == '4':
#             courses = session.execute(select(Course.id, Course.name).order_by(Course.id))
#             for course in courses:
#                 print(f"{course.id}. {course.name}")
#
#         elif t == '5':
#             name = input('Studentning ismi: ')
#             phone = input('Studentning phone ni: ')
#             session.execute(insert(User).values({"first_name": name, "phone": phone}))
#             session.commit()
#
#         elif t == '6':
#             _id = int(input("O‘chiriladigan studentning id si: "))
#             session.execute(delete(User).filter(User.id == _id))
#             session.commit()
#
#         elif t == '7':
#             _id = int(input("O'zgartiriladigan studentning id si: "))
#             new_name = input("Studentning yangi ismi: ")
#             new_phone = input("Studentning yangi phone ni: ")
#             session.execute(update(User).filter(User.id == _id).values({"first_name": new_name, "phone": new_phone}))
#             session.commit()
#
#
#         elif t == '8':
#             student_id = int(input("Kursga qo'shmoqchi bulgan studentning id si: "))
#             course_id = int(input("Student qo'shmoqchi bulgan kurs id si: "))
#             query = select(User).filter(User.id == student_id)
#             student = session.scalar(query)
#             if student is None:
#                 print("Student topilmadi.")
#             else:
#                 query = select(Course).filter(Course.id == course_id)
#                 course = session.scalar(query)
#                 if course is None:
#                     print("Kurs topilmadi.")
#                 elif course in student.courses:
#                     print("Student allaqachon ushbu coursega qo'shilgan.")
#                 else:
#                     student.courses.append(course)
#                     session.commit()
#
#         elif t == '9':
#             student_id = int(input("Kursdan o'chiriladigan studentning id si: "))
#             course_id = int(input("Student o'chiriladigan course id si: "))
#             query2 = select(User).filter(User.id == student_id)
#             student = session.scalar(query2)
#             if student is None:
#                 print("Student topilmadi.")
#             else:
#                 query2 = select(Course).filter(Course.id == course_id)
#                 course = session.scalar(query2)
#                 if course is None:
#                     print("Kurs topilmadi.")
#                 elif course not in student.courses:
#                     print("Student bu coursega biriktirilmagan.")
#                 else:
#                     student.courses.remove(course)
#                     session.commit()
#
#         elif t == '10':
#             student_id = int(input("Ko'chiriladigan studentning id si: "))
#             from_course_id = int(input("Qaysi coursedan: "))
#             to_course_id = int(input("Qaysi coursega: "))
#             query3 = select(User).filter(User.id == student_id)
#             student = session.scalar(query3)
#             if student is None:
#                 print("Student topilmadi.")
#             else:
#                 query3 = select(Course).filter(Course.id == from_course_id)
#                 from_course = session.scalar(query3)
#                 query3 = select(Course).filter(Course.id == to_course_id)
#                 to_course = session.scalar(query3)
#                 if from_course is None:
#                     print("Eski course topilmadi.")
#                 elif to_course is None:
#                     print("Yangi course topilmadi.")
#                 elif from_course not in student.courses:
#                     print("Student eski coursega biriktirilmagan.")
#                 elif to_course in student.courses:
#                     print("Student allaqachon yangi coursega biriktirilgan.")
#                 else:
#                     student.courses.remove(from_course)
#                     student.courses.append(to_course)
#                     session.commit()
#
#         elif t == '0':
#             break

# Film(id, title, description, release_year), Category(id, name)
#
# with Session(engine)  as session:
#     while True:
#         """
# 1. film qoshish
# 2. film o'chirish
# 3. film o'zgartirish
# 4. film ni korish
# 5. category qo'shish
# 6. category o'chirish
# 7. category o'zgartirish
# 8. category ni korish
# """
#
#         t = input('Tanlang: ')
#         if t == '1':
#             title = input('Film title: ')
#             session.execute(insert(Film).values({"title": title}))
#             session.commit()
#
#         elif t == '2':
#             _id = int(input("Film id: "))
#             session.execute(delete(Film).filter(Film.id == _id))
#             session.commit()
#
#         elif t == '3':
#             _id = int(input("Film id: "))
#             new_title = input("Film new title: ")
#             query = update(Film).filter(Film.id == _id).values({"title": new_title})
#             session.execute(query)
#             session.commit()
#
#         elif t == '4':
#             films = session.execute(select(Film.id, Film.title).order_by(Film.id))
#             for film in films:
#                 print(f"{film.id}. {film.title}")
#
#         elif t == '5':
#             name = input('Category name: ')
#             session.execute(insert(Category).values({"first_name": name}))
#             session.commit()
#
#         elif t == '6':
#             _id = int(input("Category id : "))
#             session.execute(delete(Category).filter(Category.id == _id))
#             session.commit()
#
#         elif t == '7':
#             _id = int(input("Category id : "))
#             new_name = input("Category new name: ")
#             session.execute(update(Category).filter(Category.id == _id).values({"first_name": new_name}))
#             session.commit()
#
#         elif t == '8':
#             categories = session.execute(select(Category.id, Category.name).order_by(Category.id))
#             for category in categories:
#                 print(f"{category.id}. {category.first_name} ")
#
#         elif t == '0':
#             break

#
# with Session(engine) as session:
#     while True:
#         print("""
#     1. film qoshish
#     2. film o'chirish
#     3. film o'zgartirish
#     4. film ni korish
#     5. category qo'shish
#     6. category o'chirish
#     7. category o'zgartirish
#     8. category ni korish
#     """)
#
#         t = input('Tanlang: ')
#         if t == '1':
#             title = input('Film title: ')
#             description = input('Film description: ')
#             release_year = int(input('Film release_year: '))
#             query = (insert(Film).values(title=title, description=description, release_year=release_year ))
#             session.execute(query)
#             session.commit()
#
#         elif t == '2':
#             _id = int(input("Film id: "))
#             query = (delete(Film).filter(Film.id == _id))
#             session.execute(query)
#             session.commit()
#
#         elif t == '3':
#             _id = int(input("Film id: "))
#             new_title = input("Film new title: ")
#             new_description = input('Film description: ')
#             new_release_year = int(input('Film release_year: '))
#             query = update(Film).filter(Film.id == _id).values(title=new_title, description=new_description, release_year=new_release_year)
#             session.execute(query)
#             session.commit()
#
#         elif t == '4':
#             films = session.execute(select(Film.id, Film.title).order_by(Film.id))
#             if not films:
#                 print("Film topilmadi!!!")
#             else:
#                 for film in films:
#                     print(f"{film.id}. {film.title}")
#
#         elif t == '5':
#             name = input('Category name: ')
#             query = (insert(Category).values({"name": name}))
#             session.execute(query)
#             session.commit()
#
#         elif t == '6':
#             _id = int(input("Category id: "))
#             query = (delete(Category).filter(Category.id == _id))
#             session.execute(query)
#             session.commit()
#
#         elif t == '7':
#             _id = int(input("Category id: "))
#             new_name = input("Category new name: ")
#             query = (update(Category).filter(Category.id == _id).values({"name": new_name}))
#             session.execute(query)
#             session.commit()
#
#         elif t == '8':
#             query = (select(Category.id, Category.name).order_by(Category.id))
#             categories = session.execute(query)
#             for category in categories:
#                 print(f"{category.id}. {category.name} ")
#
#         elif t == '0':
#             break
























































