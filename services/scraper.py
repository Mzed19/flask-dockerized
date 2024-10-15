from flask import request, jsonify
from flask_smorest import Blueprint
import easyocr
from PIL import Image

# Cria um Blueprint no Flask-Smorest
scraper_bp = Blueprint("scraper", __name__, description="Operações de OCR")

# Instancia o leitor de OCR
reader = easyocr.Reader(['en', 'pt'])  # Suporta português e inglês

# Define a rota dentro do blueprint
@scraper_bp.route('/extract', methods=['POST'])
def extract_text():
    """Endpoint para extrair texto de uma imagem usando OCR"""
    file = request.files['image']  # Recebe a imagem
    img = Image.open(file)

    # Realiza o OCR
    extracted_text = reader.readtext(img, detail=0)

    # Retorna o texto extraído
    return jsonify({'text': ' '.join(extracted_text)})
