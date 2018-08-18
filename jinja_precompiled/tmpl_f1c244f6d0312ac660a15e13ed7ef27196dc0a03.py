from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/summary_tile/circular_image_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<a ng-if="isLinkAvailable()" ng-href="<[link()]>">\n  <img ng-src="<[src()]>" alt="" class="img-circle">\n</a>\n\n<img ng-if="!isLinkAvailable()" class="img-circle" ng-src="<[src()]>">'

blocks = {}
debug_info = ''