from pico2d import *
BackWIDTH = 961
BackHIEGHT = 567
tower_IMG_SIZE = 140

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


while running:
    clear_canvas()

    if BackGround is None:
        BackGround = load_image('resources.png')
    BackGround.clip_draw(666, 708-583, BackWIDTH, BackHIEGHT, BackWIDTH/2 , BackHIEGHT/2 )

    update_canvas()
    handle_events()

close_canvas()

