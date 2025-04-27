import json

class CardImporter():
    def __init__(self, file_path):
        self.file_path = file_path
        self.cards = self.load_cards_from_json(file_path)

    def get_cards(self):
        return self.cards
    
    def load_cards_from_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data['cards']