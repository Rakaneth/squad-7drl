from numpy import isin
import tcod
import sys
import constants.screen as sc
from gamescreen import GameScreen, WinScreen, LoseScreen, MainScreen

def main():
    tilesheet = tcod.tileset.load_tilesheet(
        'res/font/agm_16x16.png', 16, 16, tcod.tileset.CHARMAP_CP437
    )

    screens = [
        MainScreen(),
        WinScreen(),
        LoseScreen(),
    ]

    screen_manager = dict()

    for s in screens:
        screen_manager[s.name] = s
    
    cur_screen: GameScreen = screen_manager['main']

    console = tcod.Console(sc.SCR_W, sc.SCR_H, order='F')
    running = True
    with tcod.context.new(
        columns=console.width,
        rows=console.height,
        tileset=tilesheet
    ) as context:
        while running:
            #render
            console.clear()
            cur_screen.render(console)
            context.present(console)

            #input
            for ev in tcod.event.wait():
                context.convert_event(ev)
                hr = cur_screen.dispatch(ev)
                if hr:
                    running = hr.running
                    if running:
                        if hr.screen:
                            cur_screen = screen_manager[hr.screen]

if __name__ == '__main__':
    main()
    sys.exit()