from flask import Flask, request, jsonify
from sympy import sympify, latex

app = Flask(__name__)

@app.route("/text2latex", methods=["POST"])
def convert_text_to_latex():
    try:
        data = request.get_json()
        expr_text = data.get("text", "")
        expr_sympy = sympify(expr_text)
        latex_output = latex(expr_sympy)
        return jsonify({"latex": latex_output})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
