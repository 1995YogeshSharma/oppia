from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/header_css_libs.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_DEV_MODE = resolve('DEV_MODE')
    pass
    yield u'<link rel="stylesheet" type="text/css" media="screen"\n      href="https://fonts.googleapis.com/css?family=Capriola|Rubik|Roboto|Material+Icons|Open+Sans:400,600">\n'
    if (not (undefined(name='DEV_MODE') if l_0_DEV_MODE is missing else l_0_DEV_MODE)):
        pass
        yield u'\n  <link rel="stylesheet" type="text/css" media="screen"\n        href="/third_party/generated/css/third_party.min.css">\n'
    else:
        pass
        yield u'\n  <link rel="stylesheet" type="text/css" media="screen"\n        href="/third_party/generated/css/third_party.css">\n'
    yield u'\n<link rel="stylesheet" type="text/css" media="screen"\n      href="/templates/dev/head/css/oppia.css">'

blocks = {}
debug_info = '3=12'