from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 65, 190, 190)
        self.set_font("Arial", "B", 35)
        self.text(55, 45, "CS50 Shirtificate")

    def footer(self):
        self.set_font("Arial", "B", 35)
        self.set_text_color(255,255,255)
        self.text(45, 140, user_name + " took CS50")


user_name = input("What`s your name? ")
pdf_file = PDF()
pdf_file.add_page()
pdf_file.output("shirtificate.pdf")