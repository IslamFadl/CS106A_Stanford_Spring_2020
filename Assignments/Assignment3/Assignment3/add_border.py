from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/simba-sq.jpg')
    bordered_img = add_border(image, 10)
    bordered_img.show()
    image.show()


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    # TODO: your code here
    # creating a new simple image taking into account border size
    new_width = original_img.width + border_size*2
    new_height = original_img.height + border_size*2
    bordered_image = SimpleImage.blank(new_width, new_height)
    # double for loop over the pixels
    for x in range(bordered_image.width):
        for y in range(bordered_image.height):
            # checks if a pixel is a border pixel
            if is_border_pixel(x, y, border_size, bordered_image):
                pixel = bordered_image.get_pixel(x, y)
                pixel.red = 0
                pixel.green = 0
                pixel.blue = 0
            else:
                original_pixel = original_img.get_pixel(x - border_size, y - border_size)
                bordered_image.set_pixel(x, y, original_pixel)
    return bordered_image


def is_border_pixel(x, y, border_size, bordered_image):
    '''
    Boolean function checks if a pixel is a border pixel

    :param x: pixel x coordiante in bordered_image
    :param y: pixel y coordiante in bordered_image
    :param border_size: parameter defined by the user
    :param original_img:
    :return: returns True or False
    '''
    if y < border_size:
        return True
    if y >= bordered_image.height - border_size:
        return True
    if x < border_size:
        return True
    if x >= bordered_image.width - border_size:
        return True


if __name__ == '__main__':
    main()