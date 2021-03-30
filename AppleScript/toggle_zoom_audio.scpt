tell application "System Events"
  if exists window 1 of process "zoom.us" then
    tell application process "zoom.us"
      if exists (menu 1 of menu bar item "Meeting" of menu bar 1) then
        set meetingMenu to menu 1 of menu bar item "Meeting" of menu bar 1
        set canMute to exists menu item "Mute audio" of meetingMenu
        set canUnmute to exists menu item "Unmute audio" of meetingMenu
        if canUnmute then
          click menu item "Unmute audio" of meetingMenu
        else if canMute then
          click menu item "Mute audio" of meetingMenu
        end if
      end if
    end tell
  end if
end tell