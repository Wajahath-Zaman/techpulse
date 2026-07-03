import hashlib
import math
import re
from datetime import datetime
from typing import Optional


def clean_text(text: Optional[str]) -> str:
    """
    clean and normalize text by removing extra whitespace
    
    Args:
        text: Input text
    
    Returns:
        Cleaned Text.
    """

    if not text:
        return ""
    
    # Replace multiple whtitespaces characters with a single space

    text = re.sub(r"\s+", " ", text)

    return text.strip()

def calculate_word_count(text: str) -> int:
    '''
    Calculates the number of words that are present in the extracted text.

    Args: 
        text: Input Text.

    Returns:
        Word count in intergers.
    '''

    if not text:
        return 0
    
    return len(text.split())

def calculate_reading_time(word_count:int, words_per_minute: int=200) -> int:
    '''
    Estimate Reading Time in minutes.

    Args:
        word_count: Total number of words
        word_per_minute: Average reading speed.

    Returns:
        Estimate reading time in minutes
    '''

    if word_count <= 0:
        return 0
    
    return math.ceil(word_count / words_per_minute)


def generate_content_hash(text: str) -> str:
    '''
    Generate a SHA-256 hash for article content.

    Args:
        text: Article content.

    Returns:
        SHA-256 hash string.
    '''
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def parse_datetime(datetime_str: Optional[str]) -> Optional[datetime]:
    '''
    Parse an ISO-8601 datetime string into a datetime object.

    Args:
        datetime_str: Datetime string.

    Returns:
        datetime object if parsing succeeds, otherwise None.
    '''

    if not datetime_str:
        return None
    
    try:
        return datetime.fromisoformat(datetime_str)
    except ValueError:
        return None