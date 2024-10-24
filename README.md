
# Introdução a Detecção de Objetos com YOLOv8

Este projeto foi desenvolvido para realizar a **detecção de objetos** utilizando o modelo **YOLOv8** (You Only Look Once). O projeto está estruturado para detectar diferentes tipos de objetos a partir de modelos treinados em datasets específicos, como carros, capacetes de segurança em obras e balões de quadrinhos.

## Estrutura do Repositório

O repositório está organizado da seguinte maneira:

```bash
├── dataset_A
│   └── modelo_A.pt  # Modelo treinado para detecção de carros
├── dataset_B
│   └── modelo_B.pt  # Modelo treinado para detecção de capacetes em obras
├── dataset_C
│   └── modelo_C.pt  # Modelo treinado para detecção de balões de quadrinhos
├── imagem_quadrinhos
│   └── imagem1.png  # Imagens a serem analisadas pelo modelo C (detecção de balões de quadrinhos)
│   └── imagem2.png  # Outra imagem para análise
├── video_canteiro_obra
│   └── video1.mp4  # Vídeo para detecção de capacetes de segurança em obras (usando o modelo B)
│   └── video2.mp4  # Outro vídeo para detecção de capacetes
├── video_carro_na_pista
│   └── video1.mp4  # Vídeo para detecção de carros (usando o modelo A)
│   └── video2.mp4  # Outro vídeo para detecção de carros
```

### Descrição dos Componentes

1. **dataset_A/**: Contém o modelo **`modelo_A.pt`**, que foi treinado para realizar a **detecção de carros**. Esse modelo foi treinado em um dataset com imagens de veículos e está preparado para identificar carros em imagens e vídeos.

2. **dataset_B/**: Contém o modelo **`modelo_B.pt`**, treinado especificamente para a **detecção de capacetes de segurança** em ambientes de obras. Esse modelo pode ser aplicado a vídeos e imagens capturados em canteiros de obras para garantir o uso de equipamentos de segurança.

3. **dataset_C/**: Contém o modelo **`modelo_C.pt`**, treinado para a **detecção de balões de quadrinhos** em imagens de quadrinhos ou cartoons. Esse modelo é útil para identificar balões de fala ou pensamento em desenhos.

4. **imagem_quadrinhos/**: Pasta que contém imagens para análise com o modelo treinado para detectar balões de quadrinhos (**modelo C**).

5. **video_canteiro_obra/**: Contém vídeos que representam canteiros de obras. Esses vídeos podem ser analisados utilizando o modelo B para **detecção de capacetes de segurança**.

6. **video_carro_na_pista/**: Contém vídeos de carros em pistas. Estes vídeos são analisados usando o modelo A para a **detecção de veículos**.

## Uso do Projeto

Para utilizar os modelos pré-treinados para detecção de objetos (carros, capacetes ou balões de quadrinhos), siga as instruções abaixo:

1. **Carregar o modelo treinado**:
    - Se deseja analisar vídeos ou imagens de carros, carregue o **modelo A**.
    - Para a detecção de capacetes de segurança em obras, carregue o **modelo B**.
    - Para detecção de balões de quadrinhos, carregue o **modelo C**.

2. **Realizar a inferência**:
    - Aplique os modelos em vídeos ou imagens armazenadas nas pastas **`imagem_quadrinhos`**, **`video_canteiro_obra`**, e **`video_carro_na_pista`** para realizar a detecção de objetos específicos.

3. **Visualizar os resultados**:
    - O código pode ser configurado para exibir as imagens ou vídeos com as detecções anotadas (bounding boxes).

## Exemplo de Código

Aqui está um exemplo de como carregar e utilizar o modelo para realizar a detecção em uma imagem:

```python
from ultralytics import YOLO
import cv2
from google.colab.patches import cv2_imshow

# Carregar o modelo de detecção de carros (modelo A)
model = YOLO('./dataset_A/modelo_A.pt')

# Caminho da imagem que queremos analisar
imagem_path = './video_carro_na_pista/video1.mp4'

# Realizar a inferência usando o modelo
results = model(imagem_path)

# Exibir o primeiro frame com as anotações
annotated_image = results[0].plot()
cv2_imshow(annotated_image)
```

## Requisitos

- **YOLOv8**: Para realizar a detecção de objetos.
- **OpenCV**: Para manipulação de imagens e vídeos.
- **Google Colab**: (Opcional) para facilitar o desenvolvimento e exibição das imagens.

## Contribuição

Sinta-se à vontade para contribuir com melhorias no projeto, como novos datasets, melhorias no desempenho dos modelos, ou novos exemplos de uso.

