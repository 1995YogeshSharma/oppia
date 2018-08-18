from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/feedback_popup_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  feedback-popup .oppia-feedback-popover-textarea {\n    border: 1px solid rgba(0,0,0,0.2);\n    margin-top: 4px;\n    padding: 4px;\n    resize: none;\n    width: 200px;\n  }\n</style>\n<div style="min-width: 200px;">\n  <div ng-show="!feedbackSubmitted">\n    <button type="button" class="oppia-close-popover-button protractor-test-exploration-feedback-close-button" ng-click="closePopover()">\n      <i class="material-icons md-18">&#xE5CD;</i>\n    </button>\n    <br>\n\n    <div>\n      <textarea ng-model="feedbackText" rows="5" class="protractor-test-exploration-feedback-textarea oppia-feedback-popover-textarea"\n                placeholder="<[\'I18N_PLAYER_LEAVE_FEEDBACK\' | translate]>" focus-on="<[feedbackPopoverId]>">\n      </textarea>\n    </div>\n\n    <!-- The z-index ensures that the button is not overlapped by the checkbox div. -->\n    <md-button class="pull-right protractor-test-exploration-feedback-submit-btn"\n               ng-class="{\'oppia-feedback-popover-submit-btn-enabled\': feedbackText}" style="margin-top: 6px; z-index: 30;"\n               ng-click="saveFeedback()"\n               ng-disabled="!feedbackText"\n               translate="I18N_PLAYER_SUBMIT_BUTTON">\n    </md-button>\n    <div class="checkbox" style="font-size: 0.9em; margin: 12px 0 4px 0;" ng-show="isLoggedIn">\n      <label>\n        <input type="checkbox" ng-model="isSubmitterAnonymized">\n        <span translate="I18N_PLAYER_STAY_ANONYMOUS"></span>\n      </label>\n    </div>\n  </div>\n\n  <div ng-show="feedbackSubmitted" class="ng-cloak" translate="I18N_PLAYER_THANK_FEEDBACK">\n  </div>\n</div>'

blocks = {}
debug_info = ''