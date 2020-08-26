import pandas as pd
import pdfkit

"""
Make it so that the html being made with the first function also
is the same html being
"""
path = r"C:\Users\Hank\Documents\Random Python Scripts\help1.html"
pdf_path = r"C:\Users\Hank\Documents\Random Python Scripts\pdfkitTest.pdf"

# Function that takes a csv and puts it into a html that can be read
def csv_to_html():
    # Path to the CSV
    csv_path = r"C:\Users\Hank\Documents\testing.csv"
    # Opens the csv as a database
    df = pd.read_csv(csv_path)
    # Writes the csv to an html
    html = df.to_html()
    # Opens the file and writes the html to it
    with open(path, "w") as csv:
        csv.write(html)
        csv.close()


# csv_to_html()

# This will convert the html to markdown because it can then be converted to a pdf
def html_to_md():
    import html2md

    html = open(path, "r").read()
    md = html2md.convert(html)
    print(html)
    md_path = r"C:\Users\Hank\Documents\Random Python Scripts\Test.md"
    with open(md_path, "w") as mrd:
        mrd.write(md)
        mrd.close()


# html_to_md()

# This will convert the html to pdf, hopefully
def html_to_pdf():
    # This needs to be on the computer running it or the program wont run
    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    )
    pdfkit.from_file(path, pdf_path, configuration=config)


# html_to_pdf()


def main():
    csv_to_html()
    html_to_md()
    html_to_pdf()


# main()
def test_func():
    list = []
    x = 13
    while x < 20:
        x += 1
        list.append(x)
        print(list)
    bl = "function is working in emacs "
    print("I am using this to test if the blacken " + bl, "\n")


# test_func()

# =======================================================================
# Converts a CSV to XLSX(Excel) files.
# pip install openpyxl
# from openpyxl import Workbook
# import csv

# csv_path = r"C:\Users\Hank\Documents\Testing.csv"
# wb = Workbook()
# ws = wb.active
# with open(csv_path, "r") as f:
#    for row in csv.reader(f):
#        ws.append(row)

# xlsx_path = r"C:\Users\Hank\Documents\Testing.xlsx"
# wb.save(xlsx_path)
# This is currently working
# ======================================================================
# Turning it into a dfunction, we get:
def csv_2_xlsx():
    from openpyxl import Workbook
    import csv

    csv_path = r"C:\Users\Hank\Documents\Testing.csv"
    wb = Workbook()
    ws = wb.active
    with open(csv_path, "r") as f:
        for row in csv.reader(f):
            ws.append(row)
    xlsx_path = r"C:\Users\Hank\Documents\Testing1.xlsx"
    wb.save(xlsx_path)
    print(f"Your csv has been converted to an xlsx and stored {xlsx_path}")


csv_2_xlsx()
