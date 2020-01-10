import uuid
from ..model.user_model import User
from .. import db_sql


def add_new_user():
    user = User(id=str(uuid.uuid4()), username='test', email='test@gmail.com')
    db_sql.session.add(user)
    db_sql.session.commit()
