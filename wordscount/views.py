from django.shortcuts import render

def index(request):
	return render(request, 'index.html',)

def count(request):
    sentence = request.GET['message']
    full_words = sentence.split()
    return render(request,'count.html',{'sentence' : sentence,
    	'result' : len(full_words)})

