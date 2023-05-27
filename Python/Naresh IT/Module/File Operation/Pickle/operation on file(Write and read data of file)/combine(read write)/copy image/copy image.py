try:
    with open("example.jpg", "rb") as rb:
        with open("copied image/copied.png", "wb") as wb:
            orgnialImg = rb.read()      # Copied the image
            wb.write(orgnialImg)
            print("Image Copied successfully.")
except FileNotFoundError:
    print("Image does not found.")