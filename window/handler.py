from pygame import event
from dataclasses import dataclass
from typing import Callable

@dataclass
class Handler:
    event_type: int
    handler: Callable[[event.Event], None]
