from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/background/background_banner_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div style="position: absolute; width: 100%; background-color: #aed2e9; text-align: center; overflow: hidden;">\n  <img ng-src="<[bannerImageFileUrl]>" align="center"\n       style="width: 3000px; top: 65px; max-width: 3000px;" alt="">\n</div>'

blocks = {}
debug_info = ''