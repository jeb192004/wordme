import flet as ft
from tiles import Tiles
from drag_controlls import DragControlls

class Player:
    def __init__(self, page, bd):
        self.page = page
        self.bd = bd
        self.player_names = ["Player 1", "Player 2"]
        self.tiles = Tiles()
        self.dc = DragControlls(self.page, self.bd)
    
    def set_up_player_names(self):
        # Create player name row
        player_name_row = ft.Row(
            controls=[ft.Text(player_name, color="black") for player_name in self.player_names],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        return player_name_row
    
    def set_up_player(self):
        # Player letter tiles
        player_tiles = list(Tiles().pick_seven_letters())
    
        # Create draggable tiles for the player
        tile_row = ft.Row(
            controls=[
                ft.Draggable(
                    group="available",
                    content=ft.Container(
                        content=ft.Text(tile, color="black"),
                        width=30,
                        height=30,
                        bgcolor=ft.colors.YELLOW,
                        alignment=ft.alignment.center,
                        margin=ft.Margin(.5, .5, .5, .5),
                        border=ft.Border(
                            left=ft.BorderSide(1, "black"),
                            top=ft.BorderSide(1, "black"),
                            right=ft.BorderSide(1, "black"),
                            bottom=ft.BorderSide(1, "black"),
                        ),
                    ),
                    #on_drag_start=lambda e: self.dc.drag_start(e),
                    on_drag_complete=lambda e: self.dc.drag_complete(e),                    
                )
                for tile in player_tiles
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        return {
            "tile_row": tile_row,
            "draggable_tiles": [{'tile': tile, 'item': item} for tile, item in zip(player_tiles, tile_row.controls)]
        }