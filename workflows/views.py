from django.shortcuts import render
from .forms import GeneratedWorkflowForm

# Create your views here.

def workflows(request):
    """
    A view to render the workflow page.
    """
    if request.method == "POST":
        form = GeneratedWorkflowForm(request.POST)
        if form.is_valid():
            form = GeneratedWorkflowForm(request.POST)
        else:
            form = GeneratedWorkflowForm()

    return render(
        request,
        'workflows/workflows.html',
        {
            'form': form,
        },
    )

