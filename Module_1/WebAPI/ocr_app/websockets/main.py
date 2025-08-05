import base64
# from loguru import logger
from io import BytesIO

import numpy as np
import uvicorn
from fastapi import FastAPI, WebSocket
from PIL import Image

app = FastAPI()
# hay sử dụng cho các thiết bị cuối do khó scale nên k hay được dùng để giao tiếp giữa 2 thành phần trong server
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive()
        img = Image.open(BytesIO(data["bytes"]))
        np_img = np.array(img)
        # Send the image back to the browser
        await websocket.send({"type": "websocket.send", "bytes": data["bytes"]})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8083)
