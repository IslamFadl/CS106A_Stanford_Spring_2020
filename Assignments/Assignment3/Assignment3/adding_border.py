from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/simba-sq.jpg')
    bordered_img = add_border(image, 10)
    bordered_img.show()


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
    width = original_img.width
    height = original_img.height
    print(width)
    print(height)
    print(border_size)
    bordered_img = SimpleImage.blank((width + (2*border_size)), (height + (2*border_size))
    for pixel in bordered_img:
        pixel.red = 0
        pixel.green = 0
        pixel.blue = 0
    for y in range(height):
        for x in range(width):
            pixel = original_img.get_pixel(x, y)
            bordered_img.set_pixel( (border_size + x), (border_size + y) , pixel)
    return bordered_img

if __name__ == '__main__':
    main()