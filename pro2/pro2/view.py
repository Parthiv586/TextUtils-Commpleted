
from django.shortcuts import  render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')
def analyze(request):
#take text
    a = request.POST.get('text', 'default')
# check on checkboxes
    removepunc = request.POST.get('check','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremove = request.POST.get('spaceremove','off')
    charcount = request.POST.get('charcount','off')
    punc = '''/\!()-[]}{;:'",<>./?@#$%^&*_~'''
    purpose= ""
    c = ''
    cap = ''
# removepunc is open
    if (removepunc == "on"):
        for char in a:
            if char not in punc:
                c = c + char 
        purpose = purpose + 'Remove Punctuations'
        # return render(request,'analyze.html',p)
        a = c
# capitalize is on
    if (fullcaps=="on"):
        cap = cap + a.upper()
        # p2 = {'purpose' : 'Change to Uppercase','analyzed_text' : cap }
        # return render(request, 'analyze.html', p2)
        purpose = purpose + "Capitalize Text"
        a = cap
# newlineremove is on 
    if (newlineremove == 'on'):
        analyzed_text = ''
        for char in a:
            if char != "\n" and char != "\r":
                analyzed_text = analyzed_text + char
                
        # p2 = {'purpose' : 'Removed New Lines','analyzed_text' : analyzed_text }
        # return render(request,'analyze.html',p2)
        purpose = purpose+"New Line Remove"
        a = analyzed_text
# spaceremove is on
    if (spaceremove=="on"):
        an = ''
        i = 0
        for i in range(0,len(a)):
            if not(a[i]==" " and a[i+1]==" "):
                an = an + a[i]
            i = i+1
        # p2 = {'purpose' : 'Extra Space Removed','analyzed_text' : analyzed_text }
        # return render(request, 'analyze.html', p2)
        purpose = purpose+"Space Remove"
        a = an

# char_counter is on
    if (charcount=="on"):
        # p2 = {'purpose' : 'Characters are:','analyzed_text' : len(a) }
        # return render(request, 'analyze.html', p2)
        purpose = purpose + str(len(a))+'Characters are in text.'
        

# all checkbox off
    if(removepunc!="on" and charcount!="on" and newlineremove!="on" and spaceremove!="on"):
        return HttpResponse("Error!!")
    p = {'purpose' : purpose,'analyzed_text' : a}
    return render(request,'analyze.html',p)
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')