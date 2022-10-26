from flask import Flask, request
import re

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def flask_postcode():
    code = """
            <form action="/" method="POST">
            <label>Wprowadź kod pocztowy: </label>
            <input type="kod_pocztowy" name="postcode" >
            <button type="submit"> Sprawdź </button>
            </form>"""
    try:
        if request.method == "POST":
            n = request.form["postcode"]
            return "KOd poprawny" if re.match(r'^[\d]{2}-[\d]{3}$', n) else "kod niepoprawny"
        else:
            return code
    except (ValueError, TypeError):
        return f"kod niepoprawny"


if __name__ == "__main__":
    app.run(debug=True, port=5030)
