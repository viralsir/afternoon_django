from django.shortcuts import render,redirect
from .models import course
from  django import forms
from django.views.generic import CreateView,ListView,UpdateView,DeleteView


class NewCourseView(CreateView):
    model = course
    fields = '__all__'
    template_name = 'courses/course_new.html'
    #success_url = 'courses/view'
#model_form.html
#course_form.html

class ListCourseView(ListView):
    model = course
    context_object_name = 'courses'
    template_name = "courses/course_view.html"
    ordering = ['-name']

#model_list.html
#course_list.html

class UpdateCourseView(UpdateView):
    model = course
    fields = '__all__'
    template_name = 'courses/course_new.html'

class DeleteCourseView(DeleteView):
    model = course
    success_url = '/courses/view'

# model_confirm_delete.html

# class NewCourseForm(forms.Form):
#     name=forms.CharField(max_length=34)
#     description=forms.CharField(max_length=34)
#     fees=forms.IntegerField()
#
#
# # Create your views here.
# def course_new(request):
#     form=NewCourseForm()
#     if request.method=='POST':
#         form=NewCourseForm(request.POST)
#         if form.is_valid():
#             new_course=course()
#             new_course.name=form.cleaned_data['name']
#             new_course.description=form.cleaned_data['description']
#             new_course.fees=form.cleaned_data['fees']
#             new_course.save()
#             return redirect('course-view')
#
#     return render(request,"courses/course_new.html",{
#         "form":form
#     })
#
# def course_view(request):
#     return render(request,"courses/course_view.html",{
#         "courses":course.objects.all()
#     })