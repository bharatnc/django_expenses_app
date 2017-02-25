from django.conf.urls import url
from django.contrib import admin
from .import views



from .views import (
expenses,
expenses_add,
expenses_list,
expenses_edit,
expenses_delete,
expenses_detail,
expenses_export,
export_xls,
export_csv,
expenses_undolist,
expenses_undone,
expenses_deleteall,
)

urlpatterns = [
    url(r'^$', expenses ),
    url(r'^add/$', expenses_add),
    url(r'^list/(?P<id>\d+)/$', expenses_list, name= 'detail'),
    url(r'^(?P<id>\d+)/edit/$', expenses_edit, name= 'edit_expense'),
   	url(r'^list/(?P<id>\d+)$', expenses_list),
    url(r'^delete/(?P<id>\d+)$', expenses_delete ,name= 'delete_expense'),
    url(r'^detail/$', expenses_detail),
    url(r'^export/$', expenses_export),
    url(r'^export_xls$', export_xls),
    url(r'^export_csv$', export_csv),
    url(r'^undolist$', expenses_undolist, name = 'expenses_undo_list'),
    url(r'^undone$', expenses_undone, name = 'expenses_undone'),
    url(r'^deleteall$', expenses_deleteall, name = 'expenses_deleteall'),
]
