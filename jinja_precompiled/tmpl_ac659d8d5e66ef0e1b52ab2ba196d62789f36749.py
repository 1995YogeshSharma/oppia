from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/progress_nav_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="progress-nav-bar" layout="row" layout-align="space-between center">\n  <!-- Wrapping div on first button keeps the second button right-aligned\n    even when the first button is not present. -->\n  <div>\n    <!-- ng-if on this second wrapping div because ng-if lags on buttons. -->\n    <div ng-if="hasPrevious && !helpCardHasContinueButton">\n      <md-button ng-click="changeCard(activeCardIndex-1)" class="md-raised protractor-test-back-button" style="margin: 0 0 12px 12px;">\n        <i class="material-icons oppia-vcenter" aria-hidden="true">&#xE5C4;</i>\n      </div>\n    </md-button>\n  </div>\n  <div ng-if="hasNext">\n    <md-button ng-click="changeCard(activeCardIndex+1)" class="md-raised" style="margin: 0 12px 12px 0">\n      <i class="material-icons oppia-vcenter" aria-hidden="true">&#xE5C8;</i>\n    </md-button>\n  </div>\n  <div ng-if="!hasNext" style="margin: 0 12px 12px 0">\n    <div ng-if="isSubmitButtonShown() && !shouldContinueButtonBeShown() && !helpCardHasContinueButton">\n      <!-- Special case for the \'Continue\' interaction. -->\n      <md-button ng-if="interactionId === \'Continue\'" ng-click="onSubmit()"\n                 class="oppia-learner-confirm-button protractor-test-continue-button">\n        <[interactionCustomizationArgs.buttonText.value]>\n        <i class="fa fa-arrow-right" style="font-size: 19px; padding-top: 1.5px;"></i>\n      </md-button>\n      <md-button ng-if="shouldGenericSubmitButtonBeShown()"\n                 class="oppia-learner-confirm-button protractor-test-submit-answer-button" ng-click="onSubmit()"\n                 ng-disabled="isSubmitButtonDisabled()"\n                 translate="I18N_INTERACTIONS_SUBMIT">\n      </md-button>\n    </div>\n    <continue-button ng-if="shouldContinueButtonBeShown()"\n                     focus-on="<[::CONTINUE_BUTTON_FOCUS_LABEL]>"\n                     is-learn-again-button="isLearnAgainButton()"\n                     ng-click="onClickContinueButton()">\n    </continue-button>\n  </div>\n</div>\n\n<style>\n  /*\n    This affects the progress nav bar.\n  */\n  progress-nav .progress-nav-bar {\n    background-color: white;\n    margin-left: 87px;\n    /*\n    87px is used to move the opppia avatar inside the conversation-skin-tutor-card div (so that it does not goes out of screen during zoom in).\n    */\n  }\n\n  @media screen and (max-width: 959px) {\n   progress-nav .progress-nav-bar {\n      margin-left: 0;\n    }\n  }\n</style>'

blocks = {}
debug_info = ''