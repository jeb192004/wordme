import flet as ft
from tiles import Tiles
from drag_controlls import DragControlls

class Player:
    def __init__(self, page, dc):
        self.page = page
        
        self.player_names = ["Player 1","|", "Player 2"]
        self.dc = dc
    
    def set_up_player_names(self):
        # Create player name row
        player_name_row = ft.Row(
            controls=[ft.Text(player_name, color="black") for player_name in self.player_names],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        player_name_container=ft.Container(
            content=player_name_row,
            margin=ft.Margin(5, 5, 5, 5),
        )
        return player_name_container
    
    def set_up_player(self):
        # Player letter tiles
        player_tiles = list(Tiles().pick_seven_letters())
    
        # Create draggable tiles for the player
        tile_row = ft.Row(
            controls=[
                ft.Stack([
                    Tiles().player_drag_target(self.dc),
                    Tiles().player_tile(tile, 1, self.dc)
                ])
                for tile in player_tiles
            ],
            spacing=2,
            alignment=ft.MainAxisAlignment.CENTER,
        )
        player_row_stack = ft.Stack([
            ft.Row(controls=[
                    ft.Container(bgcolor=ft.colors.BLUE_ACCENT_400, expand=False, height=10, width=45*7+20),
                    
                ],alignment=ft.MainAxisAlignment.CENTER,),
                ft.Container(content=tile_row,
                             margin=ft.Margin(0, 0, 0, 5))
        ],alignment=ft.alignment.bottom_center,)
        return {
            "tile_row": player_row_stack,
            "draggable_tiles": [{'tile': tile, 'item': item} for tile, item in zip(player_tiles, tile_row.controls)]
        }