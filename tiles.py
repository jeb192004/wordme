
import random

tiles_placed=[]
class Tiles:
    def __init__(self):
        self.tiles = ["A", "A", "A", "A", "A", "A", "A", "A", "A",
                      "B", "B",
                      "C", "C", "C", "C",
                      "D", "D", "D", "D",
                      "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E",
                      "F", "F",
                      "G", "G", "G",
                      "H", "H",
                      "I", "I", "I", "I", "I", "I", "I", "I", "I",
                      "J",
                      "K",
                      "L", "L", "L", "L",
                      "M", "M",
                      "N", "N", "N", "N", "N", "N",
                      "O", "O", "O", "O", "O", "O", "O", "O",
                      "P", "P",
                      "Q",
                      "R", "R", "R", "R", "R", "R",
                      "S", "S", "S", "S",
                      "T", "T", "T", "T", "T", "T", "T",
                      "U", "U", "U", "U",
                      "V", "V",
                      "W", "W",
                      "X",
                      "Y", "Y",
                      "Z"
                      " ", " "]
        self.tile_bag = []
        self.player_tiles = []

    def pick_seven_letters(self):
        self.player_tiles
        self.tile_bag
        player_tiles = random.sample(self.tiles, 7)
        tile_bag = self.tiles[:-7]
        #print(player_tiles)
        #print(tile_bag)
        return player_tiles

    def set_up_tile_list(self):
        pass
       
    def tiles_placed(self):
        if len(tiles_placed) == 0:
            return False

    def check_pos_available(self, board, index):
        space = board.controls[index]
        print(space.controls[0].group)
        if len(space.controls) > 1:
            return False
        else:
            return True

    def get_available_spaces(self, board):
        available_spaces = []
        for index, space in enumerate(board.controls):
            if space.controls[0].group == "available":
                available_spaces.append(index)
        return available_spaces