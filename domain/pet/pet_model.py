from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import (Column, Integer, String, Float, ForeignKey)




class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    raca = Column(String, nullable=False)
    cor = Column(String, nullable=False)
    destination_pet = Column(String, nullable=False)
    dono_id = Column(Integer, ForeignKey("dono.id"))
    account = relationship("Dono", backref="dono", uselist=False)

    def __repr__(self) -> str:
        return f"{self.name}, {self.raca}"

