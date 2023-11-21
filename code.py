from touch import Touch
from audiooutcontroller import AudioOutController

from board import A0, A1, A2

touch_list = [ # 1x3
    [Touch(A0, 1, 400),
     Touch(A1, 2, 200),
     Touch(A2, 3, 400)]
]

songlist = [
    "audios/polla-ch.mp3",
    "audios/transito-ch.mp3",
    "audios/sorteo_boletas-ch.mp3",
    "audios/gasco-ch.mp3",
]

audio_h = AudioOutController(matrix=touch_list, init_file=songlist[3])


print("Running")
while True:
    touched, fast_touched = audio_h.check(None)
    ##print([i.value() for i in touch_list[0]])
    if not audio_h.is_playing() and not fast_touched[2] and not fast_touched[1] and not fast_touched[0]:
        audio_h.stop_audio()

    if fast_touched[2] and fast_touched[0]:
        audio_h.play_audio(songlist[3], force=True)
    elif touched[0]:
        audio_h.run_stage()
        audio_h.play_audio(songlist[0])
    elif touched[1]:
        audio_h.run_stage()
        audio_h.play_audio(songlist[1])
    elif touched[2]:
        audio_h.run_stage()
        audio_h.play_audio(songlist[2])


