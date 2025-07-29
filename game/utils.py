"""
Utility functions and Classes
Pure functions and helper classes for functional programming approach
"""

import math
from dataclasses import dataclass
from typing import List, Tuple
from .constants import SCREEN_HEIGHT, SCREEN_WIDTH

@dataclass
class Vector2D:
    # vector class immutable for functional programming
    x:float
    y:float
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    