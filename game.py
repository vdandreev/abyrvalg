import field
import uuid
import pickle

class Game():

    def __init__(self):
        self.session = {}
        
        self.session["id"] = str(uuid.uuid4().__repr__())

        #for player in players:
        #  self.session[player] = {}
        #  self.session[player]["name"] = player
        #  self.session[player]["field"] = field.Field()

    def join_game(self, player_name):
        """
        This should enable a player to join game. It should create an entry for
        the new player in session dict, alongside with field and id.
        It should check how many players already joined and do not allow to join
        more than 2 players.
        It should return plaer token and game token.
        """
        pass

    def get_session_id(self):
        return self.session["id"]

    def get_player_token(self, player_name):
        try:
            return self.session[player_name]["token"]
        except:
            return False

    def player_field_state(self, player_name, token):
        try:
            if self.session[player_name].has_key(token):
                return self.session[player_name]["field"]
        except:
            return False


    def save_game(self) :
        """
        This should save game to a file, which name derived from game id

        """
        pickle.dump(self.session,open(file_path,'wb'))




    def load_game(self, game_id):
        """
        It should load game from previously saved one
        """

        self.session = pickle.load(open(file_path,'rb'))



new_game = Game(['kate','tom'])
new_game.save_game('home\goods')
old_game = Game()
old_game.load_game('home\goods')
