tell application "System Events"
  activate
  if exists window 1 of process "Microsoft Teams" then
    tell application "Microsoft Teams" to activate
    tell application "System Events"
      keystroke "m" using {shift down, command down}
    end tell
  end if
end tell