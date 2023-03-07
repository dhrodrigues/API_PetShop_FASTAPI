from sqlalchemy.orm.session import Session
from domain.tutor.tutor_model import Tutor
from domain.tutor.tutor_repository import TutorRepository
from domain.tutor.tutor_schema import TutorSchema, TutorSchemaCreate


def create (db: Session, body: TutorSchemaCreate) -> TutorSchema:
    tutor = Tutor(**body.dict())
    return TutorRepository().create(db, tutor)


def get_tutores (db: Session) -> TutorSchema:
    return TutorRepository().all(db, Tutor)

def get_tutor(db: Session, id: int) -> TutorSchema:
    return TutorRepository().filter_by_id(db, Tutor, id)
    