import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize keyboard
kbd = Keyboard(usb_hid.devices)

# Define pins for 6 switches (adjust if wired differently)
switch_pins = [board.D0, board.D1, board.D2, board.D3, board.D4, board.D5]

# Setup switches
switches = []
for pin in switch_pins:
    sw = digitalio.DigitalInOut(pin)
    sw.direction = digitalio.Direction.INPUT
    sw.pull = digitalio.Pull.UP
    switches.append(sw)

# Map each switch to a key or shortcut
keymap = [
    Keycode.A,                # Switch 1 → "A"
    Keycode.B,                # Switch 2 → "B"
    Keycode.C,                # Switch 3 → "C"
    [Keycode.CONTROL, Keycode.C],  # Switch 4 → "Ctrl+C"
    [Keycode.CONTROL, Keycode.V],  # Switch 5 → "Ctrl+V"
    Keycode.F13               # Switch 6 → "F13" (macro key)
]

while True:
    for i, sw in enumerate(switches):
        if not sw.value:  # pressed (active low)
            if isinstance(keymap[i], list):
                kbd.press(*keymap[i])
            else:
                kbd.press(keymap[i])
        else:
            if isinstance(keymap[i], list):
                kbd.release(*keymap[i])
            else:
                kbd.release(keymap[i])
