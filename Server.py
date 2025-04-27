from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/game-state", methods=["GET"])
def get_game_state():
    return jsonify({
        "players": ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"],
        "market_cards": ["Card A", "Card B", "Card C", "Card D", "Card E"],
        "your_hand": ["Draw Two", "Punch", "Kick"],
        # ... other game state pieces
    })

@app.route("/play-card", methods=["POST"])
def play_card():
    data = request.get_json()
    card_name = data.get('cardName')
    print(f"Playing card: {card_name}")
    # Process the card play...
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)
