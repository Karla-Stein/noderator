from django.shortcuts import render

# Create your views here.

def workflows(request):
    """
    A view to render the workflow page.
    """
    return render(
        request,
        'workflows/workflows.html'
    )

