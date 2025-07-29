"""
Game constants
Centralised location for all game constants and configuration
"""
# Screen settings
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

# Game physics
SHIP_MAX_SPEED = 300
SHIP_THRUST_POWER = 400
SHIP_ROTATION_SPEED = 5
SHIP_SIZE = 15
DRAG_FACTOR = 0.98

# Combat settings
BULLET_SPEED = 500
BULLET_SIZE = 3
BULLET_LIFETIME = 2000  # milliseconds
SHOT_COOLDOWN = 300  # milliseconds
BULLET_DAMAGE = 20
COLLISION_DAMAGE = 1
PLAYER_COLLISION_DAMAGE = 0.5

# Game settings
INITIAL_HEALTH = 100
ASTEROID_COUNT = 5
ASTEROID_MIN_SIZE = 20
ASTEROID_MAX_SIZE = 40

# AI settings
AI_REACTION_TIME = 0.1  # seconds
AI_SHOOTING_ACCURACY = 0.8  # 0.0 to 1.0
AI_EVASION_DISTANCE = 100  # pixels
AI_AGGRESSION = 0.7  # 0.0 to 1.0 (how likely to pursue vs evade)