import cv2
import numpy as np
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

def compare_images(img1, img2):
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    score, _ = cv2.quality.QualitySSIM_compute(img1_gray, img2_gray)
    return score[0]

@app.post("/compare")
async def compare(reference: UploadFile = File(...), target: UploadFile = File(...)):
    try:
        reference_img = cv2.imdecode(np.frombuffer(reference.file.read(), np.uint8), cv2.IMREAD_COLOR)
        target_img = cv2.imdecode(np.frombuffer(target.file.read(), np.uint8), cv2.IMREAD_COLOR)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error processing images")

    score = compare_images(reference_img, target_img)
    return JSONResponse(content={"similarity_score": score})