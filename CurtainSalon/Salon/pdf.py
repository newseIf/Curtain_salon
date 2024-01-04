from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus.tables import Table
from Salon.models import Product



def print_pdf():
    data = Product.objects.all()
    dat = [
        ['id', 'name'],
        [i for i in data],
    ]

    filename = '123.pdf'

    pdf = SimpleDocTemplate(
        filename,
        pagesize=letter
    )
    table = Table(dat)

    elems=[]

    elems.append(table)
    pdf.build(elems)
