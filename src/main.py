import cv2
import os
import argparse
import shutil
import time
from src.core.detector import PlateDetector
from src.core.ocr import PlateOCR
from src.utils.helpers import get_dominant_color, find_closest_color
from src.config.constants import CROPS_DIR, TEMP_DIR

def get_latest_crop(folder_path):
    if not os.path.exists(folder_path): return None
    files = os.listdir(folder_path)
    image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]
    if not image_files: return None
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))
    return os.path.join(folder_path, image_files[-1])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', default='0')
    parser.add_argument('--show', action='store_true')
    args = parser.parse_args()
    
    source = int(args.source) if args.source.isdigit() else args.source
    cap = cv2.VideoCapture(source)
    detector = PlateDetector()
    ocr = PlateOCR()
    
    print(f'Iniciando captura: {source}')
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success: break
        
        results = detector.track(frame)
        for result in results:
            ann = result.plot()
            names = result.names
            
            for box, tid, cls in detector.get_tracking_info(result):
                if names[int(cls)] == 'Placa':
                    path = get_latest_crop(CROPS_DIR)
                    if path:
                        img = cv2.imread(path)
                        if img is not None:
                            txt = ocr.read_plate(img)
                            if txt:
                                print(f'--- DETECCAO ---')
                                print(f'Placa: {txt}')
                                col = find_closest_color(get_dominant_color(img))
                                print(f'Cor: {col}')
                                cv2.imwrite('ultima_placa.png', img)
                                if os.path.exists(TEMP_DIR): 
                                    try:
                                        shutil.rmtree(TEMP_DIR)
                                    except Exception:
                                        pass
                                        
            if args.show: 
                try:
                    cv2.imshow('Leitor', ann)
                except cv2.error:
                    print('Erro: Interface Grafica nao suportada. Remova a flag --show.')
                    args.show = False
                
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
        time.sleep(1)
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
