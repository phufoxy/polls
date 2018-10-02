from django.shortcuts import render,HttpResponse,redirect
from .models import Choise, Question
# Create your views here.
def index(request):
    name1='abc'
    questions1 = Question.objects.order_by('-id')
    # hni
    # date
    #sgjkjwrhnjghrfnjllfnfk
    #djkfhkd
    context1 = {
        'name':name1,
        'questions':questions1
    }
    return render(request,'index.html',context1)

def index_details(request,id):
    questions = Question.objects.get(pk=id)

    context ={
        'question':questions
    }
    return render(request,'edit.html',context)

def index_newdata(request):
    return render(request,'newdata.html')

def create_view(request):
    text = request.GET['text']
    pub_date= request.GET['pub_date']
    question = Question(question_text=text,pub_date=pub_date)
    question.save()
    return redirect('index')

def index_update(request,id):
    questions = Question.objects.get(pk=id)

    context ={
        'question':questions
    }
    return  render(request,'update.html',context)

def delete_view(request,id):
    question = Question.objects.get(pk=id)
    question.delete()
    return redirect('index')
    
def update_view(request,id):
    text = request.GET['text']

    question = Question.objects.get(pk=id)
    question.question_text = text
    # question.pub_date = pub_date
    question.save()
    return redirect('index')