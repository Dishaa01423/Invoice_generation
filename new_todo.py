from fpdf import FPDF
import glob
from pathlib import Path

# Created the list of all the filepaths.
filepaths = glob.glob("files/*.txt")
# create one pdf file.
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each file text.
for filepath in filepaths:
    # Add a page to the PDF document for each text file.
    pdf.add_page()

    # Get the filename without extension and convert it  to title case.
    filename = Path(filepath).stem
    name = filename.title()

    # Add the name to the PDF.
    pdf.set_font(family="Times", size=30, style="B")
    pdf.cell(w=50, h=8, txt=name,ln=1)

    # Using multi_cell for writing multiple text.
    with open(filepath,"r") as file:
        content = file.read()
    # Add the text file content to the PDF.
    pdf.set_font(family="Times", size=15)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("output.pdf")