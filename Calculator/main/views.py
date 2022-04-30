from django.shortcuts import render
from . import operation
# Create your views here.
def index(request):

    res = ''
    try :
        if request.method == 'POST':

            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')

            if opr == '+':
                res = operation.adding(n1, n2)
            elif opr == '-':
                res = operation.sub(n1,n2)
            elif opr=='*':
                res = operation.mul(n1, n2)
            elif opr=='/':
                res = operation.div(n1 ,n2)
            else:
                res = "Invalid"
            
        

    except:
        res = 'Invalid'

    print(res)

    return render(request, 'index.html', {'res':res})