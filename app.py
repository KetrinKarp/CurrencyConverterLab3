from flask import Flask, request, jsonify
from currency_converter.exchange import get_exchange_rate, convert_amount, get_supported_currencies

app = Flask(__name__)

@app.route('/get_exchange_rate', methods=['GET'])
def get_rate():
    base_currency = request.args.get('baseCurrency')
    target_currency = request.args.get('targetCurrency')

    if not base_currency or not target_currency:
        return jsonify({"error": "Please provide baseCurrency and targetCurrency"}), 400

    try:
        rate = get_exchange_rate(base_currency, target_currency)
        return jsonify({"baseCurrency": base_currency, "targetCurrency": target_currency, "rate": rate})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/convert_amount', methods=['GET'])
def convert():
    base_currency = request.args.get('baseCurrency')
    target_currency = request.args.get('targetCurrency')
    amount = request.args.get('amount', type=float)

    if not base_currency or not target_currency or not amount:
        return jsonify({"error": "Please provide baseCurrency, targetCurrency, and amount"}), 400

    try:
        converted_amount = convert_amount(base_currency, target_currency, amount)
        return jsonify({"baseCurrency": base_currency, "targetCurrency": target_currency, "amount": amount, "convertedAmount": converted_amount})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_supported_currencies', methods=['GET'])
def get_currencies():
    try:
        currencies = get_supported_currencies()
        return jsonify({"supportedCurrencies": currencies})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
