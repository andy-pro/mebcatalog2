import fnmatch
from mebcatalog import render_404, mebcatalog

def admin(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['Admin:']

def index(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['Index file:']

def application(environ, start_response):
    routes = [('admin*',      admin),
              ('',            mebcatalog),
              ('index',       index),
              ('mebcatalog*', mebcatalog),]
    path = (environ['PATH_INFO']).strip('/')
    for pathmask, app in routes:
        if fnmatch.fnmatch(path, pathmask):
            return app(environ, start_response)
    return render_404(environ, start_response)

#from paste.exceptions.errormiddleware import ErrorMiddleware
#application = ErrorMiddleware(application, debug=True)
#------------------------Extended debug information-------------------------------------------------
#from paste.evalexception.middleware import EvalException
#application = EvalException(application)