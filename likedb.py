import json

class LikeDB:
    def __init__(self, path):
        self.path = path # "data.json"
        
        try:
            with open(path, 'r') as f:
                self.data = json.load(f)
        except:
            self.data = {
                "like": 0,
                "dislike": 0
            }
    
    def save(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)
    
    def add_like(self, chat_id):
        pass
        
    
    def add_dislike(self, chat_id):
        pass
    
    def get_likes(self, chat_id) -> int:
        pass

    def get_dislikes(self, chat_id) -> int:
        pass



            