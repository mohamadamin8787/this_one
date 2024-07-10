from services.models import Category


def generai_processor(request):
    context = {
        'category' : Category.objects.filter(status = True)
    }
    return context  