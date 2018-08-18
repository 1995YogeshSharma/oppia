from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/learner_view_suggestion_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Suggest a Change</h3>\n</div>\n\n<div class="modal-body protractor-test-exploration-suggestion-modal">\n  <!-- ng-model needs to bind to a property of an object on the scope (the property cannot sit directly on the scope). -->\n  <ck-editor-rte ng-show="showEditor" ng-model="suggestionData.suggestionHtml"></ck-editor-rte>\n  <br>\n  Briefly describe your changes (required):\n  <input type="text" ng-model="description" class="protractor-test-suggestion-description-input" style="width: 100%">\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancelSuggestion()">Cancel</button>\n  <button class="btn btn-success protractor-test-suggestion-submit-btn" ng-click="submitSuggestion()" ng-disabled="(originalHtml == suggestionData.suggestionHtml) || !description">\n    Submit Suggestion\n  </button>\n</div>'

blocks = {}
debug_info = ''