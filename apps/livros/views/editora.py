from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from apps.livros.models import Editora
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages

class EditoraCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Editora
    fields = '__all__'
    success_message = 'Editora cadastrada com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_editoras")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Editoras - Biblioteca'
        context['descricao'] = 'Cadastro de Editora'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class EditoraUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Editora
    fields = '__all__'
    success_message = 'Editora atualizada com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("listar_autores")

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Editoras - Biblioteca'
        context['descricao'] = 'Editar Editora'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class EditoraDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Editora
    success_message = 'Editora excluída com sucesso!'
    error_message = 'Editora não pode ser excluída!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar_editoras")

    def get_context_data(self, **kwargs):
        context = super(DeleteView, self).get_context_data(**kwargs)
        context['titulo'] = 'Editoras - Biblioteca'
        return context

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(EditoraDelete, self).delete(request, *args, **kwargs)


class EditoraList(ListView):
    model = Editora
    template_name = "cadastros/listas/editoras.html"

