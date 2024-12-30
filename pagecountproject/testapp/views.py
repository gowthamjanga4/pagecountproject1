from django.shortcuts import render


# Create your views here
def page_count_view(request):
    print('cookies from the client:', request.COOKIES)
    count = int(request.COOKIES.get('count', 0))
    count = count + 1
    resp = render(request, 'testapp/count.html', {'count': count})
    resp.set_cookie('count', count)
    return resp
