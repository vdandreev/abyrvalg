import field
import uuid
import pickle

class Game():

    def __init__(self, players = ["kate", "tom"]):
        self.session = {}
        
        self.session["id"] = str(uuid.uuid4().__repr__())

        for player in players:
          self.session[player] = {}
          self.session[player]["name"] = player
          self.session[player]["field"] = field.Field()

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


    def save_game(self,file_path) :
        """
        This should save game to file as an object, so the following would be possible
        new_game = Game(["vasya", "pupkin"])
        new_game.save_game("/path/to/file")

        """


        pickle.dump(self.session,open(file_path,'wb'))




    def load_game(self, file_path):
        """
        This should load a game from file, so something following possible:
        old_game = Game()
        old_game.load_game("/path/to/file")
        you can check correctness by checking players and their tokens
        """

        self.session = pickle.load(open(file_path,'rb'))



new_game = Game(['kate','tom'])
new_game.save_game('home\goods')
old_game = Game()
old_game.load_game('home\goods')
