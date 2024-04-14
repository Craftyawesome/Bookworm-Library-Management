from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Document
from .forms import DocumentForm
import os


class HomePageView(LoginRequiredMixin, CreateView, ListView):
    model = Document
    template_name = "print_list.html"
    form_class = DocumentForm
    success_url = reverse_lazy("print")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@require_POST
def delete_document(request, pk):
    try:
        document = Document.objects.get(pk=pk)
        if request.user.is_staff or document.user == request.user:
            file_path = document.cover.path
            document.delete()
            if os.path.exists(file_path):
                os.remove(file_path)
            return JsonResponse({'success': True})
    except Document.DoesNotExist:
        pass
    return JsonResponse({'success': False})
