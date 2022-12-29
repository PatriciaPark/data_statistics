from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

# 400 Error
def bad_request(request) :
    return render(request, "400.html", status=400)
 
# 404 Error
def page_not_found(request) :
    return render(request, "404.html", status=404)
 
# 500 Error
def server_error(request) :
    return render(request, "500.html", status=500)