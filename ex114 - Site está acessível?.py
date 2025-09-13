import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br/')
except urllib.error.URLError:
    print('Deu problema')
else:
    print('TUDO OK')