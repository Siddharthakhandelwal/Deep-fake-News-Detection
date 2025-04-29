from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size):
    # Create a new image with a transparent background
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw a circle
    circle_color = (76, 175, 80)  # Green color
    draw.ellipse([(2, 2), (size-2, size-2)], fill=circle_color)
    
    # Add text "DF" in the center
    try:
        font_size = int(size * 0.5)
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "DF"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    position = ((size - text_width) // 2, (size - text_height) // 2)
    draw.text(position, text, fill=(255, 255, 255), font=font)
    
    return image

def main():
    # Create icons directory if it doesn't exist
    os.makedirs('extension/icons', exist_ok=True)
    
    # Generate icons in different sizes
    sizes = [16, 48, 128]
    for size in sizes:
        icon = create_icon(size)
        icon.save(f'extension/icons/icon{size}.png')

if __name__ == '__main__':
    main() 