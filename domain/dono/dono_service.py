from sqlalchemy.orm.session import Session
from domain.dono.dono_model import Dono
from domain.dono.dono_repository import DonoRepository
from domain.dono.dono_schema import DonoSchema, DonoSchemaCreate


def create (db: Session, body: DonoSchemaCreate) -> DonoSchema:
    dono = Dono(**body.dict())
    return DonoRepository().create(db, dono)


def get_donos (db: Session) -> DonoSchema:
    return DonoRepository().all(db, Dono)

def get_dono(db: Session, id: int) -> DonoSchema:
    return DonoRepository().filter_by_id(db, Dono, id)
    