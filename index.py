from multiprocessing import context
from unicodedata import name
import pandas as pd
from docxtpl import DocxTemplate
from datetime import datetime
today = datetime.today().strftime("%d %b %y")
df = pd.read_csv('contact.csv')
doc = DocxTemplate("template.docx")
my_context = {
    'today_date': today,
    'my_phone': "5556632145",
    'my_email': "demoemail@myemail.com",
    'my_address': "Kolkata,West Bengal,India"
}
for index, row in df.iterrows():
    context = {
        'hiring_manager_name': row['name'],
        'address': row['address'],
        'phone_number': row['phone_number'],
        'email': row['email'],
        'job_position': row['job']
    }
    context.update(my_context)
    doc.render(context)
    doc.save(f"generated_doc{index+1}.docx")
    print(f"generatedpdf{index+1}")