from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/rating_display_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<span style="<[getCursorStyle()]>" ng-mouseleave="leaveArea()">\n  <span ng-if="ratingValue || isEditable" ng-repeat="star in stars" class="fa <[star.cssClass]> oppia-rating-star protractor-test-rating-star" ng-click="clickStar(star.value)" ng-mouseenter="enterStar(star.value)">\n    <span class="oppia-icon-accessibility-label">Rate this <[$index + 1]> stars</span>\n  </span>\n</span>'

blocks = {}
debug_info = ''