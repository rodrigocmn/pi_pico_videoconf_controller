import time
import digitalio
import rotaryio
import displayio
import board
import usb_hid
import busio
# Import Keyboard and Keycode from Adafruit CircuitPython HID
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
# Import the SSD1306 module.
import adafruit_displayio_ssd1306
import adafruit_imageload
from controller_config import ControllerConfig


def get_app_config(app_name):
    """
    This function retrieves the active app config and print respective logo on screen
    """

    # refer to global variables
    global audio_keys
    global video_keys
    
    # Load logo
    bitmap, palette = adafruit_imageload.load("img/" + app_name + ".bmp",
                                         bitmap=displayio.Bitmap,
                                         palette=displayio.Palette)
    
    # Display logo
    tile_grid1 = displayio.TileGrid(bitmap, pixel_shader=palette)
    group = displayio.Group()
    group.append(tile_grid1)
    display.show(group)
    
    audio_keys, video_keys = ControllerConfig.get_keyboard_shortcuts(app_name)
    

# Define Buttons' PIN and initial state
buttons = {
    'btn_audio' : [board.GP15,'DOWN'], # Audio Button
    'btn_video' : [board.GP12,'DOWN'], # Video Button
    'btn_confg' : [board.GP7, 'DOWN'], # Config Button
    'btn_rtry' : [board.GP5,'UP']      # Rotary Push Button
}


for k, v in buttons.items():
    globals()[k] = digitalio.DigitalInOut(v[0])
    globals()[k].direction = digitalio.Direction.INPUT
    globals()[k].pull = getattr(digitalio.Pull, v[1])

# Encoder Knob
encoder = rotaryio.IncrementalEncoder(board.GP0, board.GP1)

# Keyboard and Consumer Control
keyboard = Keyboard(usb_hid.devices)
consumer_control = ConsumerControl(usb_hid.devices)

# OLED Display.
displayio.release_displays()
i2c = busio.I2C(board.GP21, board.GP20)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# Change the following according to your display configuration
WIDTH = 128
HEIGHT = 32  

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

# List of supported apps
# (Google Meet, MS Teams and Zoom)
supported_apps = ["meet", "zoom", "teams"]

# Initial settings
last_position = encoder.position
btn_rtry_state = None
active_app_index = 0

# Execute inital application configuration
get_app_config(supported_apps[active_app_index])

while True:
    
    # Check volume change
    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT)
    elif position_change < 0:
        for _ in range(-position_change):
            consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT)
    last_position = current_position
    
    # Check Play/Pause button
    if not btn_rtry.value and btn_rtry_state is None:
        btn_rtry_state = "pressed"
    if btn_rtry.value and btn_rtry_state == "pressed":
        consumer_control.send(ConsumerControlCode.PLAY_PAUSE)
        btn_rtry_state = None
        
    # Check buttons' actions
    if btn_audio.value:
        print("audio presseed")
        keyboard.press(*audio_keys)
        time.sleep(0.1)
        keyboard.release(*audio_keys)
    elif btn_video.value:
        print("video presseed")
        keyboard.press(*video_keys)
        time.sleep(0.1)
        keyboard.release(*video_keys)
    elif btn_confg.value:
        print("config presseed")
        if  active_app_index >= len(supported_apps) - 1 :
            active_app_index = 0
        else:
            active_app_index = active_app_index + 1
        get_app_config(supported_apps[active_app_index])
        time.sleep(0.1)
        
    time.sleep(0.1)



