# 🔍 Detecção de Objetos com YOLOv5

Este repositório contém um projeto de detecção de objetos utilizando o framework [YOLOv5](https://github.com/ultralytics/yolov5), com um modelo **já treinado** e pronto para realizar inferência em novas imagens.

O projeto foi desenvolvido como parte da disciplina de **Inteligência Computacional** no IFB.

---

## 🧠 Sobre o projeto

- 📦 Framework: YOLOv5 (Ultralytics)
- 📸 Dataset: Imagens rotuladas do Kaggle
- 🧠 Treinamento: Modelo com **1 classe** (`objeto`)
- ⚙️ Execução local com **CPU**
- ✅ Modelo já treinado incluído no repositório

---

## 📁 Estrutura do Projeto

yolov5/
├── data/
│ ├── images/train/ # Imagens usadas no treinamento e teste
│ ├── labels/train/ # Labels no formato YOLO (geradas a partir de CSV)
│ └── dataset.yaml # Arquivo de configuração do dataset
├── runs/train/exp/weights/
│ └── best.pt # Modelo treinado (peso final)
├── train.py # Script de treinamento
├── detect.py # Script de inferência
├── requirements.txt # Dependências do YOLOv5
└── READMEPROJECT.md # Este arquivo

---

## ⚙️ Requisitos

- Python 3.8+
- PyTorch
- PIL, pandas, matplotlib
- Placa NVIDIA (opcional)

Install as dependências com:

```bash
pip install -r requirements.txt

🚀 Como Rodar a Inferência
Você pode rodar a detecção de objetos nas imagens com o modelo treinado (best.pt) usando:

python detect.py --weights runs/train/exp/weights/best.pt --source data/images/train --conf 0.4

🔄 Parâmetros úteis:
Parâmetro	Descrição
--weights	Caminho para os pesos do modelo treinado
--source	Pasta ou imagem a set analisada (.jpg, .mp4, etc.)
--conf	Nível mínimo de confiança (ex: 0.4)
--device	Use cpu ou 0 para GPU NVIDIA (se disponível)

🖼️ Onde Ver os Resultados
Os resultados da inferência serão salvos automaticamente em:

runs/detect/exp/

Você encontrará as imagens com as caixas de detecção desenhadas ao redor dos objetos.

📌 Extras
O modelo foi treinado com 30 épocas, mas pode set ajustado facilmente com o parâmetro --epochs.

O script de conversão de CSV para YOLO format está disponível em outro branch/opcional.

A estrutura de diretórios segue o padrão official do YOLOv5 para facilitar reuso e expansão.

👨‍💻 Author
Lucas Tony
Ciência da Computação – IFB - Campus Taguatinga
Projeto acadêmico – Inteligência Computacional
```
