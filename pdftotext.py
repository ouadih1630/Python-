import PyPDF2
from pathlib import Path

def pdf_to_text(pdf_path):
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)

            # Get the number of pages in the PDF
            num_pages = len(pdf_reader.pages)

            # Initialize an empty string to store text
            text = ""

            # Iterate through all pages
            for page_num in range(num_pages):
                # Get the page
                page = pdf_reader.pages[page_num]

                # Extract text from the page
                text += page.extract_text()

            return text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage

pdf_path = "..\..\Documents\SVT 2015 RATTRAPPAGE.pdf"
text_content = pdf_to_text(pdf_path)
if text_content:
    print("Text extracted from PDF:")
    print(text_content)
else:
    print("Failed to extract text from the PDF.")
