from adafruit_hid.keycode import Keycode

class ControllerConfig:
    
    def get_keyboard_shortcuts(app_name):
        
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
            
    
        
        