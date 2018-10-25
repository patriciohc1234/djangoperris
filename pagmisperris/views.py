from django.shortcuts import render


def post_list(request):
    return render(request, 'pagmisperris/post_list.html', {})