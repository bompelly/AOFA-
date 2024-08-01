from PIL import Image
import os

def convert_jpeg_to_png_with_colors(input_path):
    # Open the image file
    img = Image.open(input_path)
    
    # Convert the image to RGB mode if it's not
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Define the output path
    base, ext = os.path.splitext(input_path)
    output_path = f"{base}.png"
    
    # Save as PNG
    img.save(output_path, 'PNG')
    
    # Extract and list colors
    colors = img.getcolors(maxcolors=1000000)  # Maxcolors can be set as per the image complexity
    unique_colors = set()
    for count, color in colors:
        unique_colors.add(color)
    
    # Create a color summary (for simplicity, we just list them here)
    pms_table_path = f"{base}_PMS_table.txt"
    with open(pms_table_path, 'w') as f:
        f.write("Color Count: {}\n".format(len(unique_colors)))
        for color in unique_colors:
            f.write(f"{color}\n")
    
    return output_path, pms_table_path

# Example usage
input_path = 'image.jpg'
output_path, pms_table_path = convert_jpeg_to_png_with_colors(input_path)

print(f"PNG image saved to: {output_path}")
print(f"Color summary saved to: {pms_table_path}")
