from PIL import Image
def encode_message(image_path, message, output_path):
    img = Image.open(image_path)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')  # Ensure the image is in RGBA format
    encoded = img.copy()
    width, height = img.size
    message += "###"
    binary_message = ''.join([format(ord(char), '08b') for char in message])
    data_index = 0
    for row in range(height):
        for col in range(width):
            if data_index < len(binary_message):
                r, g, b, a = img.getpixel((col, row))
                new_r = (r & ~1) | int(binary_message[data_index])
                encoded.putpixel((col, row), (new_r, g, b, a))
                data_index += 1
            else:
                break
        if data_index >= len(binary_message):
            break
    encoded.save(output_path, "PNG")  # Save as PNG to support RGBA
    print(f"Message encoded and saved as {output_path}")
def decode_message(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_message = ""
    for row in range(height):
        for col in range(width):
            r, g, b, a = img.getpixel((col, row))
            binary_message += str(r & 1)
    message = ''.join([chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)])
    end_marker = message.find("###")
    if end_marker != -1:
        return message[:end_marker]
    return "No hidden message found"
