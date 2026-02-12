
from sqlalchemy import String, ForeignKey, Table, Column, Integer,UniqueConstraint, Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.base import CreatedBase, Base



film_category = Table(
    "film_category",
    Base.metadata,
    Column("film_id", ForeignKey("films.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
)

class Film(Base):
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text, nullable=True)
    release_year: Mapped[int] = mapped_column(Integer, nullable=True)
    # categories: Mapped[list['Category']] = relationship('Category', secondary='FilmCategory', back_populates='films')

    categories = relationship("Category", secondary=film_category, back_populates="films")

    def __str__(self):
        return f"{self.id} - {self.title}"


class Category(Base):
    name: Mapped[str] = mapped_column(String(25))
    # films: Mapped[list['Film']] = relationship('Film', secondary='FilmCategory', back_populates='categories')

    films = relationship("Film", secondary=film_category, back_populates="categories")

    def __str__(self):
        return f"{self.id} - {self.name}"


# class FilmCategory(Base):
#     film_id: Mapped[int] = mapped_column(ForeignKey('films.id'))
#     category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
#
#     __table_args__ = (
#         UniqueConstraint('film_id', 'category_id'),
#     )
#
#     def __str__(self):
#         return f'id: {self.id}, category_id: {self.category_id}, film_id: {self.film_id}'


