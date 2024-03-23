from django.shortcuts import render

def page(request):
    return render(
        request=request,
        template_name='page.html',
        context={
            "name": "Home",
            "person": ["Mira", "Dima"],
        },
    )
