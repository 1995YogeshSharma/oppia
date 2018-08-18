from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/feedback_tab/editor_view_suggestion_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Review Suggestion</h3>\n</div>\n\n<div class="modal-body">\n  <section class="oppia-suggestion-review-container">\n    <div class="oppia-suggestion-review-panel-container" style="float: left;">\n      <strong>Current:</strong>\n      <div class="oppia-suggestion-review-panel">\n        <angular-html-bind ng-if="currentContent" html-data="currentContent">\n        </angular-html-bind>\n        <div ng-if="!currentContent" style="color: red;">Oops! This state no longer exists!</div>\n      </div>\n    </div>\n    <div class="oppia-suggestion-review-panel-container" style="float: right;">\n      <strong>Suggested:</strong>\n      <div class="oppia-suggestion-review-panel">\n        <angular-html-bind html-data="newContent">\n        </angular-html-bind>\n      </div>\n    </div>\n  </section>\n  <div ng-show="canAccept" style="margin-top: 20px; margin-left: 10px;">\n    Review message (required if rejecting):\n    <input type="text" ng-model="reviewMessage" style="width: 100%">\n  </div>\n  <div style="margin-top: 20px; margin-left: 10px;" ng-show="canAccept">\n    Brief Description of Changes (required if accepting):\n    <input class="protractor-test-suggestion-commit-message"type="text" ng-model="commitMessage" style="width: 100%">\n  </div>\n</div>\n\n<div class="modal-footer">\n  <div ng-show="errorMessage" class="oppia-suggestion-review-error">\n    <[ errorMessage ]>\n  </div>\n  <button class="btn btn-default" ng-click="cancelReview()">Cancel</button>\n  <button class="btn btn-danger" ng-show="canEdit && isNotHandled" ng-click="rejectSuggestion()" ng-disabled="!canReject">Reject</button>\n  <button class="btn btn-success protractor-test-exploration-accept-suggestion-btn" ng-show="canEdit && isNotHandled" ng-click="acceptSuggestion()" ng-disabled="!canAccept || commitMessage.length == 0">Accept</button>\n</div>'

blocks = {}
debug_info = ''