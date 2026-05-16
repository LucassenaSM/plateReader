# Leitor de Placas de Veiculos

Sistema de reconhecimento e rastreamento de placas de veiculos em tempo real utilizando YOLOv8 para deteccao e Pytesseract para OCR.

## Funcionalidades
- Deteccao e rastreamento de placas de veiculos (Mercosul e Antigas).
- Identificacao da cor dominante do veiculo.
- Processamento em tempo real ou via video.
- Salvamento automatico da ultima placa detectada.

## Pre-requisitos
Antes de comecar, voce precisara ter instalado em sua maquina:
- Python 3.8+
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

## Instalacao

1. Clone o repositorio.
2. Crie um ambiente virtual:
   `ash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   `
3. Instale as dependencias:
   `ash
   pip install -r requirements.txt
   `

## Como Usar

Para rodar com a camera padrao (0):
`ash
python run.py --source 0 --show
`

Para rodar com um arquivo de video:
`ash
python run.py --source caminho/do/video.mp4 --show
`

## Estrutura do Projeto
- 
un.py: Ponto de entrada simplificado.
- src/: Codigo fonte modularizado.
- models/: Modelos YOLO (.pt).
- scripts/: Scripts utilitarios.

## Licenca
Este projeto esta sob a licenca MIT.
