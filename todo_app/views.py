from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Students
def navigate(request):
	return render(request,'form.html')
def submitaction(request):
	s=Students()
	s.firstname=request.POST['fname']
	s.lastname= request.POST['lname']
	s.email=request.POST['email']
	s.save()
	p=Students.objects.all()
	return render(request,'indexx.html',{'obj':p})
def delete(request,ident):
	delstu  = Students.objects.get(id=ident)
	delstu.delete()
	p=Students.objects.all()
	return JsonResponse({'id': id})

def bridge(request):
	redirect('http://localhost:8000/delete')
	delete()

def update(request,ident):
	getupdate  = Students.objects.get(id=ident)
	return render(request,'update.html',{'obj':getupdate})
def putupdatedval(request,ident):
	p=Students.objects.all()
	upobj = Students.objects.get(id=ident)
	upobj.firstname=request.POST['fname']
	upobj.lastname= request.POST['lname']
	upobj.email=request.POST['email']
	upobj.save()
	return render(request,'indexx.html',{'obj':p})



# from django.shortcuts import render, redirect
# from .models import Reader
# # Create your views here.
# def index(request):
# 	reader = Reader.objects.all()
# 	# for x in reader:
# 	# 	print(x.id)
# 	return render(request, 'index.html', {'reader': reader})

# def addNewReader(request):
# 	return render(request, 'add_new_reader.html')

# def createNewReader(request):
# 	reader = Reader()
# 	reader.enrollment_number = request.POST["enrollment_id"]
# 	reader.student_name = request.POST["student_name"]
# 	reader.mobile = request.POST["mobile"]
# 	reader.department = request.POST["department"]
# 	reader.academic_year = request.POST["academic_year"]
# 	reader.books_issued = request.POST["books_issued"]
# 	reader.date_of_return = request.POST["date_of_return"]
# 	reader.comments = request.POST["comments"]
# 	reader.save()
# 	return redirect('/')
# def destroyReader(request, ident):
# 	reader = Reader.objects.get(id=ident)
# 	reader.delete()
# 	return redirect('/')