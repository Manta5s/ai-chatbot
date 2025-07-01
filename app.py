from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Naudok API raktą iš aplinkos kintamųjų
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "Nėra klausimo"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

# ŠITA DALIS turi būti BLOKE
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)