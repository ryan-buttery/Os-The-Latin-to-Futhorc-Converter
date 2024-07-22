import base64
from io import BytesIO
from tkinter import PhotoImage


def encode_image_to_base64(image_path: str) -> str:
    """
    Encode an image to a base64 string.

    Args:
    image_path (str): The path to the image file.

    Returns:
    str: The base64 encoded string of the image.
    """
    try:
        # Open the image file in binary mode
        with open(image_path, "rb") as image_file:
            # Read the image file
            image_data = image_file.read()
            # Encode the image data to base64
            base64_encoded_image = base64.b64encode(image_data).decode("utf-8")
            return base64_encoded_image
    except Exception as e:
        print(f"Error encoding image to base64: {e}")
        return None


def decode_base64_image(base64_string: str) -> PhotoImage:
    """
    Decode a base64 string to a PhotoImage object for use in Tkinter.

    Args:
    base64_string (str): The base64 encoded image string.

    Returns:
    PhotoImage: The decoded image as a PhotoImage object.
    """
    image_data = base64.b64decode(base64_string)
    image = PhotoImage(data=BytesIO(image_data).getvalue())
    return image


if __name__ == "__main__":
    pass
