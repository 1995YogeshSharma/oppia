from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/learner_view_suggestion_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3 translate="I18N_LEARNER_DASHBOARD_SUGGESTION_TEXT"></h3>\n</div>\n\n<div class="modal-body">\n  <section class="oppia-suggestion-review-container">\n    <div class="oppia-suggestion-review-panel-container" style="float: left;">\n      <strong translate="I18N_LEARNER_DASHBOARD_SUGGESTION_CURRENT_STATE_CONTENT_HEADER"></strong>\n      <div class="oppia-suggestion-review-panel">\n        <div>\n          <angular-html-bind ng-if="oldContent" html-data="oldContent">\n          </angular-html-bind>\n        </div>\n        <div ng-if="!oldContent" style="color: red;" translate="I18N_LEARNER_DASHBOARD_SUGGESTION_NO_CURRENT_STATE"></div>\n      </div>\n    </div>\n    <div class="oppia-suggestion-review-panel-container" style="float: right;">\n      <strong translate="I18N_LEARNER_DASHBOARD_SUGGESTION_SUGGESTED_STATE_CONTENT_HEADER"></strong>\n      <div class="oppia-suggestion-review-panel">\n        <angular-html-bind html-data="newContent">\n        </angular-html-bind>\n      </div>\n    </div>\n  </section>\n  <div style="margin-top: 20px; margin-left: 10px;">\n    <span translate="I18N_LEARNER_DASHBOARD_SUGGESTION_DESCRIPTION"></span>\n    <div class="oppia-suggestion-review-panel">\n      <angular-html-bind html-data="description">\n      </angular-html-bind>\n    </div>\n  </div>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()" translate="I18N_MODAL_CANCEL_BUTTON"></button>\n</div>'

blocks = {}
debug_info = ''