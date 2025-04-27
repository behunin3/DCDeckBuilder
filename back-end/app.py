# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from frontend

# Mocked game state
game_state = {
    "players": ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"],
    "market_cards": ["Kick", "Punch", "Super Speed", "Vulnerability", "Power Ring"],
    "your_hand": ["Draw Two", "Punch", "Kick"]
}

@app.route("/game-state", methods=["GET"])
def get_game_state():
    return jsonify(game_state)

@app.route("/play-card", methods=["POST"])
def play_card():
    data = request.get_json()
    card_name = data.get('cardName')

    # Remove the card from hand if it exists
    if card_name in game_state["your_hand"]:
        game_state["your_hand"].remove(card_name)
        print(f"Played card: {card_name}")
        return jsonify({"success": True, "message": f"Played {card_name}."})
    else:
        return jsonify({"success": False, "message": "Card not found in hand."}), 400

if __name__ == "__main__":
    app.run(port=5000, debug=True)
