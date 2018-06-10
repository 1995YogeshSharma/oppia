from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/learner_dashboard/remove_activity_from_learner_dashboard_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3 translate="I18N_LEARNER_DASHBOARD_REMOVE_ACTIVITY_MODAL_HEADER" translate-values="{sectionNameI18nId: sectionNameI18nId}"></h3>\n</div>\n\n<div class="modal-body">\n  <p translate="I18N_LEARNER_DASHBOARD_REMOVE_ACTIVITY_MODAL_BODY" translate-values="{entityTitle: activityTitle, sectionNameI18nId: sectionNameI18nId}"></p>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()" translate="I18N_MODAL_CANCEL_BUTTON"></button>\n  <button class="btn btn-danger protractor-test-confirm-delete-interaction"\n          ng-click="remove()" translate="I18N_LEARNER_DASHBOARD_REMOVE_BUTTON">\n  </button>\n</div>'

blocks = {}
debug_info = ''