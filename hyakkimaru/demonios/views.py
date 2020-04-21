from django.shortcuts import render, redirect
from .models import demonio
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,'index.html')

def lista_demonios(request):
    demonios = demonio.objects.all()
    return render(request,'demonios/lista_demonios.html',{'demonios':demonios})

def demonio_print(self, pk=None):
    import io
    from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import Table

    response = HttpResponse(content_type='application/pdf')
    buff = io.BytesIO()
    doc = SimpleDocTemplate(buff,
                            pagesize=letter,
                            rightMargin=40,
                            leftMargin=40,
                            topMargin=60,
                            bottomMargin=18,
                            )
    demonios = []
    styles = getSampleStyleSheet()
    header = Paragraph("Listado de Demonios", styles['Heading1'])
    demonios.append(header)
    headings = ('Id', 'nombre', 'partecuerpo', 'ubicacion')
    if not pk:
        todosdemonios = [(d.id, d.nombre, d.partecuerpo, d.ubicacion)
                           for d in demonio.objects.all().order_by('pk')]
    else:
        todosdemonios = [(d.id, d.nombre, d.partecuerpo, d.ubicacion)
                           for d in demonio.objects.filter(id=pk)]
    
    t = Table([headings] + todosdemonios)
    t.setStyle(TableStyle(
        [
            ('GRID', (0, 0), (3, -1), 1, colors.dodgerblue),
            ('LINEBELOW', (0, 0), (-1, 0), 2, colors.darkblue),
            ('BACKGROUND', (0, 0), (-1, 0), colors.dodgerblue)
        ]
    ))

    demonios.append(t)
    doc.build(demonios)
    response.write(buff.getvalue())
    buff.close()
    return response