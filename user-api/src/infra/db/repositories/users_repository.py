from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.domain.models.users import Users
from typing import List
from sqlalchemy.sql import exists, select
import hashlib


class UsersRepository:
    @classmethod
    def select_users(cls) -> List[Users] | List:
        with DBConnectionHandler() as db:
            try:
                query = db.session.query(UsersEntity).all()
                return query

            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, user_id: int) -> Users | None:
        with DBConnectionHandler() as db:
            try:
                user = (
                    db.session.query(UsersEntity)
                    .filter(UsersEntity.id == user_id)
                    .first()
                )
                return user

            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def create_user(cls, name: str, cpf: str, email: str, phone_number: str) -> None:
        with DBConnectionHandler() as db:
            try:
                data_insert = UsersEntity(
                    name=name,
                    cpf=cpf,
                    email=email,
                    phone_number=phone_number
                )

                db.session.add(data_insert)
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def update_user(cls, user_id: int, email: str, phone_number: str) -> None:
        with DBConnectionHandler() as db:
            try:
                user = (
                    db.session.query(UsersEntity)
                    .filter(UsersEntity.user_id == user_id)
                    .first()
                )

                user.name = name
                user.email = email
                user.phone_number = phone_number
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def delete_user(cls, user_id: int) -> None:
        with DBConnectionHandler() as db:
            try:
                user = (
                    db.session.query(UsersEntity)
                    .filter(UsersEntity.id == user_id)
                    .delete()
                )
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception


    @classmethod
    def get_user_by_cpf(cls, cpf: str) -> bool:
        with DBConnectionHandler() as db:
            try:
                hashed_cpf = hashlib.sha256(cpf.encode()).hexdigest()
                user = (
                    db.session.query(
                        exists()
                        .where(UsersEntity.cpf == hashed_cpf)
                    ).scalar()
                )
                return user

            except Exception as exception:
                db.session.rollback()
                raise exception
