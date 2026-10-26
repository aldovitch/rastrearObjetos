# 🔍 Rastreamento de Objetos em Vídeos (rastrearObjetos)

Este é um projeto em Python focado na **identificação e rastreamento contínuo de elementos em vídeos** utilizando visão computacional. O sistema permite selecionar visualmente uma Região de Interesse (ROI) em um frame inicial (como uma pessoa, veículo ou animal) e acompanhá-la automaticamente ao longo do tempo.

---

## 🚀 Como Funciona o Rastreamento?

O projeto utiliza inteligência visual para isolar características geométricas e texturas do elemento demarcado:

1. **Seleção da ROI:** O usuário pausa o primeiro frame do vídeo e desenha uma caixa delimitadora (Bounding Box) na Região de Interesse, ao redor do elemento alvo.
2. **Inicialização pelo CSRT:** O algoritmo **CSRT** mapeia os canais espaciais e a confiabilidade daquela região para criar um modelo matemático do objeto.
3. **Acompanhamento Ponto a Ponto:** Conforme a sequência de vídeo é decodificada, o rastreador calcula a nova posição e atualiza as coordenadas da caixa delimitadora (`bbox`) em tempo real, desenhando um retângulo verde dinâmico sobre o elemento. Se o objeto sair de cena ou sumir, um alerta visual de falha é exibido.

---

## 📺 Demonstração Visual

*(Grave um pequeno GIF ou adicione um print da tela com o retângulo verde acompanhando um objeto e substitua o caminho abaixo)*

![Demonstração do Rastreamento](docs/demonstracao_rastreamento.gif)

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **OpenCV** (Utilizando a API de trackers integrados - `cv2.TrackerCSRT_create`)
* **yt-dlp** (Gerenciador e otimizador de download de mídias do YouTube)

---

## 💻 Instalação e Configuração

Certifique-se de ter o Python configurado e siga o passo a passo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/aldovitch/rastrearObjetos
   ```

2. **Instale as dependências obrigatórias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎯 Como Executar o Projeto

O fluxo de execução está totalmente automatizado e utiliza caminhos relativos, criando uma pasta local `videos/` para gerenciar as mídias.

### 1. Coleta de Vídeos de Teste (Opcional)
Para baixar os vídeos de demonstração configurados (como tráfego urbano e pedestres), execute:
```bash
python src/baixar_videos.py
```

### 2. Rodar o Rastreamento Visual
Para iniciar o mapeamento e testes com o OpenCV:
```bash
python src/teste_rastreamento.py
```

**Instruções de Uso na Interface:**
* **Selecionar Elemento:** Quando a janela do primeiro frame abrir, clique e arraste o mouse criando um retângulo sobre o alvo escolhido.
* **Confirmar Seleção:** Pressione **Enter** ou **Espaço** para iniciar o rastreamento automático.
* **Cancelar/Limpar:** Pressione **c** se quiser refazer o desenho do retângulo antes de confirmar.
* **Sair da Aplicação:** Pressione a tecla **ESC** a qualquer momento para fechar a janela.

---

## 📂 Estrutura de Arquivos

* `src/`
  * `baixar_videos.py`: Script automatizado para baixar e armazenar vídeos do YouTube localmente via `yt-dlp`.
  * `teste_rastreamento.py`: Algoritmo principal que captura os frames do OpenCV, gera a interface de ROI e aplica o rastreamento CSRT.
* `videos/`: Pasta criada automaticamente para armazenar os arquivos `.mp4`.
* `requirements.txt`: Dependências necessárias para a reprodutibilidade do projeto.
* `README.md`: Documentação técnica do sistema.
