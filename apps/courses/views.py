from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course, Description


# Create your views here.
def index(request):

	courses = Course.objects.all()
	print courses.query
	context = {'course_listing': courses}
	return render(request, 'courses/index.html', context)

def add(request):
	if request.method == "POST":
		if len(request.POST['course_name']) < 1:
			messages.error(request, 'Course\'s Name cannot be empty!')
    	if len(request.POST['description']) < 1:
    		messages.error(request, 'Course\'s Description cannot be empty!')
    	else:
    		new_description = Description.objects.create(name=request.POST['description'])
    		Course.objects.create(name=request.POST['course_name'],description=new_description)
    		
    		print(Course.objects.raw("SELECT * from courses_course"))
    		print(Course._meta.db_table)
	return redirect('/')

def remove_confirm(request, course_id):
	if request.method == "GET":
		del_course = Course.objects.get(description_id=course_id)
		context = {'del_course': del_course}
		return render(request, 'courses/delete.html', context)

		#Entry.objects.filter(pub_date__year=2005).delete()

def remove_course(request, course_id):
	if request.method == "GET":
		Course.objects.filter(description_id=course_id).delete()
		return redirect('/')
			
			




