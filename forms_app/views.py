from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomForm, FormField

def home(request):
    return render(request, 'forms_app/home.html')

def form_list(request):
    forms = CustomForm.objects.all()
    return render(request, 'forms_app/form_list.html', {'forms': forms})

def form_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if CustomForm.objects.filter(name=name).exists():
            return render(request, 'forms_app/form_create.html', {'error': 'Form name already exists.'})
        form = CustomForm.objects.create(name=name)
        return redirect('form_field_add', form_id=form.id)
    return render(request, 'forms_app/form_create.html')

def form_field_add(request, form_id):
    form = get_object_or_404(CustomForm, pk=form_id)
    if request.method == 'POST':
        label = request.POST.get('label')
        field_type = request.POST.get('field_type')
        options = request.POST.get('options', '')
        FormField.objects.create(form=form, label=label, field_type=field_type, options=options)
        return redirect('form_field_add', form_id=form.id)
    return render(request, 'forms_app/form_field_add.html', {'form': form})

def form_render(request, pk):
    form = CustomForm.objects.get(pk=pk)
    fields = form.fields.all()

    # Prepare field options by splitting the options string
    for field in fields:
        if field.options:
            field.options = field.options.split(',')

    if request.method == 'POST':
        responses = {field.label: request.POST.get(field.label) for field in fields}
        return render(request, 'forms_app/form_response.html', {'form': form, 'responses': responses})

    return render(request, 'forms_app/form_render.html', {'form': form, 'fields': fields})

