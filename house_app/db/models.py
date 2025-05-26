from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional, List
from datetime import datetime
from house_app.db.database import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    username: Mapped[str] = mapped_column(String(40), unique=True)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    tokens: Mapped[List["RefreshToken"]] = relationship("RefreshToken", back_populates='user',
                                                        cascade='all, delete')


class House(Base):
    __tablename__ = "houses"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    area: Mapped[Optional[int]] = mapped_column(Integer)
    year: Mapped[Optional[int]] = mapped_column(Integer)
    garage: Mapped[Optional[int]] = mapped_column(Integer)
    total_basement: Mapped[Optional[int]] = mapped_column(Integer)
    bath: Mapped[Optional[int]] = mapped_column(Integer)
    overall_quality: Mapped[Optional[int]] = mapped_column(Integer)
    neighborhood: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    price: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    



class RefreshToken(Base):
    __tablename__ = "refresh_token"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    token: Mapped[str] = mapped_column(String, nullable=False)
    created_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_profiles.id'))
    user: Mapped['UserProfile'] = relationship('UserProfile', back_populates='tokens')

