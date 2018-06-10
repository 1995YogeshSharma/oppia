from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/footer_js_libs.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_DEV_MODE = resolve('DEV_MODE')
    l_0_get_static_resource_url = resolve('get_static_resource_url')
    pass
    if (not (undefined(name='DEV_MODE') if l_0_DEV_MODE is missing else l_0_DEV_MODE)):
        pass
        yield u'\n  <script src="%s"></script>\n' % (
            escape(context.call((undefined(name='get_static_resource_url') if l_0_get_static_resource_url is missing else l_0_get_static_resource_url), '/third_party/generated/js/third_party.min.js')), 
        )
    else:
        pass
        yield u'\n  <script src="%s"></script>\n' % (
            escape(context.call((undefined(name='get_static_resource_url') if l_0_get_static_resource_url is missing else l_0_get_static_resource_url), '/third_party/generated/js/third_party.js')), 
        )

blocks = {}
debug_info = '1=12&2=15&4=20'