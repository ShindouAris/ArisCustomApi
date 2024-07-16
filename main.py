from flask import Flask, request
import dotenv
import os
import aiohttp

base_url = "https://api.rnilaweera.lk/api/v1/user/"

dotenv.load_dotenv()

apiKey = os.environ.get("RSNCHATAPIKEY")

async def gemini(content: str):
    async with aiohttp.ClientSession()as clss:
        url = f"{base_url}/bard"
        headers = {"Authorization": f"Bearer {apiKey}"}

        payload = {"prompt": content}

        resp = await clss.request("POST", url=url, headers=headers, json=payload)
        jsonResp = await resp.json()
        return jsonResp["message"]

async def gpt(content: str):
    async with aiohttp.ClientSession()as clss:
        url = f"{base_url}/gpt"
        headers = {"Authorization": f"Bearer {apiKey}"}

        payload = {"prompt": content}

        resp = await clss.request("POST", url=url, headers=headers, json=payload)
        jsonResp = await resp.json()

        return jsonResp["message"]

app = Flask(__name__)

@app.route('/api/chatGPT', methods=["POST"])
async def praseGPT_response():
    responseMSG = ""
    userCONTENT = request.form["chat_content"]
    return await gpt(f"{userCONTENT}")

@app.route('/api/gemini', methods=["POST"])
async def praseGemini_response():
    responseMSG = ""
    userCONTENT = request.form["chat_content"]
    return await gemini(f"{userCONTENT} ")


if __name__ == "__main__":
    app.run(debug=True, port=80)