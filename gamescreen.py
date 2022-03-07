import tcod
from typing import Optional

class HandleResult:
    """The result of a screen's handle function"""

    def __init__(self, running: bool=True, screen: str=None, action=None):
        self.running = running
        self.screen = screen
        self.action = action


class GameScreen(tcod.event.EventDispatch[HandleResult]):
    """Game screens superclass"""
    
    #TODO: Game data
    def __init__(self, name: str):
        self.__name = name
        self.mx = -1
        self.my = -1
    
    @property
    def name(self):
        return self.__name
    
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[HandleResult]:
        return self.handle_key(event)
    
    def ev_mousemotion(self, event: tcod.event.MouseMotion) -> Optional[HandleResult]:
        self.mx = event.tile.x
        self.my = event.tile.y
        return self.handle_mouse_move(self.mx, self.my)
    
    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[HandleResult]:
        return self.handle_mouse_clicK(event.button, self.mx, self.my)
    
    def ev_quit(self, event: tcod.event.Quit) -> Optional[HandleResult]:
        return HandleResult(False)
    
    def handle_key(self, event: tcod.event.KeyDown) -> Optional[HandleResult]:
        print(f'Key {event.sym} pressed')

    def handle_mouse_move(self, x: int, y: int) -> Optional[HandleResult]:
        print(f'Mouse moved to ({x},{y})')
    
    def render(self, console: tcod.console.Console):
        console.print(0, 0, f'This is the {self.name} screen.')
    
    def handle_mouse_click(self, button: int, x: int, y: int) -> Optional[HandleResult]:
        print(f'Button {button} clicked at ({x},{y})')
    

class MainScreen(GameScreen):
    """The main screen."""
    
    def __init__(self):
        super().__init__('main')
    
    def handle_key(self, event: tcod.event.KeyDown) -> Optional[HandleResult]:
        hr = HandleResult()
        
        match event.sym:
            case tcod.event.K_ESCAPE:
                hr.running = False
            case tcod.event.K_w:
                hr.screen = 'win'
            case tcod.event.K_l:
                hr.screen = 'lose'
        
        return hr
    
    def render(self, console: tcod.console.Console):
        super().render(console)
        console.print(0, 1, "[w] to win, [l] to lose, [Esc] to exit")


class WinScreen(GameScreen):
    """Test win screen"""

    def __init__(self):
        super().__init__('win')
    
    def handle_key(self, event: tcod.event.KeyDown) -> Optional[HandleResult]:
        hr = HandleResult()
        
        if event.sym == tcod.event.K_ESCAPE:
            hr.screen = 'main'
        
        return hr
    
    def render(self, console: tcod.console.Console):
        super().render(console)
        console.print(0, 1, '[Esc] to return to main screen.')


class LoseScreen(GameScreen):
    """Test lose screen."""

    def __init__(self):
        super().__init__('lose')
    
    def handle_key(self, event: tcod.event.KeyDown) -> Optional[HandleResult]:
        hr = HandleResult()

        if event.sym == tcod.event.K_ESCAPE:
            hr.screen = 'main'
        
        return hr
    
    def render(self, console: tcod.console.Console):
        super().render(console)
        console.print(0, 1, '[Esc] to return to main screen.')

            


        
    


