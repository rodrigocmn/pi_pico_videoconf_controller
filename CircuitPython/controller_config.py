from adafruit_hid.keycode import Keycode

# Identifies the operating system
# Valid values:
#   mac - MacOS (requires respective Automation config)
#   win - Windows (not yet implemented - need tests with AutoHotKey)
#   default - all OSs (requires the app to be active)
# for more information visit: https://connection.rnascimento.com
os_identifier = "default"

class ControllerConfig:
    
    def get_keyboard_shortcuts(app_name):

        # Use keyboard shortcuts for Quick Action (Automator/AppleScript)
        if os_identifier == "mac":

            if app_name == "meet":
                audio_keys = Keycode.CONTROL, Keycode.SHIFT, Keycode.COMMAND, Keycode.F1
                video_keys = Keycode.CONTROL, Keycode.SHIFT, Keycode.COMMAND, Keycode.F2

            elif app_name == "teams":
                audio_keys = Keycode.CONTROL, Keycode.SHIFT, Keycode.COMMAND, Keycode.F3
                video_keys = Keycode.CONTROL, Keycode.SHIFT, Keycode.COMMAND, Keycode.F4

            elif app_name == "zoom":
                audio_keys = Keycode.CONTROL, Keycode.SHIFT, Keycode.COMMAND, Keycode.F5
                video_keys = Keycode.CONTROL, Keycode.SHIFT, Keycode.COMMAND, Keycode.F6

        # Use apps' default shortcuts (requires app to be active)
        else:

            if app_name == "meet":
                audio_keys = Keycode.COMMAND, Keycode.D
                video_keys = Keycode.COMMAND, Keycode.E

            elif app_name == "teams":
                audio_keys = Keycode.SHIFT, Keycode.COMMAND, Keycode.M
                video_keys = Keycode.SHIFT, Keycode.COMMAND, Keycode.O

            elif app_name == "zoom":
                audio_keys = Keycode.SHIFT, Keycode.COMMAND, Keycode.A
                video_keys = Keycode.SHIFT, Keycode.COMMAND, Keycode.V
        
        return audio_keys,video_keys
            
    
        
        