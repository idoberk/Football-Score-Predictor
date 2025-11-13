from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db.base import Base

class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    external_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False, index=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    short_name: Mapped[Optional[str]] = mapped_column(String(50))

    logo_url: Mapped[Optional[str]] = mapped_column(String(255))

    country: Mapped[Optional[str]] = mapped_column(String(50), index=True)

    founded_year: Mapped[Optional[int]] = mapped_column(Integer)

    venue_name: Mapped[Optional[str]] = mapped_column(String(100))

    venue_capacity: Mapped[Optional[int]] = mapped_column(Integer)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)

    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    home_matches: Mapped[List["Match"]] = relationship("Match", foreign_keys="Match.home_team_id", back_populates="home_team")

    away_matches: Mapped[List["Match"]] = relationship("Match", foreign_keys="Match.away_team_id", back_populates="away_team")


    def __repr__(self) -> str:
        return f"<Team(id={self.id}, name='{self.name}')>"