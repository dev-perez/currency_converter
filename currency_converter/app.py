from flask import Flask, jsonify
import requests


app = Flask(__name__)

response = requests.get(
    "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL"
)

if response.status_code == 200:
    dict_data = response.json()
else:
    dict_data = {}


@app.route("/")
def index():
    return """Use the following routes to access the values: \n
    /dollar_real/, /euro_real/, /bit_real/, /eth_real/"""


@app.route("/dollar_real/")
def dollar_real():
    conversion_data = dict_data.get("USDBRL", {})

    if conversion_data:
        ask_rate = float(conversion_data.get("ask", 0))
        conversion_result = f"From Dollar to Real: {ask_rate:.2f}"
    else:
        conversion_result = "Value not found"

    return jsonify({"conversion_result": conversion_result})


@app.route("/euro_real/")
def euro_real():
    conversion_data = dict_data.get("EURBRL", {})

    if conversion_data:
        ask_rate = float(conversion_data.get("ask", 0))
        conversion_result = f"From Euro to Real: {ask_rate:.2f}"
    else:
        conversion_result = "Value not found"

    return jsonify({"conversion_result": conversion_result})


@app.route("/bit_real/")
def bit_real():
    conversion_data = dict_data.get("BTCBRL", {})

    if conversion_data:
        ask_rate = float(conversion_data.get("ask", 0))
        conversion_result = f"From Bitcoin to Real: {ask_rate:.2f}"
    else:
        conversion_result = "Value not found"

    return jsonify({"conversion_result": conversion_result})


@app.route("/eth_real/")
def eth_real():
    conversion_data = dict_data.get("ETHBRL", {})

    if conversion_data:
        ask_rate = float(conversion_data.get("ask", 0))
        conversion_result = f"From Ethereum to Real: {ask_rate:.2f}"
    else:
        conversion_result = "Value not found"

    return jsonify({"conversion_result": conversion_result})


if __name__ == "__main__":
    app.run(debug=True)
