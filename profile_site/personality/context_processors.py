from personality.models import Bio


def bio_processor(request):

    biograpy = Bio.objects.get(id=1)
    return {'bio': biograpy}
