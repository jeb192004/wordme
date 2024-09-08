
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
        #last tile checked
        self.last_tile_checked = None
        #row for player letters direction left or right/col for player letters direction up or down
        self.row_col = None
        #array of tiles played
        self.lettersPlayed = []
        #array to hold word score modifiers
        self.wordScoreModifier = []

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
    
    def play(self, board, alert):
        self.lettersPlayed = []
        isValidPlacement = False
        for item in board.controls:
            index = item.controls[0].data
            if index==112:
                if len(item.controls) < 2:
                    return "no tile played on start position"
            if len(item.controls) > 1 and item.controls[1].group == "available":
                space_value = item.controls[0].content.content.value
                if space_value == "TW" or space_value == "DW":
                    if space_value=="TW":
                        self.wordScoreModifier.append(3)
                    if space_value=="DW":
                        self.wordScoreModifier.append(2)
                #if self.last_tile_checked is not None:
                #isValidPlacement = self.check_valid_placement(board, index)
                tile_data=dict(item.controls[1].data)
                tile_data['index']=index
                self.lettersPlayed.append(tile_data)
                #print(space_value, index)
                #self.last_tile_checked=index

        validArray = self.check_valid_placement(board)
        isValid = validArray[0]
        validText = validArray[1]
        print(isValid, validText)
        if isValid==False:
            alert.alert(validText)
        else:
            alert.alert(validText)
        return self.lettersPlayed
    
    def check_valid_placement(self, board):

        add_tiles=[-15, 15, -1, 1]
        for t in self.lettersPlayed:
            invalidCount=0
            
            if t["index"]==112:
                pass
            else:
                for num in add_tiles:
                    num = t["index"] + num
                    if len(board.controls[num].controls)<2:
                        invalidCount+=1
                if invalidCount==4:
                    return [False, "Invalid word placement"]
            
        return [True, "Valid word placement"]
        