"""
Configuration and Environment Variables
Production-ready settings for Cinemagic API Hub
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# TMDB API Configuration
TMDB_API_KEY = os.getenv("TMDB_API_KEY", "8265bd1679663a7ea12ac168da84d2e8")
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p"

# API Timeouts
API_TIMEOUT = int(os.getenv("API_TIMEOUT", 5))
CACHE_TTL = int(os.getenv("CACHE_TTL", 86400))  # 24 hours

# Model Configuration
MODEL_PATHS = {
    "movies_list": "movies_list.pkl",
    "vectorizer": "vectorizer.pkl",
    "vectors": "vectors.pkl"
}

# UI Configuration
APP_TITLE = "CINEMAGIC | AI Movie Recommender"
APP_ICON = "🎬"
RECOMMENDATIONS_COUNT = 6
TRENDING_COUNT = 12
CHAT_HISTORY_DISPLAY = 3

# Feature Flags
ENABLE_TRAILER = True
ENABLE_EXTERNAL_SEARCH = True
ENABLE_COLLABORATIVE_FILTERING = False  # Future enhancement

# Logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
