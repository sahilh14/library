import json
import MySQLdb
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hello(request):
    #import pdb; pdb.set_trace()
    # print request.GET
    # print dir(request)
    # print type(request)
    db = MySQLdb.connect(user='root', db='library', passwd='Hp@4672351', host='localhost')
    cur = db.cursor()
    cur.execute('Select title from books order by title')
    names = [row[0] for row in cur.fetchall()]
    db.close()
    l = list()
    for key,value in request.META.items():
        l.append((key, value))
    return render(request, 'hello.html', {'names': l})
    # return render(request, 'hello.html', {'names': names})
    # return HttpResponse('%s' % names)
    # data = {'data': names}
    # return HttpResponse(names)
    # return HttpResponse(json.dumps(data))
    # return JsonResponse({'data': names})
