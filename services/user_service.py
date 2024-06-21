from flask import jsonify, redirect, url_for
from flask_login import login_user
from repositories.user_repository import UserRepository


class UserService:

    @staticmethod
    def login(nickname, password):
        user = UserRepository.get_by_nickname_and_password(nickname, password)
        if user:
            login_user(user)
            print(f"[DEBUG] Login successful for user: {nickname}")
            return True
        else:
            print(f"[DEBUG] Invalid login attempt for user: {nickname}")
            return False

    @staticmethod
    def register(name, nickname, password):
        if UserRepository.get_by_nickname(nickname):
            print(f"[DEBUG] Registration failed: User {nickname} already exists.")
            return False

        UserRepository.add_user(name, nickname, password)
        print(f"[DEBUG] User registered: {nickname}")
        return True
