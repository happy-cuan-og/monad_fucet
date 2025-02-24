from flask import Flask, request, jsonify
import requests,json,secrets
from fake_useragent import FakeUserAgent
from flask_cors import CORS
from eth_account import Account

app = Flask(__name__)
CORS(app)


@app.route("/submit", methods=["POST"])
def verify_recaptcha():
    data = request.json
    recaptcha_token = data.get("recaptcha_token")
    try:

        ua = FakeUserAgent()

        akun = Account.create()

        headers = {
            'User-Agent': ua.random,
            'Content-Type': "application/json",
            'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            'origin': "https://testnet.monad.xyz",
            'priority': "u=1, i",
            'referer': "https://testnet.monad.xyz/",
        }
        #Setting your proxy here exemple (http://user:pass@ip:port)
        proxies = {
            "http": "http://",
            "https": "http://"
        }
        payload = {
            "address": akun.address,
            "visitorId": secrets.token_hex(16),
            "recaptchaToken": recaptcha_token
        }

        response = requests.post("https://testnet.monad.xyz/api/claim",json=payload,headers=headers,proxies=proxies)


        if response.status_code == 200:
            result = response.json()
            print(f"Success: {result}")
            with open("pk.txt", "a") as f:
                f.write(f"{akun.key.hex()}\n")
            return jsonify('success')
        else:
            return jsonify(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.SSLError as e:
        return jsonify(f"SSLError encountered: {e}")
    except Exception as e:
        return jsonify(f"Unexpected error: {e}")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
