from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/profile_link/profile_link_text_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<a ng-if="isUsernameLinkable(username())" ng-href="/profile/<[username()]>">\n  <[username()]>\n</a>\n<span ng-if="!isUsernameLinkable(username())">\n  <[username()]>\n</span>'

blocks = {}
debug_info = ''