from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime,
    ForeignKey
)

from database import Base

from datetime import datetime


# =========================================================
# TRIP MODEL
# =========================================================

class Trip(Base):

    __tablename__ = "trips"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(200),
        nullable=False
    )

    category = Column(
        String(100)
    )

    route = Column(
        String(500)
    )

    image = Column(
        String(500)
    )

    rating = Column(
        Float,
        default=0
    )

    reviews = Column(
        Integer,
        default=0
    )

    price = Column(
        Float
    )

    duration = Column(
        String(100)
    )

    difficulty = Column(
        String(50)
    )

    description = Column(
        Text
    )

    tags = Column(
        String(500)
    )

    recommended_for = Column(
        String(500)
    )

    ai_match = Column(
        Integer,
        default=0
    )


# =========================================================
# USER MODEL
# =========================================================

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    full_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    profile_image = Column(
        String(500),
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


# =========================================================
# AI DESTINATION MODEL
# =========================================================

class Destination(Base):

    __tablename__ = "destinations"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(150),
        nullable=False
    )

    district = Column(
        String(100)
    )

    category = Column(
        String(150)
    )

    description = Column(
        Text
    )

    best_for = Column(
        String(500)
    )

    tags = Column(
        String(500)
    )

    average_stay = Column(
        Integer,
        default=2
    )

    base_cost_per_person = Column(
        Float,
        default=0
    )

    hotel_cost_per_night = Column(
        Float,
        default=0
    )

    food_cost_per_day = Column(
        Float,
        default=0
    )

    transport_cost = Column(
        Float,
        default=0
    )

    rating = Column(
        Float,
        default=0
    )

    image = Column(
        String(500),
        nullable=True
    )

    latitude = Column(
        Float,
        nullable=True
    )

    longitude = Column(
        Float,
        nullable=True
    )


# =========================================================
# AI TRANSPORT COST MODEL
# =========================================================

class TravelCost(Base):

    __tablename__ = "travel_costs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    destination = Column(
        String(150),
        nullable=False
    )

    transport_type = Column(
        String(50),
        nullable=False
    )

    estimated_cost = Column(
        Float,
        default=0
    )

    duration_hours = Column(
        Float,
        default=0
    )

    comfort_level = Column(
        String(50)
    )


# =========================================================
# AI FOOTFALL MODEL
# =========================================================

class FootfallData(Base):

    __tablename__ = "footfall_data"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    destination = Column(
        String(150),
        nullable=False
    )

    visit_date = Column(
        DateTime,
        nullable=False
    )

    crowd_level = Column(
        String(50),
        nullable=False
    )

    crowd_score = Column(
        Integer,
        default=50
    )

    estimated_visitors = Column(
        Integer,
        default=0
    )


# =========================================================
# HOTEL MODEL
# =========================================================

class Hotel(Base):

    __tablename__ = "hotels"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    trip_id = Column(
        Integer,
        ForeignKey("trips.id"),
        nullable=False
    )

    name = Column(
        String(200),
        nullable=False
    )

    location = Column(
        String(200)
    )

    image = Column(
        String(500)
    )

    rating = Column(
        Float
    )

    price_per_night = Column(
        Float
    )

    room_type = Column(
        String(100)
    )

    facilities = Column(
        Text
    )

    available_rooms = Column(
        Integer,
        default=0
    )

    description = Column(
        Text
    )