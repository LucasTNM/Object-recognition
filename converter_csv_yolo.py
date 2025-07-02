import pandas as pd
import os
from PIL import Image
import shutil
import glob

# Verificar se o arquivo existe antes de tentar carregá-lo
csv_dir = '../../yolo_images/data/'
csv_candidates = glob.glob(os.path.join(csv_dir, 'train_solution_bounding_boxes*.csv'))

print(f"\nArquivos encontrados em {csv_dir}:")
if os.path.exists(csv_dir):
    for file in os.listdir(csv_dir):
        print(f"  - {file}")
else:
    print("❌ Diretório não encontrado!")

if not csv_candidates:
    print(f"Nenhum CSV encontrado em {csv_dir}")
    exit(1)

csv_path = csv_candidates[0]  # Pega o primeiro que encontrar
print(f"Usando CSV: {csv_path}")

# Verificar se o arquivo existe
if not os.path.exists(csv_path):
    print(f"Arquivo CSV não encontrado: {csv_path}")
    print("Arquivos disponíveis na pasta:")
    csv_dir = os.path.dirname(csv_path)
    if os.path.exists(csv_dir):
        for file in os.listdir(csv_dir):
            if file.endswith('.csv'):
                print(f"  - {file}")
    else:
        print(f"Diretório não encontrado: {csv_dir}")
    exit(1)

images_path = '../../yolo_images/data/training_images'
labels_output_path = 'data/labels/train'
images_output_path = 'data/images/train'

os.makedirs(labels_output_path, exist_ok=True)
os.makedirs(images_output_path, exist_ok=True)

# Classe única (0)
class_id = 0

# Carregar CSV
try:
    df = pd.read_csv(csv_path)
    df = df.drop_duplicates()
    print(f"CSV carregado com sucesso: {len(df)} linhas encontradas")
except Exception as e:
    print(f"Erro ao carregar CSV: {e}")
    exit(1)

# ...existing code...
for image_name, group in df.groupby('image'):
    image_file = os.path.join(images_path, image_name)
    if not os.path.exists(image_file):
        print(f"Imagem não encontrada: {image_file}, pulando.")
        continue

    # Copiar imagem para a pasta YOLO
    shutil.copy(image_file, os.path.join(images_output_path, image_name))

    # Abrir imagem para obter dimensões
    with Image.open(image_file) as img:
        w, h = img.size

    # Criar arquivo de label
    label_file = os.path.join(labels_output_path, image_name.replace('.jpg', '.txt'))
    with open(label_file, 'w') as f:
        for _, row in group.iterrows():
            xmin, ymin, xmax, ymax = row['xmin'], row['ymin'], row['xmax'], row['ymax']
            x_center = ((xmin + xmax) / 2) / w
            y_center = ((ymin + ymax) / 2) / h
            bbox_width = (xmax - xmin) / w
            bbox_height = (ymax - ymin) / h
            f.write(f"{class_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n")

print("Conversão concluída com sucesso!")