class Team:
    def __init__(self,name,players,coach):

        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

        
    def add_player(self, player):
            
            self.players.append(player)

    def has_player(self, player):
        return player in self.players
        # if player in self.players:
        #       return True
        # return False 
    
    # return player in self.players
    
    def play_game(self, result_win):
         if result_win:
              self.points += 3
         
    