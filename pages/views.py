from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pages.models import Contact


# from django.views import View


# Create your views here.
# class home(View):
#     def get(self, request):
#         return HttpResponse("<h1> Welcome to my django home page.</h1>")
#
#     def post(self, request):
#         pass


def home(request):
    return render(request, 'index.html', {'title': 'Home Page'})


# class contact(View):
#     def get(self, request):
#         return HttpResponse("<h1> Contact Us </h1>")
#
#     def post(self, request):
#         pass


def contact(request):
    if request.method == 'GET' and request.GET.get('method') == 'delete' and request.GET.get('id'):
        rec = Contact.objects.filter(id = request.GET.get('id'))
        rec.delete()

    if request.method == 'GET' and request.GET.get('method') == 'edit' and request.GET.get('id'):
        rec = Contact.objects.filter(id = request.GET.get('id')).get()
        return render(request, 'edit.html', {'page_title': 'Edit Page', 'row': rec})

    if request.method == 'POST':
        if request.GET.get('method') == 'edit':
            rec = Contact.objects.filter(id = request.GET.get('id'))
            rec.update(
                name = request.POST['name'],
                email = request.POST['email'],
                address = request.POST['address'],
                city = request.POST['city'],
                zipcode = request.POST['zipcode'],
            )
            return HttpResponseRedirect('/contact')
        else:
            data = Contact(
                name = request.POST['name'],
                email = request.POST['email'],
                address = request.POST['address'],
                city = request.POST['city'],
                zipcode = request.POST['zipcode'],
            )
            data.save()
    cnt = Contact.objects.all()
    return render(request, 'contact.html', {'title': 'Contact Page', 'rows': cnt})


def about(request):
    return render(request, 'about.html', {'title': 'About Page'})


def member(request, cat_id, mem_id):
    return HttpResponse("<h1> Team Member ID: {} from Category ID: {}</h1>".format(mem_id, cat_id))


def team(request):
    if request.method == 'GET' and 'cat_id' in request.GET and 'mem_id' in request.GET:
        return HttpResponse("<h1> Team Member ID: {} from Category ID: {}</h1>".format(request.GET.get('mem_id'),
                                                                                       request.GET.get('cat_id')))
    else:
        return HttpResponse("<h1>Team Members List</h1>")
