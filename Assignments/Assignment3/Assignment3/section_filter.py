from simpleimage import SimpleImage

Brightness_Threshold = 0.6*255
def main():
    """
    This program loads an image and applies the narok filter
    to it by setting "bright" pixels to grayscale values.
    """
    image = SimpleImage('images/simba-sq.jpg')
    # Apply the filter
    # TODO: your code here
    for pixel in image:
        #calculate the average brightness of a pixel
        average = pixel_average(pixel)
        if average > Brightness_Threshold:
            #geryscale the pixel
            pixel.red = average
            pixel.blue = average
            pixel.green = average
    image.show()

def pixel_average(pixel):
    '''
    gets the average brightness of a pixel
    Input:
        - pixel
    Output:
        - avergae value of the pixels's brightness
    '''
    return ((pixel.green + pixel.red + pixel.blue)//3)

if __name__ == '__main__':
    main()