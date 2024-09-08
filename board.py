import flet as ft
from drag_controlls import DragControlls

class Board:
    
    def __init__(self, page, tiles):
        self.page = page
        self.tiles = tiles
        self.board_size = 15
        self.space_size = 25
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

        self.dc = DragControlls(self.page, self, self.tiles)

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
        # Ensure the grid stays at the correct aspect ratio and doesn't stretch
        self.board.width = self.space_size * self.board_size + (self.board_size - 1) * 1  # Grid width based on square size and spacing
        whole_board_size=self.board_size * self.space_size +15
        scrollable_row = ft.Row(
            controls=[self.board],  # Add GridView here
            scroll=ft.ScrollMode.HIDDEN,  # Enable horizontal scrolling
            width=whole_board_size,
            height=whole_board_size,  # Adjust height to fit your content
    )
        return [self.board, scrollable_row]

    def get_board_index(self, board, index):
        #row = x
        #col = y
        #index = row * self.board_size + col
        return board.controls[index]
    
    def check_pos_available(self, board, index):
        space = board.controls[index]
        print(space.controls[0].group)
        if len(space.controls) > 1:
            return False
        else:
            return True
        
    def update_group(self, index, group):
        isAvailable = self.check_pos_available(self.board, index)
        if isAvailable:
            space = self.get_board_index(self.board, index)
            #print(space.controls[0])
            space.controls[0].group = group
            #print(space.controls[0].group)
            space.update()
        else:
            pass
        
    