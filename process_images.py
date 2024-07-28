import os
import pytesseract
from PIL import Image

# Caminho onde o Tesseract está instalado
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Diretórios de entrada e saída
input_dir = 'Inputs'
output_dir = 'Output'

# Certifique-se de que os diretórios existam
if not os.path.exists(input_dir):
    print(f"O diretório {input_dir} não existe. Por favor, crie-o e adicione imagens para processar.")
    exit()

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Processar cada imagem no diretório de entrada
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        # Caminho completo da imagem
        image_path = os.path.join(input_dir, filename)
        
        # Abrir a imagem
        with Image.open(image_path) as img:
            # Usar o Tesseract para reconhecer o texto
            text = pytesseract.image_to_string(img)
            
            # Nome do arquivo de saída
            output_file_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
            
            # Escrever o texto reconhecido no arquivo de saída
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(text)
                
        print(f"Processado {filename} e salvo em {output_file_path}")

print("Processamento concluído.")
