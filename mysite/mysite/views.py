from django.http import HttpResponse


def index(request):
    if request.user.is_authenticated:
        return HttpResponse(
            '''
            <p>Welcome to <a href="https://djangocas.dev">django-cas-ng</a>.</p><p>You logged in as <strong>{}</strong>.</p><p><a href="/accounts/logout">Logout</a></p>
            <iframe height="500" width="800" src="http://10.200.0.43:8502" title="W3Schools Free Online Web Tutorials"></iframe>
            '''.format(request.user)
        )
    else:
        return HttpResponse('<p>Welcome to <a href="https://djangocas.dev">django-cas-ng</a>.</p><p><a href="/accounts/login">Login</a></p>')
