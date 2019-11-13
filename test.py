def get_pixel_color(i_x, i_y):
    import PIL.ImageGrab
    return PIL.ImageGrab.grab().load()[i_x, i_y]

def terminate_app(app_name):
    import os
    os.system("taskkill /f /im " + app_name)

if __name__ == "__main__":
    import time
    while True:
        time.sleep(0.3)
#        print(get_pixel_color(960, 540))
        if get_pixel_color(960, 540) == (0,0,0):
            terminate_app("notepad.exe")
