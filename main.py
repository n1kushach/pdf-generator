import pandas as pd
from fpdf import FPDF

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    pages = row["Pages"]
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(139, 143, 142)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 22, 200, 22)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(pages - 1):
        pdf.add_page()
        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("Output.pdf")
