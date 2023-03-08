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
    name = input("What's you name? ")
    shirt_for(name)


def shirt_for(name):
    file_name = "shirtificate.pdf"
    image_path = "shirtificate.png"
    title = "CS50 Shirtificate"
    name = name + " took CS50"
    width_a4 = 210
    height_a4 = 297
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image(image_path, x=20, y=60, h=height_a4-100, w=width_a4-40)
    pdf.set_font("helvetica", "B", 30)
    pdf.cell(width_a4, 35, title, align="C")
    pdf.ln(100)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 15)
    pdf.cell(width_a4, 20, name, align="C")
    pdf.output(file_name)


if __name__ == "__main__":
    main()
