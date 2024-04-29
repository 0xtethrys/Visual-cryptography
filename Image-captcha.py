from random import randint
from PIL import Image, ImageDraw, ImageFont

def generate_captcha(width, height, length):
    # Define the image and font properties
    font_size = 36
    font = ImageFont.truetype("arial.ttf", font_size)
    background_color = (255, 255, 255)
    text_color = (0, 0, 0)
    
    # Create a new image
    image = Image.new("RGB", (width, height), background_color)
    
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    
    # Generate a random string of digits
    captcha_text = "".join([str(randint(0, 9)) for _ in range(length)])
    
    # Calculate the size of the text
    text_width, text_height = draw.textsize(captcha_text, font=font)
    
    # Calculate the position of the text
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    # Draw the text
    draw.text((x, y), captcha_text, font=font, fill=text_color)
    
    # Add some noise to the image
    for i in range(10):
        x = randint(0, width - 1)
        y = randint(0, height - 1)
        draw.point((x, y), fill=(0, 0, 0))
    
    # Apply a random rotation to the image
    angle = randint(-15, 15)
    image = image.rotate(angle)
    
    # Return the image and the captcha text
    return image, captcha_text

# Example usage
captcha_image, captcha_text = generate_captcha(200, 100, 6)
captcha_image.show()
print("CAPTCHA Text:", captcha_text)
