from PyPDF2 import PdfFileWriter, PdfFileReader

def add_encrypt(input_pdf, output_pdf, password):
    pdf_writter = PdfFileWriter()
    pdf_reader = PdfFileReader(input_pdf)

    for page in range(pdf_reader.getNumPages()):
        pdf_writter.addPage(pdf_reader.getPage(page))

    pdf_writter.encrypt(user_pwd=password, owner_pwd=None, use_128bit=True)

    with open(output_pdf, 'wb') as fh:
        pdf_writter.write(fh)


if __name__ == '__main__':
    add_encrypt(input_pdf='splunk-product-data-sheet.pdf', output_pdf='encrypt.pdf', password='123')
