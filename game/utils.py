"""
Utility Functions and Classes
Pure functions and helper classes for functional programming approach
"""

import math
from dataclasses import dataclass
from typing import List, Tuple
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT

@dataclass
class Vector2D:
    """Immutable vector class for functional programming approach"""
    x: float
    y: float
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0, 0)
        return Vector2D(self.x / mag, self.y / mag)
    
    def dot(self, other):
        """Dot product with another vector"""
        return self.x * other.x + self.y * other.y
    
    def angle(self):
        """Get angle of vector in radians"""
        return math.atan2(self.y, self.x)

# Pure functions for game logic
def clamp(value: float, min_val: float, max_val: float) -> float:
    """Pure function to clamp a value between min and max"""
    return max(min_val, min(value, max_val))

def wrap_position(pos: Vector2D, width: int = SCREEN_WIDTH, height: int = SCREEN_HEIGHT) -> Vector2D:
    """Pure function to wrap position around screen boundaries"""
    return Vector2D(pos.x % width, pos.y % height)

def distance_between(pos1: Vector2D, pos2: Vector2D) -> float:
    """Pure function to calculate distance between two points"""
    return math.sqrt((pos1.x - pos2.x)**2 + (pos1.y - pos2.y)**2)

def rotate_point(point: Vector2D, angle: float) -> Vector2D:
    """Pure function to rotate a point around origin"""
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return Vector2D(
        point.x * cos_a - point.y * sin_a,
        point.x * sin_a + point.y * cos_a
    )

def angle_between_points(from_pos: Vector2D, to_pos: Vector2D) -> float:
    """Pure function to calculate angle between two points"""
    diff = to_pos - from_pos
    return math.atan2(diff.y, diff.x)

def normalize_angle(angle: float) -> float:
    """Pure function to normalize angle to [-π, π] range"""
    while angle > math.pi:
        angle -= 2 * math.pi
    while angle < -math.pi:
        angle += 2 * math.pi
    return angle

def angle_difference(angle1: float, angle2: float) -> float:
    """Pure function to calculate the shortest angular difference"""
    diff = angle2 - angle1
    return normalize_angle(diff)

def lerp(a: float, b: float, t: float) -> float:
    """Linear interpolation between two values"""
    return a + (b - a) * clamp(t, 0.0, 1.0)

def random_velocity(min_speed: float, max_speed: float) -> Vector2D:
    """Generate random velocity vector"""
    import random
    angle = random.uniform(0, 2 * math.pi)
    speed = random.uniform(min_speed, max_speed)
    return Vector2D(math.cos(angle) * speed, math.sin(angle) * speed)