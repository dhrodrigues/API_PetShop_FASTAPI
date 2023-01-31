from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import (Column, Integer, String, Float, ForeignKey,Date)




class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    serviço = Column(String, nullable=False)
    data = Column(String, nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    account = relationship("Pet", backref="pets", uselist=False)

    def __repr__(self) -> str:
        return f"{self.serviço}, {self.data}"

