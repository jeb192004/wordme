import flet as ft
from tiles import Tiles

class DragControlls:
    def __init__(self, page, board, tiles):
        self.page = page
        self.board = board
        self.tiles = tiles
        self.available_spaces = []


    def drag_will_accept(self, e):
        '''e.control.content.border = ft.border.all(
            2, ft.colors.GREEN if e.data == "true" else ft.colors.RED
        )
        e.control.update()'''

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
        print(f"source tile group: {src.group}")
            
        if index in self.available_spaces:
            new_draggable_tile = ft.Draggable(
                group="available",
                content=ft.Container(
                    content=ft.Text(tile, color="black"),
                    width=30,
                    height=30,
                    bgcolor=ft.colors.YELLOW,
                    alignment=ft.alignment.center,
                    margin=ft.Margin(0.5, 0.5, 0.5, 0.5),
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
            )
            #index = self.bd.get_index_from_group("available")
            #update group from available to current_play
            #self.bd.update_group(index, "current_play")
            #board.controls[index].controls[0].group = "current_placed"
            e.control.parent.controls.append(new_draggable_tile)
            e.control.parent.update()
            #tile_rowCount = len(tile_row)
            #print(e.control.parent.controls, board.controls[index].controls[0].group)
            #self.available_spaces = self.tiles.get_available_spaces(board)
            #print(self.available_spaces, index)
            #self.bd.update_board(tile_rowCount-1, index)
            
            #remove tile from player set of tiles
            tile_row.remove(src)
            #update the players set of tiles
            src.parent.update()
        
        

    def drag_leave(self, e):
        '''e.control.content.border = None
        e.control.update()'''
        
    
    def drag_start(self, e):
        #print(e.control)
        
            #print(e.control)
        #print(e.control)
        #tile_row = e.control.parent
        #tile_row.controls.remove(e.control)
        #tile_row.update()
        pass

    def drag_complete(self, e):
        #tile_row = e.control.parent
        #tile_row.controls.remove(e.control)
        #tile_row.update()
        pass