# youtube_video_downloader

Este projeto utiliza `yt-dlp` para baixar vídeos do YouTube com a resolução mais alta disponível ou com a resolução escolhida pelo usuário.

## Descrição

- **Nome do Script:** `you_tube_analyzer.py`
- **Propósito:** Baixar vídeos do YouTube com alta qualidade.
- **Funcionalidades:**
  - Permite ao usuário escolher entre as resoluções disponíveis.
  - Seleciona automaticamente a maior resolução disponível, se preferido.

## Requisitos

- Python 3
- yt-dlp

## Uso

1. Clone o repositório para sua máquina local.
   ```bash
   git clone https://github.com/Mrinank-Bhowmick/python-beginner-projects.git
   
2. Navegue até o diretório do script
   ```bash
   cd python-beginner-projects/projects/YouTube\ Video\ Downloader/

3. Instale as dependências necessárias.
   ```bash
   pip install yt-dlp

4. Execute you_tube_analyzer.py
   ```bash
   python3 you_tube_analyzer.py

## Solução de Problemas

Se você encontrar conflitos de dependências com versões mais recentes, siga os passos 
abaixo para configurar um ambiente virtual e instalar as versões específicas necessárias:

### 1. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv meu_ambiente
   source meu-ambiente/bin/activate
```

### 2. Instale as versões compatíveis das dependências:
   ```bash
   pip install requests_mock clyent==1.2.1 nbformat==5.4.0 requests==2.28.1
```

