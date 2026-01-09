# You import all the IOs of your board
import board

# KMK core
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

# Modules
from kmk.modules.tapdance import TapDance
from kmk.modules.macros import Press, Release, Tap, Macros, Delay

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Enable Macros
macros = Macros()
keyboard.modules.append(macros)

# Enable Tap Dance
tapdance = TapDance()
keyboard.modules.append(tapdance)

# Define your pins here (order matters!)
PINS = [
    board.D8,   # 0
    board.D9,   # 1
    board.D10,  # 2
    board.D11,  # 3
    board.D4,   # 4
    board.D5,   # 5
]

# Tell KMK we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# -----------------------
# MEDIA TAP DANCE (D9)
# -----------------------
TD_SKIP = KC.TD(
    KC.MEDIA_NEXT_TRACK,   # 1 tap
    KC.MEDIA_PREV_TRACK    # 2 taps
)

# -----------------------
# APP LAUNCH MACROS (D10)
# -----------------------

OPEN_SLACK = KC.Macro(
    Press(KC.LCMD),
    Tap(KC.SPACE),
    Release(KC.LCMD),
    Delay(80),
    Tap(KC.S),
    Tap(KC.L),
    Tap(KC.A),
    Tap(KC.C),
    Tap(KC.K),
    Delay(80),
    Tap(KC.ENTER),
)

OPEN_AM = KC.Macro(
    Press(KC.LCMD),
    Tap(KC.SPACE),
    Release(KC.LCMD),
    Delay(80),
    Tap(KC.M),
    Tap(KC.U),
    Tap(KC.S),
    Tap(KC.I),
    Tap(KC.C),
    Delay(80),
    Tap(KC.ENTER),
)

OPEN_DISCORD = KC.Macro(
    Press(KC.LCMD),
    Tap(KC.SPACE),
    Release(KC.LCMD),
    Delay(80),
    Tap(KC.D),
    Tap(KC.I),
    Tap(KC.S),
    Tap(KC.C),
    Tap(KC.O),
    Tap(KC.R),
    Tap(KC.D),
    Delay(80),
    Tap(KC.ENTER),
)

PTM = KC.Macro(
    Press(KC.LCMD),
    Press(KC.LSHIFT),
    Tap(KC.V),
    Release(KC.LSHIFT),
    Release(KC.LCMD),
)


TD_CHAT = KC.TD(
    OPEN_SLACK,     # 1 tap
    OPEN_DISCORD    # 2 taps
)

TD_AM = KC.AM(
    OPEN_AM,
)

TD_PTM = KC.PTM(
    PTM,
)

# -----------------------
# KEYMAP
# -----------------------
keyboard.keymap = [
    [
        KC.MEDIA_PLAY_PAUSE,  # D8
        TD_SKIP,              # D9
        TD_CHAT,              # D10
        TD_AM,                # D11
        TD_PTM,                # D4
        KC.MISSION_CONTROL,                # D5
    ]
]

# Start KMK
if __name__ == '__main__':
    keyboard.go()
