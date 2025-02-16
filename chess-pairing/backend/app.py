from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/pairings")
def get_pairings():
    return jsonify({"round": 1, "pairings": [["Player A", "Player B"]]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)