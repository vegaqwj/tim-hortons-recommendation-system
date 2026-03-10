
from flask import Flask, request, jsonify
from serving.recommend import recommend

app = Flask(__name__)

@app.route("/recommend")
def recommend_api():
    user_id = request.args.get("user_id")
    recs = recommend(user_id)
    return jsonify({
        "user_id":user_id,
        "recommendations":[str(r) for r in recs.numpy()]
    })

if __name__ == "__main__":
    app.run(debug=True)
