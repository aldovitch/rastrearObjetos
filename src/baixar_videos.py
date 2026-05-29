import yt_dlp

# Lista de URLs dos vídeos
urls = [
    #'https://www.youtube.com/watch?v=MNn9qKG2UFI',  # carros
    'https://www.youtube.com/watch?v=WxTA4r4V9uQ',  # pessoas
    #'https://www.youtube.com/watch?v=1YKdGCgMR6s', # birds,
    #'https://www.youtube.com/shorts/zkmE82Tpl7c',
    'https://www.youtube.com/shorts/MeHau8mn8LE' #tokio
]
#videoset_path = './videos/'
videoset_path = 'D:/_sets_/videosets/'

for url in urls:
    ydl_opts = {
        'outtmpl': videoset_path + '%(title)s.%(ext)s',
        'format': 'best[height<=1200]',  # qualidade menor para testar
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])