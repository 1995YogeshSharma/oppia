from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/test_interaction_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  .test-interaction-modal .submit-answer-btn {\n    text-align: right;\n  }\n</style>\n\n<div class="form-inline test-interaction-modal" style="margin-bottom: 20px;">\n  <div ng-if="interactionIsInline">\n    <div class="preview-conversation-skin-inline-interaction">\n      <table class="preview-conversation-skin-card-row-container" style="margin-bottom: 0;">\n        <tr class="preview-conversation-skin-card-row">\n          <td class="preview-conversation-skin-row-avatar" valign="top">\n            <img class="preview-conversation-skin-row-avatar-img img-circle" ng-src="<[userBlueImgUrl]>" >\n          </td>\n          <td class="preview-conversation-skin-learner-input">\n            <angular-html-bind html-data="getInputTemplate()"></angular-html-bind>\n          </td>\n        </tr>\n      </table>\n    </div>\n  </div>\n  <div class="preview-conversation-skin-supplemental-interaction" ng-if="!interactionIsInline">\n    <div>\n      <md-card class="preview-conversation-skin-supplemental-card">\n        <div>\n          <angular-html-bind html-data="getInputTemplate()">\n          </angular-html-bind>\n        </div>\n      </md-card>\n    </div>\n  </div>\n  <br>\n  <div class="submit-answer-btn">\n    <md-button class="oppia-learner-confirm-button protractor-test-submit-answer-button"\n               ng-disabled="!interactionAnswerIsValid"\n               ng-click="onSubmitAnswerFromButton()"\n               translate="I18N_INTERACTIONS_SUBMIT">\n    </md-button>\n  </div>\n</div>'

blocks = {}
debug_info = ''