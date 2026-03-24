from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def generate_advice(income, expenses, age):
    savings = income - expenses
    advice = []

    if savings <= 0:
        advice.append("⚠️ You are overspending! Cut unnecessary expenses.")
    else:
        advice.append("✅ Good savings habit!")

    if age < 30:
        advice.append("📈 Invest aggressively in equity mutual funds.")
    elif age < 50:
        advice.append("⚖️ Maintain balanced portfolio (equity + debt).")
    else:
        advice.append("🛡️ Focus on low-risk investments.")

    if savings > income * 0.4:
        advice.append("🔥 Excellent savings rate! Consider increasing SIP.")

    return advice

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    income = int(data["income"])
    expenses = int(data["expenses"])
    age = int(data["age"])

    savings = income - expenses
    sip = savings * 0.3
    emergency = expenses * 6

    advice = generate_advice(income, expenses, age)

    return jsonify({
        "savings": savings,
        "sip": sip,
        "emergency": emergency,
        "advice": advice
    })

if __name__ == "__main__":
    app.run(debug=True)
