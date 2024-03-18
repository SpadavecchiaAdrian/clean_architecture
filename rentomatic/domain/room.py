from pydantic import BaseModel
import uuid


class Room(BaseModel):
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float
