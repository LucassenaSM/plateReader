import cv2
import numpy as np
import webcolors
from sklearn.cluster import KMeans

def get_center(x, y, w, h):
    """Calcula o centro de um retangulo."""
    cx = x + w // 2
    cy = y + h // 2
    return int(cx), int(cy)

def find_closest_color(color):
    """Encontra o nome da cor mais proxima no padrao CSS3."""
    min_colors = {}
    try:
        for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
            r_c, g_c, b_c = webcolors.hex_to_rgb(key)
            rd = (r_c - color[0]) ** 2
            gd = (g_c - color[1]) ** 2
            bd = (b_c - color[2]) ** 2
            min_colors[(rd + gd + bd)] = name
        return min_colors[min(min_colors.keys())]
    except Exception:
        return "Unknown"

def get_dominant_color(image, k=3):
    """Identifica a cor dominante em uma imagem usando KMeans."""
    if image.size == 0:
        return [0, 0, 0]
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    kmeans = KMeans(n_clusters=k, n_init='auto')
    kmeans.fit(image)
    dominant_color = kmeans.cluster_centers_.astype(int)[0]
    return dominant_color
