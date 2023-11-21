from audiomp3 import MP3Decoder
from audiopwmio import PWMAudioOut
from board import GP0, GP1


class AudioOutController:

  def __init__(self, matrix, init_file):
    self.matrix = matrix
    for axis in self.matrix:
      for pad in axis:
        pad.set_init_value(pad.touch.raw_value)
    self.audio = PWMAudioOut(quiescent_value=0,
      left_channel=GP0,
      right_channel=GP1)
    self.decoder = MP3Decoder(open(init_file, "rb"))
    self.len_m = len(self.matrix[0])
    self.touch_ids = [0]*self.len_m
    self.fast_touch_ids = [0]*self.len_m

  def stop_audio(self):
    self.audio.stop()

  def play_audio(self, filename=None, force=False):
    if filename is not None:
      print("filename: "+filename)
      self.decoder.file = open(filename, "rb")
    if force and self.audio.paused:
      self.audio.resume()
    if not self.audio.playing:
      print("playing {}".format(filename))
      self.audio.play(self.decoder)

  def run_stage(self):
    if self.audio.playing and self.audio.paused:
      self.audio.resume()
      print("continue")
    elif self.audio.playing and not self.audio.paused:
      self.audio.pause()
      print("paused")
    return self.audio.paused

  def is_playing(self):
    return self.audio.playing

  def check(self,  alarm):
    self.touch_ids = [0]*self.len_m
    self.fast_touch_ids = [0]*self.len_m
    for axis in self.matrix:
      for _i in range(self.len_m):
        for pad in axis:
          if pad.ispressed() and not pad.just_pressed():
            pad.set_press()
            self.touch_ids[pad.index] = 1
          if pad.ispressed() and pad.just_pressed():
            self.fast_touch_ids[pad.index] = 1
    return self.touch_ids, self.fast_touch_ids




