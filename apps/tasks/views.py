from django.urls import reverse_lazy
from django.views import generic
from .models import Task
from django.shortcuts import get_object_or_404
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime, pytz
from django.http import JsonResponse
# Create your views here.

class TasksView(LoginRequiredMixin, generic.CreateView):
    model = Task  
    template_name = 'tasks/task_list.html'
    success_url = reverse_lazy('tasks:items')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        # TODO: seting the due_datetime from the form inputs
        due_date = self.request.POST.get('due_date') #? 1st get the two inputs(date and time)
        due_time = self.request.POST.get('due_time')
        due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d') #?convert due_date into datetime.datetime object 
        due_time = datetime.datetime.strptime(due_time, '%H:%M').time() #?convert due_time into datetime.time object
        due_datetime = due_date + datetime.timedelta(hours=due_time.hour, minutes=due_time.minute) #? add both date and time
        #// form.instance.due_datetime = pytz.utc.localize(due_datetime) #?making the due_datetime "timezone aware" 
        form.instance.due_datetime = due_datetime.replace(tzinfo=datetime.timezone.utc) #?making the due_datetime "timezone aware" 
        # TODO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        return super().form_valid(form)

    def form_invalid(self, form):
        print("INVALID")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_time'] = datetime.datetime.now().replace(tzinfo=datetime.timezone.utc)
        context['page_name'] = "My Tasks"
        return context

#TODO: handles task removal(deletes them from database)
class AjaxRemove(generic.View):
    def get(self, request):
        task_pk = request.GET.get('task_pk', None)
        Task.objects.get(pk=task_pk).delete()
        data ={
            'deleted': True
        }
        return JsonResponse(data)


class AjaxComplete(generic.View):
    def get(self, request):
        task_pk = int(request.GET.get('task_pk', None))
        task = Task.objects.filter(pk=task_pk)
        task.update(completed=True)
        task.update(completed_on=datetime.datetime.now())
        data ={
            'completed': True
        }
        return JsonResponse(data)


class AjaxUndoComplete(generic.View):
    pass


# class Remove(generic.RedirectView):
#     def get(self, request, *args, **kwargs):
#         item = get_object_or_404(Task, pk=self.kwargs.get('pk'))
#         item.delete()
#         return super().get(request, *args, **kwargs)
    
#     def get_redirect_url(self, *args, **kwargs):
#         return reverse_lazy('tasks:items')


# class Complete(generic.RedirectView):
#     def get(self, request, *args, **kwargs):
#         task = Task.objects.filter(pk=self.kwargs.get('pk'))
#         task.update(completed=True)
#         task.update(completed_on=datetime.datetime.now())
#         #// task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
#         #// task.complete()
#         return super().get(request, *args, **kwargs)
    
#     def get_redirect_url(self, *args, **kwargs):
#         return reverse_lazy('tasks:items')


# class CompletedTasks(LoginRequiredMixin, generic.TemplateView):    
#     template_name = 'tasks/completed_tasks.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['page_name'] = "Completed Tasks"
#         return context
