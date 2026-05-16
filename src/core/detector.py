from ultralytics import YOLO
from collections import defaultdict
from src.config.constants import DEFAULT_MODEL

class PlateDetector:
    def __init__(self, model_path=DEFAULT_MODEL):
        self.model = YOLO(model_path)
        self.track_history = defaultdict(lambda: [])

    def track(self, frame, persist=True):
        return self.model.track(frame, persist=persist, save_crop=True, project='temp/', exist_ok=True)

    def get_tracking_info(self, result):
        if not result.boxes or result.boxes.id is None:
            return []
        boxes = result.boxes.xywh.cpu()
        track_ids = result.boxes.id.int().cpu().tolist()
        classes = result.boxes.cls.tolist()
        return zip(boxes, track_ids, classes)
