from models.models import User, db


class UserRepository:

    @staticmethod
    def get_by_nickname_and_password(nickname, password):
        return User.query.filter_by(nickname=nickname, password=password).first()

    @staticmethod
    def get_by_nickname(nickname):
        return User.query.filter_by(nickname=nickname).first()

    @staticmethod
    def add_user(name, nickname, password):
        new_user = User(name=name, nickname=nickname, password=password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
