import flet as ft
from board import Board
from player import Player


def main(page: ft.Page):
    page.title = "WordMe"
    page.bgcolor="white"
    #page.window.width = 420
    #page.window.min_width = 420

    bd = Board(page)
    p = Player(page, bd)

    draggable_tiles = {}
    
    player_name_row = p.set_up_player_names()
    player = p.set_up_player()
    draggable_tiles = player["draggable_tiles"]
    tile_row = player["tile_row"]
    #print(draggable_tiles)

    board = bd.set_up_board()
    isStartPosAvail = bd.check_pos_available(board)
    
    #print(isStartPosAvail)
                
    # Layout all components in a column
    page.add(
        ft.Column(
            controls=[
                player_name_row,
                board,
                tile_row,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    bd.update_group(112, "available")

# Run the app
ft.app(target=main)
