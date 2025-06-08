from dataclasses import dataclass
from datetime import datetime

@dataclass
class Tournament:
  id: int
  name: str
  max_players: int
  start_at: datetime
