import sys
import os
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prepare_photo(input_path, output_path="data/source-prepped.png"):
    if not os.path.exists(input_path):
        print(f"Error: No se encontro el archivo {input_path}")
        return

    print("1/3 Eliminando fondo...")
    with open(input_path, "rb") as inp:
        no_bg_bytes = remove(inp.read())
    
    # Cargar imagen procesada
    nparr = np.frombuffer(no_bg_bytes, np.uint8)
    img_rgba = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    print("2/3 Ajustando contraste y escala de grises...")
    b, g, r, a = cv2.split(img_rgba)
    rgb = cv2.merge([b, g, r])
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

    # Aumentar contraste local (CLAHE)
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    enhanced_gray = clahe.apply(gray)

    print("3/3 Componiendo sobre fondo blanco...")
    alpha_mask = a / 255.0
    white_bg = np.ones_like(enhanced_gray, dtype=np.uint8) * 255
    final_gray = (enhanced_gray * alpha_mask + white_bg * (1 - alpha_mask)).astype(np.uint8)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, final_gray)
    print(f"Listo! Imagen guardada en: {output_path}")

if __name__ == "__main__":
    img_file = sys.argv[1] if len(sys.argv) > 1 else "source-photo.jpg"
    prepare_photo(img_file)