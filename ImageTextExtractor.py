# Import necessary libraries
from PIL import Image
import pytesseract

# Set the path to the Tesseract executable (change it based on your installation path)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to extract text from a PNG file using OCR
def extract_text_from_png(png_path):
    try:
        # Open the PNG file
        with Image.open(png_path) as img:
            # Perform OCR to extract text
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        # Handle any exceptions that may occur during the process
        print(f"An error occurred: {e}")
        return None

# Example usage of the function
png_path = './photo.png'  # Replace with the path to your PNG file
text_content = extract_text_from_png(png_path)

# Display the extracted text or an error message
if text_content:
    print("Text extracted from PNG:")
    print(text_content)
else:
    print("Failed to extract text from the PNG.")
