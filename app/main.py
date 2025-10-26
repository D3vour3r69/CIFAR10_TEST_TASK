from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import torch
import torchvision.transforms as transforms
from PIL import Image
import io
import json

from model_loader import reznet18_for_cifar10

app = FastAPI(title="CIFAR-10 Классификатор API")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = reznet18_for_cifar10()
model.load_state_dict(torch.load('../models/cifar_reznet_best_new.pth', map_location=device))
model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
])

classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")

    try:

        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data)).convert('RGB')
        image = transform(image).unsqueeze(0).to(device)


        with torch.no_grad():
            outputs = model(image)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)[0]
            confidence, predicted = torch.max(probabilities, 0)

        return {
            "prediction": classes[predicted.item()],
            "confidence": round(confidence.item() * 100, 2),
            "all_probabilities": {
                cls: round(prob.item() * 100, 2) for cls, prob in zip(classes, probabilities)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/")
async def root():
    return {"message": "CIFAR-10 Классификатор API"}


@app.get("/classes")
async def get_classes():
    return {"classes": classes}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)