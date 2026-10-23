import cv2
print(cv2.__version__)

rastreador = cv2.TrackerCSRT_create()
# rastreador = cv2.TrackerMOSSE_create()
videos = [
    'rua.mp4', 
    '4K Road traffic video for object detection and tracking - free download now!.mp4',
    'largada da corrida infantil Pré Mirim no dia 7 de maio no parque Iguaçu.mp4'
]
videoset_path = './videos/'
# videoset_path = 'D:/_sets_/videosets/'

n_video = 0
video = cv2.VideoCapture(videoset_path + videos[n_video])

ok, frame = video.read()
print("ok=", ok)
if (not ok):
    print("Não foi possível ler o vídeo")
    quit()
    
bbox = cv2.selectROI(frame, False) #Seleciona a Region Of Interest (ROI) para rastreamento
#print("bbox=", bbox) #ROI selecionada

ok = rastreador.init(frame, bbox) #Inicializa o rastreador com o frame e a ROI selecionada

while True:
    ok, frame = video.read()
    if not ok:
        break

    ok, bbox = rastreador.update(frame) #Atualiza o rastreador e retorna a nova bbox

    if ok: #Se o rastreamento for bem sucedido
        x, y, w, h = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2, 1) #Desenha um retângulo verde na região rastreada
    else: #Se o rastreamento falhar
        cv2.putText(frame, "Rastreamento Falhou", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0, 0, 255), 2)

    cv2.imshow('Rastreamento', frame) #Mostra o frame com o rastreamento
    if cv2.waitKey(1) & 0XFF == 27: #Pressione 'ESC' para sair
        break
