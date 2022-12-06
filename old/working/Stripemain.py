import board
import displayio
import framebufferio
import rgbmatrix

bit_depth_value = 3
base_width = 64
base_height = 32
chain_across = 1
tile_down = 1
serpentine_value = True

width_value = base_width * chain_across
height_value = base_height * tile_down

# If there was a display before (protomatter, LCD, or E-paper), release it so
# we can create ours
displayio.release_displays()


#display = board.DISPLAY
matrix = rgbmatrix.RGBMatrix(
    width=width_value,
    height=height_value,
    bit_depth=bit_depth_value,
    rgb_pins=[board.GP2, board.GP3, board.GP4, board.GP5, board.GP8, board.GP9],
    addr_pins=[board.GP10, board.GP16, board.GP18, board.GP20],
    clock_pin=board.GP11,latch_pin=board.GP12,output_enable_pin=board.GP13,
    tile=tile_down,serpentine=serpentine_value,
    doublebuffer=True,
)


# Associate the RGB matrix with a Display so that we can use displayio features
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)
display.rotation = 0

rainbow = [
    (255, 0, 0), (255, 54, 0), (255, 109, 0), (255, 163, 0),
    (255, 218, 0), (236, 255, 0), (182, 255, 0), (127, 255, 0),
    (72, 255, 0), (18, 255, 0), (0, 255, 36), (0, 255, 91),
    (0, 255, 145), (0, 255, 200), (0, 255, 255), (0, 200, 255),
    (0, 145, 255), (0, 91, 255), (0, 36, 255), (18, 0, 255),
    (72, 0, 255), (127, 0, 255), (182, 0, 255), (236, 0, 255),
    (255, 0, 218), (255, 0, 163), (255, 0, 109), (255, 0, 54),
]
l=len(rainbow)
bitmap = displayio.Bitmap(width_value-1, height_value-1, l)
palette = displayio.Palette(l)

#print (len(rainbow))

def rgb2hex(r,g,b):
    return "0x{:02x}{:02x}{:02x}".format(r,g,b)

def getIfromRGB(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    RGBint = (red<<16) + (green<<8) + blue
    return RGBint

i=0
for (r,g,b) in rainbow:
    #print (r,g,b)
    #print (i)
    palette[i]=[r,g,b]
    i+=1
#palette=rainbow
#palette[0]=0x0000ff




# Create a TileGrid using the Bitmap and Palette
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)

# Create a Group
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)

# Add the Group to the Display
display.show(group)






# Draw a pixel
bitmap[0, 0] = 1

# Draw even more pixels
for x in range(0, 63):
    for y in range(0, 31):
        bitmap[x, y] = x % 27 #getIfromRGB(rainbow[1])

# Loop forever so you can enjoy your image
while True:
    pass
