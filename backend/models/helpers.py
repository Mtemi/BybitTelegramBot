from db import db

class BaseClass():
    _abstract__ = True

    @classmethod
    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
