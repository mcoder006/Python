
from PIL import Image, ImageDraw, ImageFont

def main():
    print("Text to handwritten notes in Python : ")
    text = ("Python is a high-level, interpreted programming language known for its simplicity and readability. "
            "Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code "
            "readability and syntax that allows programmers to express concepts in fewer lines of code compared to "
            "languages like C++ or Java.")

    # Create an image with white background
    img = Image.new('RGB', (800, 400), color=(255, 255, 255))

    # Initialize ImageDraw
    d = ImageDraw.Draw(img)

    # Load a font (use a TTF file available on your system or download one)
    try:
        font = ImageFont.truetype("Caveat-Regular.ttf", 30)
    except IOError:
        print("Font file not found, using default font.")
        font = ImageFont.load_default()

    # Add text to image
    d.text((10, 10), text, font=font, fill=(0, 0, 0))

    # Save the image
    img.save("python.png")
    print("Ended.")

if __name__ == "__main__":
    main()
