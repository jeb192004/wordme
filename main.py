import flet as ft
from board import Board
from player import Player
from tiles import Tiles
from drag_controlls import DragControlls
from alert import Alert


def main(page: ft.Page):
    page.title = "WordMe"
    page.bgcolor="white"
    #page.platform = ft.PagePlatform.ANDROID
    if page.platform == ft.PagePlatform.LINUX or page.platform == ft.PagePlatform.MACOS or page.platform == ft.PagePlatform.WINDOWS:
        page.window.width = 420
        page.window.min_width = 420
        page.window.padding = 0
        page.window.margin = 0

    alert=Alert(page)
    
    tiles = Tiles()
    bd = Board(page, tiles)
    boardArray = bd.set_up_board()
    board = boardArray[0]
    boardRow = boardArray[1]
    dc = DragControlls(page, board, tiles)
    p = Player(page, dc)
    

    draggable_tiles = {}
    
    player_name_row = p.set_up_player_names()
    player = p.set_up_player()
    draggable_tiles = player["draggable_tiles"]
    tile_row = player["tile_row"]
    #print(draggable_tiles)

    
    #isStartPosAvail = bd.check_pos_available(board)
    
    def play_click(e):
        wordsPlayed = tiles.play(board, alert)
        print(wordsPlayed)

    #print(isStartPosAvail)
    
    # Layout all components in a column
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.PLAY_ARROW_ROUNDED, on_click=play_click,)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_DOCKED

    page.appbar = ft.AppBar(
        title=player_name_row, 
        center_title=True,
        bgcolor=ft.colors.LIGHT_BLUE_ACCENT,
        automatically_imply_leading=False,
    )
    page.bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.colors.LIGHT_BLUE_ACCENT,
            shape=ft.NotchShape.AUTO,
            height=64,
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.KEYBOARD_DOUBLE_ARROW_RIGHT_ROUNDED, icon_color=ft.colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SWAP_VERT_ROUNDED, icon_color=ft.colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SHUFFLE_ROUNDED, icon_color=ft.colors.WHITE),
                ]
            ),
        )
    
    page.add(
        ft.Column(
            controls=[
                
                boardRow,
                tile_row,
                
                
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    
    
    #bd.update_group(112, "available")

# Run the app
ft.app(target=main)
