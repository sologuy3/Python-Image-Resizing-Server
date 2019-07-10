from PIL import Image
import io

def resize_image(image_path, target_size):
    """

    :param image_path: Path to image as string
    :param target_size: Size as a tuple (width, height)
    :return:
    """
    o_img = Image.open(image_path)
    format = o_img.format
    width_match = o_img.size[0] == target_size[0]
    height_match = o_img.size[1] == target_size[1]
    imgByteArr = io.BytesIO()
    if (not width_match) or (not height_match):
        re_image = o_img.resize(target_size)

    else:
        re_image = o_img

    re_image.save(imgByteArr, format=format)
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr




