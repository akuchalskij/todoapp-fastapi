import attr
from injector import inject
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import scoped_session, sessionmaker

from config import settings


@inject
@attr.s(auto_attribs=True)
@attr.dataclass
class Database:
    engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()


class CustomBase(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = declarative_base(cls=CustomBase)
