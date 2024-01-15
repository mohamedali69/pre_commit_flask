from backend import create_app

app = create_app()


@app.route("/health", methods=["GET"])
def helth_check():
    return "OK", 200


@app.route("/users", methods=["GET"])
def get_all_users():
    all_users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Jane"},
    ]
    return {"users": all_users}, 200


if __name__ == "__main__":
    app.run(debug=True)
