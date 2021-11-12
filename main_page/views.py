from django.shortcuts import redirect, render
from .models import MainModel
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def MainPageView(request):

    context ={'context':'Purpose: All Employee are required to fill the below form during their long-planned leave and in case of resignation to ensure the smooth running of operations in their department during their absence from duty.'}
    
    return render(request, 'pdf.html', context)


def PDFPageView(request):

    if request.method == 'POST':
        from_view_name = request.POST['from_name']
        from_view_designation = request.POST['from_designation']
        to_view_name = request.POST['to_name']
        to_view_designation = request.POST['to_designation']
        inCharge_view_name = request.POST['inCharge_name']
        inCharge_view_designation = request.POST['inCharge_designation']
        team_view_name = request.POST['teamLead_name']
        team_view_designation = request.POST['teamLead_designation']
        employee_view_name = request.POST['employee_name']
        employee_view_designation = request.POST['employee_designation']
        employee_view_responsibilites = request.POST['employee_responsibilities']

        MainModel.objects.create(
            fromName = from_view_name,
            fromDesignation = from_view_designation,
            toName = to_view_name,
            toDesignation = to_view_designation,
            inChargeName = inCharge_view_name,
            inChargeDesignation = inCharge_view_designation,
            teamLeadName = team_view_name,
            teamLeadDesignation = team_view_designation,
            employeeName = employee_view_name,
            employeeDesignation = employee_view_designation,
            employeeResponsibilities = employee_view_responsibilites
            ).save()
    return redirect(render_pdf_view)

    
def render_pdf_view(request):
    data = MainModel.objects.all().order_by('-id')[:1]
    template_path = 'pdf2.html'
    context = {'data': data[0],
               'info':'Purpose: All Employee are required to fill the below form during their long-planned leave and in case of resignation to ensure the smooth running of operations in their department during their absence from duty.'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

        



    