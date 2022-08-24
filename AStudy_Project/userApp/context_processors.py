from adminApp.models import category

def add_variable_to_context(request):
    return {
        'catData': category.objects.all()
    }