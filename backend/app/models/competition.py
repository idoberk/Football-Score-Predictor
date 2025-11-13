from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Integer, DateTime, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db.base import Base

class Competition(Base):
    __tablename__ = "competitions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    external_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False, index=True)

    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    type: Mapped[str] = mapped_column(String(20), nullable=False, index=True)

    logo_url: Mapped[Optional[str]] = mapped_column(String(255))

    country: Mapped[Optional[str]] = mapped_column(String(50), index=True)

    tier: Mapped[Optional[int]] = mapped_column(Integer)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)

    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    matches: Mapped[List["Match"]] = relationship("Match", back_populates="competition", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint(
            "type IN ('league', 'cup', 'international', 'friendly')",
            name="check_competition_type"
        ),
    )

    def __repr__(self) -> str:
        return f"<Competition(id={self.id}, name='{self.name}')>"