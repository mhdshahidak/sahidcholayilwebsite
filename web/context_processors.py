import datetime


def main_context(request):
    datetime.date.today()

    return {
        'domain' : request.META['HTTP_HOST'],
    }
