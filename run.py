from PIL import Image

def get_colour_frequency(im, tolerance=0.01):

    # tolerance is the 'threshold' of minimum colour usage
    colour_frequency = {}
    width, height = im.size

    # iterate through image
    for i in range(width):
        for j in range(height):

            # get rgb colour
            rgb_colour = im.getpixel((i, j))

            if rgb_colour in colour_frequency:
                colour_frequency[rgb_colour] += 1
            else:
                colour_frequency[rgb_colour] = 1

    # remove colours below tolerance threshold
    for colour in list(colour_frequency):
        if colour_frequency[colour] < (width*height)*tolerance:
            colour_frequency.pop(colour)

    return colour_frequency

# import image
im = Image.open('world_flags/jp.png').convert('RGB')

# get ratio
width, height = im.size
ratio = round(width / height, 2)

# get colour frequency
colour_frequency = get_colour_frequency(im)
print(colour_frequency)