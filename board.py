import flet as ft
from drag_controlls import DragControlls
import time

class Board:
    
    def __init__(self, page, tiles):
        self.page = page
        self.last_click_time = 0
        self.current_scale = 1
        self.isZoomed = True
        self.tiles = tiles
        self.board_size = 15
        self.space_size = 22*2
        self.zoomed_out_board_size = 0
        self.space_text_size=10
        self.first_letter_position = 0
        self.second_letter_position = 0
        self.third_letter_position = 0
        self.fourth_letter_position = 0
        self.fifth_letter_position = 0
        self.sixth_letter_position = 0
        self.seventh_letter_position = 0
        self.board = ft.GridView(
            expand=1,
            runs_count=self.board_size,
            max_extent=self.space_size,
            child_aspect_ratio=1.0,
            spacing=1,
            run_spacing=1,
            )
        self.board_container=None
        self.dc = DragControlls(self.page, self, self.tiles, self)

    def set_up_board(self): 
        drag_group = "available" 
        start_space = [112]
        tw_space = [0, 7, 14, 105, 119, 210, 217, 224]
        dw_space = [16, 28, 32,42, 48,56, 64, 70, 154, 160, 168, 176, 182, 192, 196,208]
        tl_space = [20, 24, 76, 80, 84, 88, 136, 140, 144, 148, 200, 204]
        dl_space = [3, 11, 36, 38, 45, 52, 59, 92, 96, 98, 101, 108, 115, 122, 126, 128, 131, 165, 172, 179, 186, 188, 213, 221]
        for i in range(self.board_size * self.board_size):
            text_color = "white"
            tile_text = ""
            background_color = ft.colors.BLUE_GREY_100
            if i in tw_space:
                tile_text = "TW"
                background_color = ft.colors.RED_400
            elif i in start_space:
                tile_text = "S"
                background_color = ft.colors.PURPLE_200
            elif i in dw_space:
                tile_text = "DW"
                background_color = ft.colors.ORANGE_500
            elif i in tl_space:
                tile_text = "TL"
                background_color = ft.colors.BLUE_800
            elif i in dl_space:
                tile_text = "DL"
                background_color = ft.colors.BLUE_400
            self.board.controls.append(
                ft.Stack(
                        [ft.DragTarget(
                            group=drag_group,
                            content=ft.Container(
                                content=ft.Text(tile_text, color=text_color, size=self.space_text_size),
                                width=self.space_size,
                                height=self.space_size,
                                bgcolor=background_color,
                                border_radius=5,
                                alignment=ft.alignment.center,
                            ),
                            on_will_accept=self.dc.drag_will_accept,
                            on_accept=lambda e: self.dc.drag_accept(e),
                            on_leave=self.dc.drag_leave,
                            data=i
                        ),
                        
                    ],
                    width=self.space_size,
                    height=self.space_size,
                )
                
            )
        #self.board.width = self.space_size * self.board_size + (self.board_size - 1) * 1  # Grid width based on square size and spacing
        self.zoomed_out_board_size=self.board_size * self.space_size +15
        
        self.board_container = ft.Container(
            content=self.board,
            width=self.zoomed_out_board_size,
            height=self.zoomed_out_board_size,
            border_radius=5,
            on_click=lambda e: self.double_click(),
            scale=ft.transform.Scale(scale=self.current_scale),
            animate_scale=ft.animation.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
        )   
        scrollable_row = ft.Row(
            expand=True,
            controls=[self.board_container],  # Add GridView here
            scroll=ft.ScrollMode.ALWAYS,  # Enable horizontal scrolling
            width=self.zoomed_out_board_size,
            height=self.zoomed_out_board_size,
            )
        scrollable_row_container = ft.Container(
            content=scrollable_row,
            width=self.board_size * (self.space_size / 2) +15,
            height=self.board_size * (self.space_size / 2) +15,
            border_radius=5,
            bgcolor=ft.colors.BLACK
        )
        return [self.board, scrollable_row_container]

    def animate(self, scale):
            if self.isZoomed:
                self.board.max_extent = self.space_size / 2
                self.board.width = self.board_size * (self.space_size / 2) +15
                self.board.height = self.board_size * (self.space_size / 2) +15
                self.board_container.width = self.board_size * (self.space_size / 2) +15
                self.board_container.height = self.board_size * (self.space_size / 2) +15
                self.isZoomed = False
            else:
                self.board.max_extent = self.space_size
                self.board.width = self.zoomed_out_board_size
                self.board.height = self.zoomed_out_board_size
                self.board_container.width = self.zoomed_out_board_size
                self.board_container.height = self.zoomed_out_board_size
                self.isZoomed = True
            gridItemsArray = self.board.controls
            for stack in gridItemsArray:
                if len(stack.controls)==1:
                    #print("drag target only")
                    pass
                elif len(stack.controls)>1:
                    #print("drag target and dragable")
                    pass
            print(self.board.parent)
            self.current_scale = scale
            #self.board_container.scale = scale
            self.page.update()

    def double_click(self):        
        current_time = time.time()
        if current_time - self.last_click_time < 0.5:
            if self.current_scale == 1:
                self.animate(0)
            else:
                self.animate(1)
        self.last_click_time = current_time

    def check_pos_available(self, board, index):
        space = board.controls[index]
        print(space.controls[0].group)
        if len(space.controls) > 1:
            return False
        else:
            return True
        

    