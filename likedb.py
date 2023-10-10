import json

class LikeDB:
    def __init__(self, path):
        self.path = path # "data.json"
        
        try:
            with open(path, 'r') as f:
                self.data = json.load(f)
        except:
            self.data = {}
    
    def save(self, data):
        with open(self.path, 'w') as f:
            json.dump(data, f, indent=4)
    
    def add_user(self, chat_id):
        chat_id = str(chat_id)

        
        if chat_id not in self.data:
            self.data[chat_id] = {
                "like": 0,
                "dislike": 0
            }
            self.save(self.data)

    def add_like(self, chat_id):
        self.data[str(chat_id)]['like'] += 1
        self.save(self.data)
        
    
    def add_dislike(self, chat_id):
        self.data[str(chat_id)]['dislike'] += 1
        self.save(self.data)
    
    def get_likes(self, chat_id) -> int:
        return self.data[str(chat_id)]['like']

    def get_dislikes(self, chat_id) -> int:
        return self.data[str(chat_id)]['dislike']



            