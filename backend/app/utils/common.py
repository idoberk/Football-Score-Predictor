"""Common utility functions"""

import uuid
from datetime import datetime, timezone
from typing import Optional


def generate_correlation_id() -> str:
    """Generate a unique correlation ID for request tracking
    
    Returns:
        A UUID string for correlation tracking
    """
    return str(uuid.uuid4())


def get_utc_now() -> datetime:
    """Get current UTC timestamp
    
    Returns:
        Current datetime in UTC timezone
    """
    return datetime.now(timezone.utc)


def format_timestamp(dt: Optional[datetime] = None) -> str:
    """Format datetime to ISO 8601 string
    
    Args:
        dt: Datetime to format, defaults to current UTC time
        
    Returns:
        ISO 8601 formatted timestamp string
    """
    if dt is None:
        dt = get_utc_now()
    return dt.isoformat()


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Safely divide two numbers, returning default if denominator is zero
    
    Args:
        numerator: The numerator
        denominator: The denominator
        default: Value to return if denominator is zero
        
    Returns:
        Result of division or default value
    """
    if denominator == 0:
        return default
    return numerator / denominator


def clamp(value: float, min_value: float, max_value: float) -> float:
    """Clamp a value between min and max bounds
    
    Args:
        value: Value to clamp
        min_value: Minimum bound
        max_value: Maximum bound
        
    Returns:
        Clamped value
    """
    return max(min_value, min(value, max_value))
