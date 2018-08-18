from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/profile_link/profile_link_image_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<a ng-if="isUsernameLinkable(username())" ng-href="/profile/<[username()]>">\n  <img ng-src="<[profilePicture]>" alt="User Avatar" class="img-circle">\n</a>\n\n<img ng-if="!isUsernameLinkable(username())" ng-src="<[profilePicture]>" alt="">'

blocks = {}
debug_info = ''