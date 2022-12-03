from adafruit_display_text import label
from adafruit_display_text import scrolling_label
from adafruit_bitmap_font import bitmap_font

def Init:

    fontLarge = "/lib/fonts/Tahoma-bold-32.bdf"
    fontSmall = "/lib/fonts/Tahoma-bold-12.bdf"

    FONTlarge = bitmap_font.load_font(fontLarge)
    FONTsmall = bitmap_font.load_font(fontSmall)

    #_, height, _, dy = FONTlarge.get_bounding_box()

    line1 = label.Label(FONTlarge, color=0x00ff00, scale=1)

    centered=False

    if centered:
        line1.anchor_point = (0.5, 0.5)
        line1.anchored_position = ((display.width // 2) - 2, display.height // 2)
else:
        line1.anchor_point = (0.0, 0.5)
        line1.anchored_position = (2, display.height // 2)


    line2 = label.Label(FONTsmall, color=0x00ff00, scale=1)
    line2.anchor_point = (0.0, 0.0)
    line2.anchored_position = (47,20)


    g = displayio.Group()
    g.append(line1)
    g.append(line2)

    display.show(g)

def ProcessColor(db):
    if db <= 40:
        dcolor=0x00ff00
    elif db <= 50:
        dcolor= 0x12ff00
    elif db <= 60:
        dcolor=0x48ff00
    elif db <= 70:
        dcolor=0xb6ff00
    elif db <= 80:
        dcolor=0xff6d00
    elif db <= 90:
        dcolor=0xff3600
    elif db <= 100:
        dcolor=0xff1200
    elif db <= 110:
        dcolor=0xff0000
    elif db > 110:
        dcolor=0xff006d

    return dcolor


def ShowDecibel(decibel):

    line2.color=ProcessColor(decibel)

    line1.text = f"{decibel}"
    line2.text = "dB"
