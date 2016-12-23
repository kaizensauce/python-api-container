from flask import Flask, jsonify
app = Flask(__name__)

quotes = [
    {
        'id': 1,
        'Assured': u'Halifax'
    },
    {
        'id': 2,
        'Assured': u'BP'
    }
]

@app.route("/quotes")
def get_quotes():
    return jsonify({'quotes': quotes})

if __name__ == "__main__":
    app.run()
