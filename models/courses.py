from sqlalchemy import String, ForeignKey, Table, Column, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base import CreatedBase, Base

user_courses = Table(
    'user_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)


class Course(CreatedBase):
    name: Mapped[str] = mapped_column(String(255))
    students: Mapped[list['User']] = relationship('User', secondary=user_courses, back_populates='courses')

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


# class UserCourse(CreatedBase):
#     student_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
#     course_id: Mapped[int] = mapped_column(ForeignKey('courses.id'))
#
#     __table_args__ = (
#         UniqueConstraint("user_id", "course_id"),
#     )