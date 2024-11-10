from django.shortcuts import render
from first_app.forms import studentForm
def home(request):
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = studentForm()        
    return render(request, 'first_app/home.html', {'form': form})
