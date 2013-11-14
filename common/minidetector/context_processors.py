def is_mobile(request):
    return {
        'is_mobile': request.mobile or request.GET.get('mobile') == '1'
    }
