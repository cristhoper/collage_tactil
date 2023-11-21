from supervisor import ticks_ms
from touchio import TouchIn


class Touch:
  def __init__(self, pin, name, threshold):
    self.touch = TouchIn(pin)
    self.last_press = 0
    self.name = name
    self.index = name - 1
    self.pressed = False
    self.init_value = self.touch.raw_value
    self.last_value = self.init_value
    self.threshold = threshold

  def milliseconds():
    return ticks_ms()

  def value(self):
    return self.touch.raw_value

  def filter_data(self, value):
    alpha = 0.5
    value = alpha * self.touch.raw_value + (1-alpha) * value
    return value

  def reading(self):
    return self.last_value

  def set_init_value(self,value):
    self.init_value = value
    return self.init_value

  def read_raw(self):
    return self.touch.raw_value

  def ispressed(self):
    self.last_value = self.filter_data(self.last_value)
    self.pressed = self.last_value - self.init_value > self.threshold # for rpi (resistivo)
    return self.pressed

  def just_pressed(self):
    now = ticks_ms()
    if now - self.last_press < 750:
      return True
    else:
      return False

  def set_press(self):
    self.last_press = ticks_ms()

