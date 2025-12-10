"""
KMK firmware for a 3x3 Xiao RP2040 macropad

Pins:
- Rows: GP0, GP1, GP2
- Cols: GP3, GP4, GP5
- Neopixel (WS2812): GP27 (1 LED)

To use this you must have CircuitPython (or a KMK-compatible MicroPython build)
on the XIAO RP2040 and the KMK library installed under `lib/` on the board.

Copy this file to the board as `main.py` alongside KMK in `lib/`.
"""

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules import rgb
import board


keyboard = KMKKeyboard()

# 3x3 matrix wiring (adjust if your wiring differs)
keyboard.row_pins = (board.GP0, board.GP1, board.GP2)
keyboard.col_pins = (board.GP3, board.GP4, board.GP5)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# Simple 1-LED NeoPixel on GP27
try:
	rgb_mod = rgb.RGB(pixel_pin=board.GP27, num_pixels=1)
	keyboard.modules.append(rgb_mod)
except Exception:
	# If rgb module isn't available on the current KMK build, continue without it
	pass

# Default layer: letters A..I mapped to the 3x3 pad
keyboard.keymap = [
	[
		KC.A, KC.B, KC.C,
		KC.D, KC.E, KC.F,
		KC.G, KC.H, KC.I,
	]
]


if __name__ == "__main__":
	keyboard.go()

