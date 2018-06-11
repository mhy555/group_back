import colorsys
from PIL import Image

# GET DOMINANT COLOR OF THE IMAGE
def get_dominant_color(image):
    image = image.convert('RGBA')
    image.thumbnail((200, 200))

    max_score = 0
    dominant_color = 0
    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        if a == 0:
            continue
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
        y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        y = (y - 16.0) / (235 - 16)
        score = (saturation + 0.1) * count
        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
    return dominant_color

# CHANGE RGB VALUE TO HSV VALUE
def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = df/mx
    v = mx
    return h, s, v

# GET COLOR NAME OF THE IMAGE
def get_color_name(image):
    r,g,b = get_dominant_color(image)
    h,s,v = rgb2hsv(r, g, b)
    h /=360
    if(s == 0 and v < 0.98 and v > 0.4):
        return 'grey'
    if(v == 0):
        return 'black'
    if(s == 0 and v >= 0.98):
        return 'white'
    if (((h >= 0 and h <= 0.05) or (h > 0.95 and h <=1)) and( v >= 0.55)):
        return 'red'
    if(((h >= 0.051 and h <= 0.1)) and (v >= 0.55)):
        return 'orange'
    if(h > 0.1 and h <= 0.19):
        return 'yellow'
    if(h > 0.19 and h <= 0.45):
        return 'green'
    if(h > 0.45 and h <= 0.5):
        return 'cyan'
    if(h > 0.5 and h <= 0.73):
        return 'blue'
    if(h > 0.73 and h <= 0.83):
        return 'purple'
    if(h > 0.83 and h <= 0.95):
        return 'pink'
    if (((h >= 0 and h <= 0.1) or (h >= 0.95 and h <= 1) ) and (v < 0.55)):
        return 'brown'
