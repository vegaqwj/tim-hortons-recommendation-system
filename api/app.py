
from flask import Flask, request, jsonify
from serving.recommendation_service import recommend

app = Flask(__name__)

@app.route("/recommend")
def rec():

    user_id = int(request.args.get("user_id",1))
    k = int(request.args.get("top_k",5))

    return jsonify({
        "user_id":user_id,
        "recommendations":recommend(user_id,k)
    })

if __name__ == "__main__":
    app.run(debug=True)
