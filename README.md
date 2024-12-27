# holofishing
Bot for fishing in Holocure. Windows only.

Hardcoded for 1920x1080 (both fullscreen and windowed should work) and WASD controls.

Usage:
1. Run holofishingbot.exe
2. Have Holocure on your main 1920x1080 monitor
3. Walk up to the fishing pond
4. Press 'F' to toggle auto-fishing
5. Press 'K' to kill the program

Python Dependencies:
- opencv-python
- mss
- pydirectinput
- numpy
- pynput
- pywin32

Known issues:
- When changing from fullscreen to windowed mode, the windowed borders may have black borders. Change the resolution to remove them.

Plans:
1. Support different resolutions (maybe scaling if possible)
2. Add some print text or GUI to give user feedback on when buttons are pressed
3. Add text file to change input keys
4. Support running on secondary monitors