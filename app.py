from flask import Flask
from flask import jsonify
from flask import request
import pickle
from googletrans import Translator

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
translator = Translator()


@app.route("/")
def index():
    return "Welcome to CSE495 API"


@app.route("/api/v1/getResult")
def getresult():
    request_data = request.get_json()
    comment = request_data['comment']
    #print(comment)
    com_en = translator.translate(comment, dest="en").text
    com_en = [com_en]
    result = model.predict(com_en)

    #print(result)
    #print(com_en)

    return jsonify({'result': result[0]})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
