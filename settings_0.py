import math

# criando tela
res = width, height = 1000, 600

HALF_WIDTH = width//2
HALF_HEIGHT = height//2
FPS = 60

#settings for the player

PLAYER_POS = 1.5,5 # minimap position
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60


FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = width // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = width // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE// 2
