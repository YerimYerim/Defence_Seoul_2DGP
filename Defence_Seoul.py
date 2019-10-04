from pico2d import *
IMG_HEIGHT = 701
IMG_WIDTH = 1648
BackWIDTH = 961
BackHIEGHT = 567
tower_IMG_SIZE = 140
Boat_IMG_SIZE = 135
Tile_SIZE = 57
x = 0
y = 0

class RECT:
    left = 0
    bot = 0
    right = 0
    top = 0

class Tower:
    Type = -1
    Level = 1
    R = RECT()


class Boat:
    hp = 1
    speed = 1
    type = 1    # 일반 1  보스 2
    R = RECT()
    R.bot = 7 * Tile_SIZE
    R.left = -Tile_SIZE
    R.right = 0
    R.top = 8 * Tile_SIZE

    def draw(self):
        BackGround.clip_draw(32, 6, Boat_IMG_SIZE, Boat_IMG_SIZE ,
                             (self.R.left+self.R.right) / 2, (self.R.top + self.R.bot) / 2, Tile_SIZE, Tile_SIZE)

    def move(self):
  #
        if  self.R.right < Tile_SIZE * 2 - 2:
            self.R.left += self.speed
            self.R.right += self.speed
        elif self.R.right == Tile_SIZE * 2 - 2 and self.R.bot > 6 * Tile_SIZE:
            self.R.bot -= self.speed
            self.R.top -= self.speed
        elif self.R.right >= Tile_SIZE * 2 - 2 and self.R.bot == 6 * Tile_SIZE:
            self.R.left += self.speed
            self.R.right += self.
        elif self.R.right >= Tile_SIZE * 2 - 2





 #




open_canvas(BackWIDTH, BackHIEGHT)

BackGround = None
running = True
def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:

        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
    pass


BackGround = load_image('resources.png')
B = Boat()
while running:
    clear_canvas()

    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2, BackHIEGHT/2 )
    B.move()
    B.draw()
    update_canvas()
    handle_events()
    delay(0.02)

close_canvas()

