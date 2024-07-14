from flask import Flask, jsonify, request
from rsnchat import RsnChat
import dotenv
import os


dotenv.load_dotenv()

apiKey = os.environ.get("RSNCHATAPIKEY")

rsnchat = RsnChat(apiKey)

def gpt(content: str) -> dict:
    resp = rsnchat.gpt(content)
    output = resp.get('message', '')

    return output


app = Flask(__name__)

@app.route('/chatGPT', methods=["POST"])
def praseGPT_response():
    responseMSG = ""
    userCONTENT = request.form["chat_content"]
    return gpt(userCONTENT)


if __name__ == "__main__":
    app.run(debug=True, port=80)