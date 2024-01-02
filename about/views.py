from django.shortcuts import render

# Create your views here.



def about_us(request):

    return render(request, 'about/about-us.html')



def terms_of_use(request):

    return render(request, 'about/terms-of-use.html')


def exchange_refund_policy(request):
    return render(request, 'about/exchange-refund-policy.html')



def bug_bounty_program(request):
    return render(request, 'about/bug-bounty-program.html')


def privacy_statement(request):
    return render(request , 'about/privacy-statement.html')