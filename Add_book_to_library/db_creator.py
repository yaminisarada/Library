from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///library1.db', echo=True)
Base = declarative_base()


class Academic(Base):
    __tablename__ = "academics"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return "{}".format(self.name)


class Biography(Base):
    """"""
    __tablename__ = "biography"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(String)
    publisher = Column(String)
    media_type = Column(String)

    academics_id = Column(Integer, ForeignKey("academics.id"))
    academics = relationship("Academic", backref=backref(
        "biography", order_by=id))


# create tables
Base.metadata.create_all(engine)