from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import String, Integer, DateTime, ForeignKey, CheckConstraint, Index, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db.base import Base

class Match(Base):
    """
    Relationships:
    - competition: The competition this match belongs to (La Liga, Champions League, Copa Del Rey, etc...)
    - home_team: The home team
    - away_team: The away team
    - prediction: ML-generated prediction for this match (one-to-one)
    """
    __tablename__ = "matches"

    id: Mapped[int] = mapped_column(primary_key=True)

    external_id: Mapped[int] = mapped_column(Integer, unique=True, nullable=False, index=True) # External team id API reference

    competition_id: Mapped[int] = mapped_column(ForeignKey("competitions.id", ondelete="CASCADE"), nullable=False, index=True)

    home_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id", ondelete="CASCADE"), nullable=False, index=True)

    away_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id", ondelete="CASCADE"), nullable=False, index=True)
    
    match_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, index=True)

    venue: Mapped[Optional[str]] = mapped_column(String(100))

    season: Mapped[int] = mapped_column(Integer, nullable=False, index=True)

    round: Mapped[Optional[str]] = mapped_column(String(50))

    home_score: Mapped[Optional[int]] = mapped_column(Integer)

    away_score: Mapped[Optional[int]] = mapped_column(Integer)

    status: Mapped[str] = mapped_column(String(20), default="scheduled", nullable=False, index=True)

    referee: Mapped[Optional[str]] = mapped_column(String(100))

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)

    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    competition: Mapped["Competition"] = relationship("Competition", back_populates="matches", lazy="joined")

    home_team: Mapped["Team"] = relationship("Team", foreign_keys=[home_team_id], back_populates="home_matches", lazy="joined")

    away_team: Mapped["Team"] = relationship("Team", foreign_keys=[away_team_id], back_populates="away_matches", lazy="joined")

    # TODO: Add prediction relationship

    # Table-level constraints

    __table_args__ = (
        CheckConstraint(
            "(home_score IS NULL OR home_score >= 0) AND (away_score IS NULL OR away_score >= 0)", name="check_scores_positive"
        ),
        CheckConstraint(
            "home_team_id != away_team_id",
            name="check_different_teams"
        ),
        CheckConstraint(
            "status IN ('scheduled', 'live', 'completed', 'postponed', 'cancelled')",
            name="check_status"
        ),
        UniqueConstraint(
            "competition_id", "season", "home_team_id", "away_team_id", "match_date", name="unique_match"
        ),
        Index("idx_matches_comp_date", "competition_id", "match_date"),
        Index("idx_matches_team_date_home", "home_team_id", "match_date"),
        Index("idx_matches_team_date_away", "away_team_id", "match_date"),
        Index("idx_matches_status_date", "status", "match_date"),
        )

    def __repr__(self) -> str:
        """String representation for debugging"""
        return (
            f"<Match(id={self.id}, "
            f"home_team_id={self.home_team_id}, "
            f"away_team_id={self.away_team_id}, "
            f"date={self.match_date.strftime('%d-%m-%Y')}, "
            f"status='{self.status}')>"
        )

    @property
    def is_upcoming(self) -> bool:
        """Check if match is upcoming (scheduled and in the future)"""
        return self.status == "scheduled" and self.match_date > datetime.now(timezone.utc)

    @property
    def is_completed(self) -> bool:
        """Check if match is completed"""
        return self.status == "completed"

    @property
    def is_live(self) -> bool:
        """Check if match is currently live"""
        return self.status == "live"

    @property
    def has_result(self) -> bool:
        """Check if match has a final result"""
        return self.home_score is not None and self.away_score is not None

    @property
    def winner(self) -> Optional[str]:
        """Determine the winner of the match"""
        if not self.has_result:
            return None
        
        if self.home_score > self.away_score:
            return "home"
        elif self.away_score > self.home_score:
            return "away"
        else:
            return "draw"

    def involves_team(self, team_id: int) -> bool:
        """Check if this match involves a specific team"""
        return self.home_team_id == team_id or self.away_team_id == team_id