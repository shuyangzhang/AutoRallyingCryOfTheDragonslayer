def get_pixel_color(i_x, i_y):
    import PIL.ImageGrab
    return PIL.ImageGrab.grab().load()[i_x, i_y]

if __name__ == "__main__":
    get_pixel_color(960, 540)
