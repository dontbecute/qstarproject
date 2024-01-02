from django.shortcuts import render

# Create your views here.
def custom_404(request, exception):
    return render(request, '404.html', status=404)



def you_dont_have_permission(request):
    return render(request, '403.html', status=403)