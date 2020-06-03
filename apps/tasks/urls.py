from django.urls import path, re_path
from .views import *

app_name = 'tasks'

urlpatterns = [
    path('', TasksView.as_view(), name = 'all_tasks'),
    path('remove/', AjaxRemove.as_view(), name='remove'),
    path('complete/', AjaxComplete.as_view(), name='complete'),
    path('undo-complete/', AjaxUndoComplete.as_view(), name='undocomplete'),
    # re_path(r'^remove/task/(?P<pk>\d+)/$', Remove.as_view(), name='task_remove'),
    # re_path(r'^complete/task/(?P<pk>\d+)/$', Complete.as_view(), name='task_complete'),
]
