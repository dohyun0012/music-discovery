from flask import Flask, jsonify, request, render_template

# Initialize the app
app = Flask(__name__)

# Get an example and return it's score from the predictor model
@app.route("/", methods=["GET", "POST"])
def run():
#     # """
#     # When A POST request with json data is made to this uri,
#     # Read the example from the json, predict probability and
#     # send it with a response
#     # """
#
#     image_path = request.form.get("image_path", "")
#     if image_path:
#         results = [get_image_score(image_path)]
#     else:
#         results = [[]]
    return render_template("index.html")

# Start the app server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
