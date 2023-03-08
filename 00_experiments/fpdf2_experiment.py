"""
https://pypi.org/project/fpdf2/

https://pyfpdf.github.io/fpdf2/Tutorial.html

"""
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        #self.image("../docs/fpdf2-logo.png", 10, 8, 33)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 15)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "Title", border=1, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Position cursor at 1.5 cm from bottom:
        self.set_y(-15)
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "I", 8)
        # Printing page number:
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def main():
    """
    Tutorial for fpdf2
    """
    """
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "B", 16)
    pdf.cell(40, 10, "Hello World!")
    pdf.cell(60, 10, 'Powered by FPDF.', new_x="LMARGIN", new_y="NEXT", align='C')
    pdf.output("tuto1.pdf")
    """
    """
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    for i in range(1, 41):
        pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
    pdf.output("new-tuto2.pdf")
    """
    


if __name__ == "__main__":
    main()
