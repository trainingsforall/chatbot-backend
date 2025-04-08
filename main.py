@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

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

        # 🐞 Log the full OpenAI response
        print("🔁 OpenAI raw response:", response)

        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)}), 500
