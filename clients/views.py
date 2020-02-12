import xlwt
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Client
from django.urls import reverse_lazy
from .filters import ClientsFilter
from django.http import HttpResponse


def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="clients.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Clients')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['First name', 'Last name', 'Date of birth', 'Age']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = Client.get_deferred_fields(Client)
    #rows = Client.objects.all().values_list('first', 'last', 'birth', 'age')
    # rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


class ClientListView(ListView):
    model = Client
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = ClientsFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'


class AddClientView(CreateView):
    model = Client
    template_name = 'add_client.html'
    fields = '__all__'


class EditClientView(UpdateView):
    model = Client
    template_name = 'edit_client.html'
    fields = '__all__'


class DeleteClientView(DeleteView):
    model = Client
    template_name = 'delete_client.html'
    success_url = reverse_lazy('home')
