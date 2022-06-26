import tabula
import pandas as pd

pdf_path = r"C:\Users\pandas\Pictures\Certificates\World Countries and Capital & Languages.pdf"
df = tabula.read_pdf(pdf_path, pages = "all", stream = True)