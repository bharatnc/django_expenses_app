from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.encoding import smart_str
from .models import Expenses
from .forms import ExpensesForm
import csv, xlwt, djqscsv

def expenses(request):
  return HttpResponse("Home")

def expenses_add(request):
  form = ExpensesForm(request.POST or None)

  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    return HttpResponseRedirect(instance.get_absolute_url())
  context = {
    "form": form,

  }
  return render(request, "expenses_templates/add_expenses.html", context)


def expenses_list(request, id):
  instance = get_object_or_404(Expenses, id=id)
  context = {"item": instance.item,
             "instance": instance,
             }
  return render(request, "expenses_templates/edited_view.html", context)


def expenses_detail(request):
  querylist = Expenses.objects.filter(deleted="").order_by("-date")
  context = {"querylist": querylist
             }
  return render(request, "expenses_templates/detail_expenses.html", context)


def expenses_edit(request, id=None):
  instance = get_object_or_404(Expenses, id=id)
  form = ExpensesForm(request.POST or None, instance=instance)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    return HttpResponseRedirect(instance.get_absolute_url())
  context = {
    "item": instance.item,
    "instance": instance,
    "form": form,}
  return render(request, "expenses_templates/edit_expenses.html", context)


def expenses_delete(request, id=None):
  instance = get_object_or_404(Expenses, id=id)
  setattr(instance, "deleted", "true")
  instance.save()
  messages.success(request, "successfully deleted")
  return redirect("/expenses/detail")


def expenses_undone(self):
  Expenses.objects.filter(deleted="true").update(deleted="")
  return redirect("/expenses/detail")


def expenses_deleteall(self):
  Expenses.objects.filter(deleted="true").delete()
  return redirect("/expenses/detail")


def expenses_export(request):
  return render(request, "expenses_templates/export_expenses.html")


def export_xls(request):
  response = HttpResponse(content_type='text/xls')
  response['Content-Disposition'] = 'attachment; filename="somefilename.xls"'
  writer = csv.writer(response)
  writer.writerow([
    smart_str(u"item"),
    smart_str(u"cost"),
  ])
  querylist = Expenses.objects.all().order_by("-date")
  for obj in querylist:
    writer.writerow([
      smart_str(obj.item),
      smart_str(obj.cost),
    ])

    return response

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow([
      smart_str(u"item"),
      smart_str(u"cost"),
    ])
    querylist = Expenses.objects.all().order_by("-date")
    for obj in querylist:
      writer.writerow([
        smart_str(obj.item),
        smart_str(obj.cost),
      ])
    return response


def expenses_undolist(request):
  querylistundo = Expenses.objects.filter(deleted="true").order_by("-date")
  context = {"querylistundo": querylistundo
             }
  return render(request, "expenses_templates/undolist_expenses.html", context)

