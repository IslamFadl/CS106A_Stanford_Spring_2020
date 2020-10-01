from simpleimage import SimpleImage

def main():
    image = SimpleImage('images/karel.png')
    trimmed_img = trim_crop_image(image, 30)
    trimmed_img.show()


def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_sz pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_sz is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side
                   of the original image

    Returns:
        A new SimpleImage with trim_sz pixels shaved off each
        side of the original image
    """
    # TODO: your code here
    height = original_img.height
    width = original_img.width
    print(height)
    print(width)
    print(trim_size)
    trimmed_img = SimpleImage.blank((width - (2*trim_size)), (height - (2*trim_size)))
    for y in range(trim_size, (height - trim_size)):
        for x in range(trim_size, (width - trim_size)):
            pixel = original_img.get_pixel(x, y)
            trimmed_img.set_pixel((x - trim_size), (y - trim_size), pixel)
    return trimmed_img

if __name__ == '__main__':
    main()