from io import BytesIO

import easyocr
import imagehash
import numpy as np
from fastapi import FastAPI, File, UploadFile
from loguru import logger
from PIL import Image

# Save all files and result to cached
# by a dictionary with key is image hash
# Không nên dùng do cache được khai báo trong process mà async chạy trên các thread dẫn đến
# có thể gấy ra lỗi khi nhiều thread cùng truy cập gọi là race condition
cache = {}

app = FastAPI(root_path="/")


@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    reader = easyocr.Reader(
        ["vi", "en"],
        gpu=True,
        detect_network="craft",
        model_storage_directory="./my_model",
        download_enabled=False,
    )
    # Read image from route
    request_object_content = await file.read()
    pil_image = Image.open(BytesIO(request_object_content))
    logger.info("pil_image")
    logger.info(pil_image)

    # Get the detection from EasyOCR
    detection = reader.readtext(pil_image)

    # Create the final result
    result = {"bboxes": [], "texts": [], "probs": []}
    for bbox, text, prob in detection:
        # Convert a list of NumPy int elements to premitive numbers
        bbox = np.array(bbox).tolist()
        result["bboxes"].append(bbox)
        result["texts"].append(text)
        result["probs"].append(prob)

    return result


@app.post("/cached_ocr")
async def ocr(file: UploadFile = File(...)):
    reader = easyocr.Reader(
        ["vi", "en"],
        gpu=False,
        detect_network="craft",
        model_storage_directory="/app/my_model",
        download_enabled=True,
    )
    # Read image from route
    request_object_content = await file.read()
    pil_image = Image.open(BytesIO(request_object_content))
    pil_hash = imagehash.average_hash(pil_image)
    logger.info(pil_hash)

    if pil_hash in cache:
        logger.info("Getting result from cache!")
        return cache[pil_hash]
    else:
        logger.info("Predicting. Please wait...")
        # Get the detection from EasyOCR
        detection = reader.readtext(pil_image)

        # Create the final result
        result = {"bboxes": [], "texts": [], "probs": []}
        for bbox, text, prob in detection:
            # Convert a list of NumPy int elements to premitive numbers
            bbox = np.array(bbox).tolist()
            result["bboxes"].append(bbox)
            result["texts"].append(text)
            result["probs"].append(prob)

        # Save the result to cache
        cache[pil_hash] = result

        return result
