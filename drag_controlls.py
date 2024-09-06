import flet as ft

class DragControlls:
    def __init__(self, page, bd):
        self.page = page
        self.bd = bd


    def drag_will_accept(self, e):
        e.control.content.border = ft.border.all(
            2, ft.colors.GREEN if e.data == "true" else ft.colors.RED
        )
        e.control.update()

    def drag_accept(self, e: ft.DragTargetAcceptEvent):
        src = self.page.get_control(e.src_id)
        tile = src.content.content.value
        tile_row = src.parent.controls
        new_draggable_tile = ft.Draggable(
            group="available",
            content=ft.Container(
                content=ft.Text(tile, color="black"),
                width=30,
                height=30,
                bgcolor=ft.colors.YELLOW,
                alignment=ft.alignment.center,
                margin=ft.Margin(0.5, 0.5, 0.5, 0.5),
                border=ft.Border(
                    left=ft.BorderSide(1, "black"),
                    top=ft.BorderSide(1, "black"),
                    right=ft.BorderSide(1, "black"),
                    bottom=ft.BorderSide(1, "black"),
                ),
            ),
            on_drag_complete=lambda e: self.drag_complete(e),
        )
        index = self.bd.get_index_from_group("available")
        self.bd.update_group(index, "current_play")
        e.control.parent.controls.append(new_draggable_tile)
        e.control.parent.update()
        tile_rowCount = len(tile_row)
        print(tile_rowCount-1, index)
        self.bd.update_board(tile_rowCount-1, index)
        
        

    def drag_leave(self, e):
        e.control.content.border = ft.border.all(
            2, ft.colors.GREEN if e.data == "true" else None
        )
        e.control.update()
    
    def drag_start(self, e):
        print(e.control.content)
        #tile_row = e.control.parent
        #tile_row.controls.remove(e.control)
        #tile_row.update()

    def drag_complete(self, e):
        tile_row = e.control.parent
        tile_row.controls.remove(e.control)
        tile_row.update()