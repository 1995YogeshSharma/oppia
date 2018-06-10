from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/promo/promo_bar_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-toast-container toast-top-center" ng-if="promoIsVisible">\n  <div class="toast toast-info oppia-toast">\n    <button type="button" class="toast-close-button" ng-click="dismissPromo()" role="button">&times;</button>\n    <div class="toast-message"><[getPromoMessage()]></div>\n  </div>\n</div>'

blocks = {}
debug_info = ''