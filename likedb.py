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
            json.dump(self.data, f, indent=4)
    
    def add_like(self):
        self.data['like'] += 1
        self.save(self.data)
        
    
    def add_dislike(self):
        self.data['dislike'] += 1
        self.save(self.data)


            