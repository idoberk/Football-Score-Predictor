"""Mock API endpoints for testing without database"""

from datetime import datetime, timedelta
from typing import List
from fastapi import APIRouter

from app.utils.common import get_utc_now

router = APIRouter(prefix="/api/v1/mock", tags=["mock"])


@router.get("/matches")
async def get_mock_matches():
    """Get mock upcoming matches for Real Madrid"""
    now = get_utc_now()
    
    matches = [
        {
            "id": 1,
            "home_team": {
                "id": 541,
                "name": "Real Madrid",
                "logo": "https://media.api-sports.io/football/teams/541.png"
            },
            "away_team": {
                "id": 529,
                "name": "Barcelona",
                "logo": "https://media.api-sports.io/football/teams/529.png"
            },
            "competition": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain"
            },
            "match_date": (now + timedelta(days=3)).isoformat(),
            "venue": "Santiago Bernabéu",
            "status": "scheduled",
            "round": "Round 25"
        },
        {
            "id": 2,
            "home_team": {
                "id": 530,
                "name": "Atletico Madrid",
                "logo": "https://media.api-sports.io/football/teams/530.png"
            },
            "away_team": {
                "id": 541,
                "name": "Real Madrid",
                "logo": "https://media.api-sports.io/football/teams/541.png"
            },
            "competition": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain"
            },
            "match_date": (now + timedelta(days=7)).isoformat(),
            "venue": "Wanda Metropolitano",
            "status": "scheduled",
            "round": "Round 26"
        },
        {
            "id": 3,
            "home_team": {
                "id": 541,
                "name": "Real Madrid",
                "logo": "https://media.api-sports.io/football/teams/541.png"
            },
            "away_team": {
                "id": 532,
                "name": "Valencia",
                "logo": "https://media.api-sports.io/football/teams/532.png"
            },
            "competition": {
                "id": 140,
                "name": "La Liga",
                "country": "Spain"
            },
            "match_date": (now + timedelta(days=10)).isoformat(),
            "venue": "Santiago Bernabéu",
            "status": "scheduled",
            "round": "Round 27"
        }
    ]
    
    return {
        "success": True,
        "count": len(matches),
        "matches": matches
    }


@router.get("/matches/{match_id}")
async def get_mock_match_detail(match_id: int):
    """Get detailed information for a specific match"""
    now = get_utc_now()
    
    match = {
        "id": match_id,
        "home_team": {
            "id": 541,
            "name": "Real Madrid",
            "logo": "https://media.api-sports.io/football/teams/541.png",
            "form": "WWDWW",
            "stats": {
                "goals_scored": 45,
                "goals_conceded": 18,
                "wins": 15,
                "draws": 3,
                "losses": 2
            }
        },
        "away_team": {
            "id": 529,
            "name": "Barcelona",
            "logo": "https://media.api-sports.io/football/teams/529.png",
            "form": "WWLWW",
            "stats": {
                "goals_scored": 42,
                "goals_conceded": 20,
                "wins": 14,
                "draws": 4,
                "losses": 2
            }
        },
        "competition": {
            "id": 140,
            "name": "La Liga",
            "country": "Spain"
        },
        "match_date": (now + timedelta(days=3)).isoformat(),
        "venue": "Santiago Bernabéu",
        "status": "scheduled",
        "round": "Round 25",
        "head_to_head": {
            "total_matches": 10,
            "real_madrid_wins": 4,
            "barcelona_wins": 4,
            "draws": 2,
            "last_5_results": ["W", "L", "D", "W", "L"]
        }
    }
    
    return {
        "success": True,
        "match": match
    }


@router.get("/predictions/{match_id}")
async def get_mock_prediction(match_id: int):
    """Get ML prediction for a specific match"""
    
    prediction = {
        "match_id": match_id,
        "predicted_outcome": "home_win",
        "confidence": 0.72,
        "predicted_score": {
            "home": 2,
            "away": 1
        },
        "probabilities": {
            "home_win": 0.72,
            "draw": 0.18,
            "away_win": 0.10
        },
        "model_version": "v1.0.0",
        "generated_at": get_utc_now().isoformat(),
        "features_used": [
            "team_form",
            "head_to_head",
            "home_advantage",
            "goals_scored_avg",
            "goals_conceded_avg"
        ],
        "explanation": {
            "key_factors": [
                "Real Madrid has won 4 of last 5 home matches",
                "Strong recent form (WWDWW)",
                "Home advantage at Santiago Bernabéu",
                "Better defensive record this season"
            ]
        }
    }
    
    return {
        "success": True,
        "prediction": prediction
    }


@router.get("/stats/team/{team_id}")
async def get_mock_team_stats(team_id: int):
    """Get team statistics"""
    
    stats = {
        "team_id": team_id,
        "team_name": "Real Madrid",
        "season": "2024/2025",
        "overall": {
            "matches_played": 20,
            "wins": 15,
            "draws": 3,
            "losses": 2,
            "goals_scored": 45,
            "goals_conceded": 18,
            "goal_difference": 27,
            "points": 48,
            "win_rate": 0.75,
            "clean_sheets": 8
        },
        "home": {
            "matches_played": 10,
            "wins": 8,
            "draws": 2,
            "losses": 0,
            "goals_scored": 25,
            "goals_conceded": 8
        },
        "away": {
            "matches_played": 10,
            "wins": 7,
            "draws": 1,
            "losses": 2,
            "goals_scored": 20,
            "goals_conceded": 10
        },
        "form": {
            "current_form": "WWDWW",
            "last_5_results": ["W", "W", "D", "W", "W"],
            "goals_last_5": 12,
            "conceded_last_5": 3
        },
        "top_scorers": [
            {"player": "Vinícius Júnior", "goals": 12},
            {"player": "Jude Bellingham", "goals": 10},
            {"player": "Rodrygo", "goals": 8}
        ]
    }
    
    return {
        "success": True,
        "stats": stats
    }
