from datetime import datetime

from sqlalchemy import Integer, create_engine, DateTime
from sqlalchemy.orm import declared_attr, Mapped, DeclarativeBase, mapped_column
from sqlalchemy.sql.functions import now


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, sort_order=-1)

    @declared_attr
    def __tablename__(cls):
        name = cls.__name__[0].lower()

        for i in cls.__name__[1:]:
            if i.isupper():
                name += '_' + i.lower()
            else:
                name += i

        if name.endswith('y'):
            name = name[:-1] + 'ie'
        return name.lower() + 's'


class CreatedBase(Base):
    __abstract__ = True
    updated_at: Mapped[datetime] = mapped_column(DateTime, insert_default=now(), server_onupdate=now(), sort_order=99)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=now(), sort_order=100)


pg_url = "postgresql://postgres:1@localhost:5432/sqlalchemy_db"

engine = create_engine(pg_url)