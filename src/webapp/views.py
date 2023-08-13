from django.shortcuts import render

def not_found_view(request, exception):
    return render(request, 'webapp/pages/404-error.html', status=404)
