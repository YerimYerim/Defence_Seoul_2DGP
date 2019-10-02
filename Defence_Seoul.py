from pico2d import *

open_canvas()
BackGround: Image = load_image('resource.png')

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

    BackGround.clip_draw(100, 100 * 1, 100, 100, 100, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

#  delay(0.05)

close_canvas()

