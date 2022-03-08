import tcod
from typing import Tuple
from constants.screen import MAP_W, MAP_H


class GameMap(tcod.map.Map):
    """Map class."""

    def __init__(self, width: int, height: int, id: str, name: str):
        super().__init__(width, height, 'F')
        self.__name = name
        self.__id = id
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def id(self) -> str:
        return self.__id
    
    def cam(self, center: Tuple[int, int]) -> Tuple[int, int]:
        cx, cy = center
        def calc(p: int, m: int, s: int):
            return sorted([p - s//2, 0, m-s])[1]
        
        left = calc(cx, self.width, MAP_W)
        top = calc(cy, self.height, MAP_H)

        return left, top
    
    def to_screen_coords(
        self, map_coord: Tuple[int, int], center: Tuple[int, int]
    ) -> Tuple[int, int]:
        mx, my = map_coord
        cx, cy = self.cam(center)
        return mx-cx, my-cy
    
    def from_screen_coords(
        self, screen_coord: Tuple[int, int], center: Tuple[int, int]
    ) -> Tuple[int, int]:
        sx, sy = screen_coord
        cx, cy = self.cam(center)
        return sx+cx, sy+cy

    

        