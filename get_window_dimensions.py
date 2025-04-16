import win32gui

def get_top_left(window_name):
    # Assumes 1080p res. for game (fullscreen or windowed)
    # Add window detection here (i.e. a msg when the window exists)
    window_handle = win32gui.FindWindow(None, window_name)
    client_rect = win32gui.GetClientRect(window_handle)
    screen_res = (client_rect[2], client_rect[3])
    window_btm_right = win32gui.ClientToScreen(window_handle, screen_res)
    window_top_left = (window_btm_right[0] - 1920, window_btm_right[1] - 1080)

    return window_top_left
