from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Substitua pelo seu token da Supercell (Bearer Token)
SUPERCELL_API_TOKEN = os.getenv("SUPERCELL_API_TOKEN", "Bearer SEU_TOKEN_AQUI")

# Endpoints base da API oficial da Supercell
BASE_URL = "https://api.clashofclans.com/v1"

@app.route("/players/<player_tag>/verifytoken", methods=["POST"])
def verify_token(player_tag):
    """Valida se o token informado pertence ao jogador."""
    player_tag = player_tag.replace("#", "%23")
    body = request.get_json()
    token = body.get("token")

    headers = {"Authorization": SUPERCELL_API_TOKEN, "Content-Type": "application/json"}
    url = f"{BASE_URL}/players/{player_tag}/verifytoken"

    response = requests.post(url, headers=headers, json={"token": token})
    return jsonify(response.json()), response.status_code


@app.route("/players/<player_tag>", methods=["GET"])
def get_player(player_tag):
    """Retorna dados completos do jogador."""
    player_tag = player_tag.replace("#", "%23")
    headers = {"Authorization": SUPERCELL_API_TOKEN}
    url = f"{BASE_URL}/players/{player_tag}"

    response = requests.get(url, headers=headers)
    return jsonify(response.json()), response.status_code


@app.route("/clans/<clan_tag>", methods=["GET"])
def get_clan(clan_tag):
    """Retorna dados completos do clã."""
    clan_tag = clan_tag.replace("#", "%23")
    headers = {"Authorization": SUPERCELL_API_TOKEN}
    url = f"{BASE_URL}/clans/{clan_tag}"

    response = requests.get(url, headers=headers)
    return jsonify(response.json()), response.status_code


@app.route("/", methods=["GET"])
def home():
    """Endpoint simples de teste."""
    return jsonify({"message": "Proxy da Clash API ativo com IP fixo"}), 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
