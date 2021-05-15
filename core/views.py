from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import ContatoForm
from .models import Servico, Funcionario, Recurso
from django.contrib import messages

# Create your views here.
from django.views.generic import FormView


class IndexView(FormView):
    template_name = 'core/index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('core:index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        p = Recurso.objects.filter()[:3]
        context['recursos'] = p
        p2 = Recurso.objects.filter()[3:]
        context['recursos1'] = p2
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
