import csv
from datetime import datetime
from sqlalchemy import  Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import  mapped_column, Mapped, relationship
from sqlalchemy.sql.functions import now

from models.base import Base

class Category(Base):
    name: Mapped[str] = mapped_column(String(255))
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    adverts: Mapped[list['Advert']] = relationship('Advert', back_populates='category')


    def __str__(self):
        return f"{self.id} - {self.name}"

class Advert(Base):
    name: Mapped[str] = mapped_column(String(255))
    slug: Mapped[str] = mapped_column(String(255), unique=True)
    price:Mapped[int] = mapped_column(Integer)
    description:Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String(15))

    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category: Mapped['Category'] = relationship('Category', back_populates='adverts')

    owner_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    owner: Mapped['User'] = relationship('User', back_populates='adverts')

    view_owner: Mapped[int] = mapped_column(Integer, server_default='0')
    published_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_onupdate=now())
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=now())

    images: Mapped[list['AdvertImage']] = relationship('AdvertImage', back_populates='advert')

class AdvertImage(Base):
    image: Mapped[str] = mapped_column(String(255))
    advert_id: Mapped[int] = mapped_column(ForeignKey('adverts.id'))
    advert: Mapped[Advert] = relationship('Advert', back_populates='images')



class District(Base):
    name: Mapped[str] = mapped_column(String(255))
    region_id: Mapped[int] = mapped_column(ForeignKey('regions.id'))
    region: Mapped[list['Region']] = relationship('Region', back_populates='districts')




class Region(Base):
    name: Mapped[str] = mapped_column(String(255))
    districts: Mapped[list['District']] = relationship('District', back_populates='region')








