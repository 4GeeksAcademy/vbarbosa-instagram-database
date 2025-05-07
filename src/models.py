from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False)
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
    
class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(120))
    author_id: Mapped[int] = mapped_column("user.id")
    post_id: Mapped[int] = mapped_column("post.id")


    def serialize(self):
        return {
            "id": self.id,
            "comment": self.comment_text,
            "author": self.authot_id,
            "post": self.post_id
        }

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column("user.id")

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_id
        }
    
class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type_media: Mapped[int] = mapped_column("enum??")
    url: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    post_id: Mapped[str] = mapped_column("post.id")

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type_media,
            "link": self.url,
            "post": self.post_id
        }
