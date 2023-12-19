from pdfminer.high_level import extract_text
import re
import json


def extract_data_from_pdf(pdf_path):
    # Extract text from PDF
    text = extract_text(pdf_path)

    # Define regular expressions to extract data
    id_pattern = re.compile(r'ID:(\d+)', re.IGNORECASE)

    # Search for patterns in the text
    id_match = id_pattern.search(text)

    # Create a dictionary to store the extracted data
    extracted_data = {}

    # Extract ID
    if id_match:
        extracted_data["ID"] = id_match.group(1)

    # You can add more patterns and extraction logic for other data fields

    return extracted_data

def pdf_to_json(pdf_path, json_path):
    # Extract data from PDF
    extracted_data = extract_data_from_pdf(pdf_path)

    # Convert the extracted data to JSON format
    json_data = json.dumps(extracted_data, indent=2)

    # Save JSON data to a file
    with open(json_path, 'w') as json_file:
        json_file.write(json_data)

if __name__ == "__main__":
    
    pdf_file_path = "mpdf.pdf"
    json_output_path = "result.json"

    # Convert PDF to JSON
    pdf_to_json(pdf_file_path, json_output_path)
