import flet as ft
from tiles import Tiles

class DragControlls:
    def __init__(self, page, board, tiles, bd):
        self.page = page
        self.board = board
        self.tiles = tiles
        self.available_spaces = []
        self.bd=bd


    def drag_will_accept(self, e):
        '''e.control.content.border = ft.border.all(
            2, ft.colors.GREEN if e.data == "true" else ft.colors.RED
        )
        e.control.update()'''
        pass

    def drag_accept(self, e: ft.DragTargetAcceptEvent):
        #index of space tile is dropped onto
        index = e.control.data
        board= e.control.parent.parent
        self.available_spaces = self.tiles.get_available_spaces(board)
        #the tile picked up from player set of tiles
        src = self.page.get_control(e.src_id)
        #the tile value ex. "F"
        tile = src.content.content.value
        #the players set of tiles
        tile_row = src.parent.controls
        print(f"source tile group: {e.control.parent.parent}")
        draggable_tile_size = 30
        draggable_tile__text_size =10
        if "row" in str(e.control.parent.parent):
            draggable_tile_size = 45
            draggable_tile__text_size = 20
        else:
            self.bd.animate(2)
        #if index in self.available_spaces:
        new_draggable_tile = ft.Draggable(
                group="available",
                content=ft.Container(
                    content=ft.Text(tile, color="black", size=draggable_tile__text_size),
                    width=draggable_tile_size,
                    height=draggable_tile_size,
                    bgcolor=ft.colors.YELLOW,
                    alignment=ft.alignment.center,
                    #margin=ft.Margin(0.5, 0.5, 0.5, 0.5),
                    border_radius=5,
                    border=ft.Border(
                        left=ft.BorderSide(1, "black"),
                        top=ft.BorderSide(1, "black"),
                        right=ft.BorderSide(1, "black"),
                        bottom=ft.BorderSide(1, "black"),
                    ),
                ),
                on_drag_start=lambda e: self.drag_start(e),
                on_drag_complete=lambda e: self.drag_complete(e),
                data=src.data
            )
        e.control.parent.controls.append(new_draggable_tile)
        e.control.parent.update()
            
            #remove tile from player set of tiles
        tile_row.remove(src)
            #update the players set of tiles
        src.parent.update()
        
        

    def drag_leave(self, e):
        '''e.control.content.border = None
        e.control.update()'''
        pass
        
    
    def drag_start(self, e):
        #print(e.control)
        
            #print(e.control)
        #print(e.control)
        #tile_row = e.control.parent
        #tile_row.controls.remove(e.control)
        #tile_row.update()
        pass

    def drag_complete(self, e):
        #print(e)
        #tile_row = e.control.parent
        #tile_row.controls.remove(e.control)
        #tile_row.update()
        pass