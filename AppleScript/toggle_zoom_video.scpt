tell application "System Events"
  if exists window 1 of process "zoom.us" then
    tell application process "zoom.us"
      if exists (menu 1 of menu bar item "Meeting" of menu bar 1) then
        set meetingMenu to menu 1 of menu bar item "Meeting" of menu bar 1
        set canStopVideo to exists menu item "Stop Video" of meetingMenu
        set canStartVideo to exists menu item "Start Video" of meetingMenu
        if canStartVideo then
          click menu item "Start Video" of meetingMenu
        else if canStopVideo then
          click menu item "Stop Video" of meetingMenu
        end if
      end if
    end tell
  end if
end tell