from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/header_css_libs.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_DEV_MODE = resolve('DEV_MODE')
    l_0_TEMPLATE_DIR_PREFIX = resolve('TEMPLATE_DIR_PREFIX')
    l_0_get_static_resource_url = resolve('get_static_resource_url')
    pass
    yield u'<link rel="stylesheet" type="text/css" media="screen"\n      href="https://fonts.googleapis.com/css?family=Capriola|Rubik|Roboto|Material+Icons|Open+Sans:400,600">\n'
    if (not (undefined(name='DEV_MODE') if l_0_DEV_MODE is missing else l_0_DEV_MODE)):
        pass
        yield u'\n  <link rel="stylesheet" type="text/css" media="screen"\n      href="%s">\n' % (
            escape(context.call((undefined(name='get_static_resource_url') if l_0_get_static_resource_url is missing else l_0_get_static_resource_url), '/third_party/generated/css/third_party.min.css')), 
        )
    else:
        pass
        yield u'\n  <link rel="stylesheet" type="text/css" media="screen"\n      href="%s">\n' % (
            escape(context.call((undefined(name='get_static_resource_url') if l_0_get_static_resource_url is missing else l_0_get_static_resource_url), '/third_party/generated/css/third_party.css')), 
        )
    yield u'\n<link rel="stylesheet" type="text/css" media="screen"\n      href="%s/css/oppia.css">' % (
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
    )

blocks = {}
debug_info = '3=14&5=17&8=22&11=25'