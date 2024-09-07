import flet as ft
from board import Board
from player import Player
from tiles import Tiles
from drag_controlls import DragControlls


def main(page: ft.Page):
    page.title = "WordMe"
    page.bgcolor="white"
    #page.platform = ft.PagePlatform.ANDROID
    if page.platform == ft.PagePlatform.LINUX or page.platform == ft.PagePlatform.MACOS or page.platform == ft.PagePlatform.WINDOWS:
        page.window.width = 420
        page.window.min_width = 420


    tiles = Tiles()
    bd = Board(page, tiles)
    board = bd.set_up_board()
    dc = DragControlls(page, board, tiles)
    p = Player(page, dc)
    

    draggable_tiles = {}
    
    player_name_row = p.set_up_player_names()
    player = p.set_up_player()
    draggable_tiles = player["draggable_tiles"]
    tile_row = player["tile_row"]
    #print(draggable_tiles)

    bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.colors.LIGHT_BLUE_ACCENT,
            shape=ft.NotchShape.CIRCULAR,
            height=64,
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
                ]
            ),
        )
    #isStartPosAvail = bd.check_pos_available(board)
    def open_pagelet_end_drawer(e):
        pagelet.end_drawer.open = True
        pagelet.end_drawer.update()
    #print(isStartPosAvail)
    pagelet = ft.Pagelet(appbar=ft.AppBar(
            title=ft.Text(page.title), bgcolor=ft.colors.LIGHT_BLUE_ACCENT
        ),
        content=ft.Container(
            content=ft.Column(
                controls=[
                    player_name_row,
                    board,
                    tile_row,
                    ft.Row(controls=[
                        ft.Container(bgcolor=ft.colors.TRANSPARENT, expand=True, height=30),
                    ]),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ),bottom_app_bar=bottom_appbar
        ,end_drawer=ft.NavigationDrawer(
            controls=[
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.icons.ADD_COMMENT, label="Item 2"
                ),
            ],
        ),
        floating_action_button=ft.FloatingActionButton(icon=ft.icons.PLAY_ARROW_ROUNDED, on_click=open_pagelet_end_drawer, ),
        floating_action_button_location=ft.FloatingActionButtonLocation.CENTER_DOCKED,
        )
    # Layout all components in a column
    '''page.add(
        ft.Column(
            controls=[
                player_name_row,
                board,
                tile_row,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )'''
    page.add(pagelet)
    if page.platform == ft.PagePlatform.LINUX or page.platform == ft.PagePlatform.MACOS or page.platform == ft.PagePlatform.WINDOWS:
        pagelet.height=page.window.height
        pagelet.update()

    bd.update_group(112, "available")

# Run the app
ft.app(target=main)
