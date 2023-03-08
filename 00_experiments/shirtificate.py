"""
CS50. Problem Set 8. CS50 Shirtificate

In a file called shirtificate.py, implement a program that
prompts the user for their name and outputs, using fpdf2,
a CS50 shirtificate in a file called shirtificate.pdf
similar to this one for John Harvard, with these specifications:

The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should “CS50 Shirtificate” as text, centered horizontally.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text.
"""
from fpdf import FPDF


def main():
    shirt_for()


def shirt_for():
    file_name = "1.pdf"
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    width_a4, height_a4 = pdf.epw, pdf.eph
    print(width_a4, height_a4)
    pdf.add_page()
    pdf.set_font("helvetica", "B", 30)
    pdf.cell(w=width_a4, h=35, txt="text1", align="C")
    print(pdf.get_x(),pdf.get_y())
    pdf.set_y(120)
    print(pdf.get_x(),pdf.get_y())
    pdf.cell(w=width_a4, h=20, txt="text2", align="C")
    print(pdf.get_x(),pdf.get_y())
    pdf.output(file_name)


if __name__ == "__main__":
    main()
