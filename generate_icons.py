from PIL import Image
import cairosvg
import io

# Sizes needed for Chrome extension
sizes = [16, 48, 128]

# Read the SVG file
with open('extension/images/icon.svg', 'rb') as svg_file:
    svg_data = svg_file.read()

# Generate PNG files for each size
for size in sizes:
    # Convert SVG to PNG
    png_data = cairosvg.svg2png(bytestring=svg_data, output_width=size, output_height=size)
    
    # Save the PNG file
    with open(f'extension/images/icon{size}.png', 'wb') as png_file:
        png_file.write(png_data)

print("Icons generated successfully!") 