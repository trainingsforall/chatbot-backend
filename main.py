@app.route("/chat", methods=["POST"])
def chat():
    print("📢 /chat endpoint was called")  # ADDED this line outside try block

    try:
        data = request.get_json()
        user_message = data.get("message", "")
        print("📝 Received message:", user_message)

        if not openai.api_key:
            print("🚫 OPENAI_API_KEY is missing!")
            return jsonify({"error": "API key not found."}), 500

        context = """
        Welcome to Strategy Evolve. We offer online training for security professionals,
        AI tools, and business workflow consultancy.
        """

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
