from flask import Flask, render_template, request, jsonify
from youtube_ByChat import create_db_from_youtube_url, get_response_from_query

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    video_url = data.get("video_url")
    question = data.get("question")

    if not video_url or not question:
        return jsonify({"error": "Missing input"}), 400

    try:
        db = create_db_from_youtube_url(video_url)
        response, _ = get_response_from_query(db, question)
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
