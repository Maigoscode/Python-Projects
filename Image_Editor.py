# Image Editor:
# Build a script that can resize, crop, and add filters to images using a library like Pillow.


from PIL import Image, ImageFilter

def edit_image(filename):
  im = Image.open(filename)

  # Resize image
  im = im.resize((500, 500))

  # Crop image
  im = im.crop((100, 100, 400, 400))

  # Add filter
  im = im.filter(ImageFilter.BLUR)

  im.show()

edit_image("/Users/muhammad/Downloads/IMG_0773_b.jpg")
