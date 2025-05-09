from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Users(db.Model):
    __tablename__='users'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "first name": self.first_name,
            "last name": self.last_name
            # do not serialize the password, its a security breach
        }

class Posts(db.Model):
    __tablename__='posts'
    id: Mapped[int] = mapped_column(primary_key=True)
    users_id: Mapped[int] = mapped_column()

    def serialize(self):
        return {
            "id": self.id,
            "user": self.users_id,
        }

class Comments(db.Model):
    __tablename__='comments'
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(250))
    author_id: Mapped[int] = mapped_column()
    posts_id: Mapped[int] = mapped_column()


    def serialize(self):
        return {
            "id": self.id,
            "comment": self.comment_text,
            "author": self.author_id,
            "post": self.posts_id
        }
    
class Media(db.Model):
    __tablename__='media'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    type_media: Mapped[int] = mapped_column("enum??")
    url: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    posts_id: Mapped[int] = mapped_column()

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type_media,
            "link": self.url,
            "post": self.posts_id
        }
