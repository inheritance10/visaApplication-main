import os
from google.cloud import vision
import io

# Kimlik bilgileri dosyasının yolunu belirtin

def detect_text_from_image(image_content):
    # Google Cloud Vision istemcisi oluştur
    client = vision.ImageAnnotatorClient()

    # Görüntüyü yükle
    image = vision.Image(content=image_content)

    # Metin tespiti için API'yi çağır
    response = client.text_detection(image=image)
    texts = response.text_annotations

    # Sonuçları birleştir
    detected_text = ' '.join([text.description for text in texts])

    return detected_text

