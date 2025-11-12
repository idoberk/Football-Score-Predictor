from sqlalchemy.orm import mapped_column, Mapped
from app.db.base import Base

class Match(Base):
    __tablename__ = "matches"
    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(nullable=False)
    