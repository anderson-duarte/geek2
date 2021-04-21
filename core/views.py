from django.shortcuts import render
from .models import Servico, Funcionario, Recurso


# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        p = Recurso.objects.filter()[:3]
        context['recursos'] = p
        p2 = Recurso.objects.filter()[3:]
        context['recursos1'] = p2
        return context
