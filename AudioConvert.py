#Для использования необходимо подключить библиотеки moviepy и ipywidgets
#Импортируем библиотеку
import moviepy.editor

#Прописываем код для конвертации видео в аудио дорожку
video = moviepy.editor.VideoFileClip("Название видеодорожки")
audio = video.audio

audio.write_audiofile("Название аудиофайла")