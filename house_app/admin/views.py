from sqladmin import ModelView
from house_app.db.models import UserProfile


class UserAdmin(ModelView, model=UserProfile):
    column_list = [column.name for column in UserProfile.__table__.columns]