from ultralytics import YOLO
import torch
torch.cuda.empty_cache()

# Carregar o modelo YOLOv8 pré-treinado // fixo 
model = YOLO("yolov8n.pt")

# selecione o caminho path para data.yaml
data = f""

# Treinar o modelo
results = model.train(
    data=data,
    epochs=30,
    imgsz=512,
    project=f"runs/custom_project",
    name="builds",
    patience=0,
)
