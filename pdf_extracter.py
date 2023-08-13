from PyPDF2 import PdfReader, PdfWriter
import uuid

keyword = input("Enter the keyword to search: ")
pdf_file_name = input("Enter the PDF file name: ")
try:
    reader = PdfReader(pdf_file_name)
    number_of_pages = len(reader.pages)
    pages_with_keyword = []
    for page_number in range(number_of_pages):
        current_page = reader.pages[page_number]
        if keyword in current_page.extract_text():
            print("found "+ keyword+ " in page "+ str(page_number))
            pages_with_keyword.append(current_page)

    if len(pages_with_keyword)>0:
        output_pdf = PdfWriter()
        for page in pages_with_keyword:
            output_pdf.add_page(page)

        output_path = "output_with_keyword" + str(uuid.uuid4())+".pdf"
        with open(output_path, "wb") as output_file:
            output_pdf.write(output_file)
        print("Extracted pages with keyword saved as", output_path)
    else:
        print("No page with keyword "+ keyword+ "found.")
except:
    print("Could not read/write the file name entered. Make sure to add the file type. For example: XYZ.pdf")
    

