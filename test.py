import time
import random
import os
import PIL.ImageGrab
import win32api
import win32gui
import win32con


KEY_DICT = {
    "w": 87,
    "s": 83,
    "a": 65,
    "d": 68,
    "space": 32
}

FAKE_DICT = {
    "w": 18,
    "s": 18,
    "a": 70,
    "d": 70,
    "space": 32
}
KEY_DICT = FAKE_DICT

def get_pixel_color(i_x, i_y):
    return PIL.ImageGrab.grab().load()[i_x, i_y]

def terminate_app(app_name):
    os.system("taskkill /f /im " + app_name)

def random_walk(hwnd):
    time_delta = random.uniform(45, 75)
    time_press = random.uniform(1, 3)
    key_1 = random.choice(["w", "s"])
    key_2 = random.choice(["a", "d"])
    print(key_1, key_2)

    time.sleep(time_delta)
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, KEY_DICT[key_1], 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, KEY_DICT[key_2], 0)
    time.sleep(time_press)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, KEY_DICT[key_1], 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, KEY_DICT[key_2], 0)

def random_jump(hwnd):
    jump_times = random.randint(0, 3)

    for i in range(jump_times):
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, KEY_DICT["space"], 0)
        time.sleep(random.uniform(1, 3))
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, KEY_DICT["space"], 0)


if __name__ == "__main__":
    WINDOW_NAME = "haha.txt - 记事本"
    hwnd = win32gui.FindWindow(0, WINDOW_NAME)

if hwnd <= 0:
    print("notepad has not detected...")
    print("未启动，脚本关闭中...")
    time.sleep(5)
    exit(0)
else:
    print("detected your program, pls do not close this application")
    print("已检测到，正在运行脚本，请勿关闭窗口")
    while True:
        if get_pixel_color(960, 540) != (0, 0, 0):
            random_walk(hwnd)
            random_jump(hwnd)
        else:
            terminate_app("notepad.exe")
            time.sleep(5)
