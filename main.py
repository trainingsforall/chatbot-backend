
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)

# Load OpenAI API key from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        print("📝 Received message:", user_message)

        # DEBUG: Check if API key is present
        if not openai.api_key:
            print("🚫 OPENAI_API_KEY is missing!")
            return jsonify({"error": "API key not found."}), 500

        # Bot context
        context = """
        Welcome to Strategy Evolve. We offer online training for security professionals,
        AI tools, and business workflow consultancy.
        """

        # Generate response using OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. Use this context: {context}"},
                {"role": "user", "content": user_message}
            ]
        )

        print("✅ OpenAI response:", response)

        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        print("❌ ERROR in /chat route:", e)
        return jsonify({"error": str(e)}), 500

# Run Flask server
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=10000)
