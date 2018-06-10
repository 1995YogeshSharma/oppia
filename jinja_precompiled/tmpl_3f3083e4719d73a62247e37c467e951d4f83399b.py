from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/tutor_card_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<audio-bar ng-if="!isIframed"></audio-bar>\n<div class="conversation-skin-tutor-card"\n     ng-class="{\'animate-card-width\': startCardChangeAnimation}">\n  <div class="conversation-skin-tutor-card-content conversation-skin-animate-tutor-card-content"\n       ng-class="{\'animate-card-change\': startCardChangeAnimation}">\n    <div class="conversation-skin-tutor-card-top-section">\n      <img class="conversation-skin-oppia-avatar"\n           ng-src="<[OPPIA_AVATAR_IMAGE_URL]>" alt="">\n      <div class="rte-viewer conversation-skin-tutor-card-top-content"\n           ng-class="getContentAudioHighlightClass()"\n           focus-on="<[getContentFocusLabel($index)]>">\n        <div class="protractor-test-conversation-content"\n             angular-html-bind="activeCard.contentHtml">\n        </div>\n        <div ng-if="isContentAudioTranslationAvailable()"\n             class="conversation-skin-audio-controls">\n        </div>\n      </div>\n    </div>\n\n    <div ng-if="(activeCard.inputResponsePairs.length > 1 && isInteractionInline) || (activeCard.inputResponsePairs.length > 0 && !isInteractionInline)">\n      <h4 class="conversation-skin-responses-dropdown-container"\n          ng-click="toggleShowPreviousResponses()">\n        <span class="conversation-skin-responses-dropdown-text">\n          <span translate="I18N_PLAYER_PREVIOUS_RESPONSES"\n                translate-values="{previousResponses: <[activeCard.inputResponsePairs.length - (isInteractionInline ? 1 : 0)]>}">\n          </span>\n          <span class="conversation-skin-responses-dropdown-icon">\n            <i class="material-icons conversation-skin-responses-dropdown-icon" ng-class="{\'conversation-skin-responses-dropdown-icon-rotated\': arePreviousResponsesShown}">&#xE037;</i>\n          </span>\n        </span>\n      </h4>\n    </div>\n\n    <div ng-show="arePreviousResponsesShown"\n         class="conversation-skin-tutor-card-middle-section conversation-skin-responses-animate-slide">\n      <div ng-repeat="responsePair in activeCard.inputResponsePairs track by $index">\n        <div ng-if="!$last || !isInteractionInline">\n          <input-response-pair data="responsePair"\n                                profile-picture="profilePicture"\n                                oppia-avatar-image-url="OPPIA_AVATAR_IMAGE_URL"\n                                input-response-pair-id="getInputResponsePairId($index)"\n                                is-last-pair="false">\n          </input-response-pair>\n        </div>\n      </div>\n    </div>\n\n    <!-- If the interaction is inline, always show the most recent response pair, if there is one. -->\n    <div class="conversation-skin-tutor-card-bottom-section" ng-if="isInteractionInline && activeCard.inputResponsePairs.length > 0">\n      <input-response-pair data="activeCard.inputResponsePairs[activeCard.inputResponsePairs.length - 1]"\n                            profile-picture="profilePicture"\n                            oppia-avatar-image-url="OPPIA_AVATAR_IMAGE_URL"\n                            input-response-pair-id="getInputResponsePairId(activeCard.inputResponsePairs.length - 1)"\n                            is-last-pair="true">\n      </input-response-pair>\n    </div>\n\n    <!--\n      Show the interaction (if it is inline) or the interaction instructions\n      (if the interaction is supplemental).\n\n      In addition, if the exploration is iframed, the terminal card will\n      have no learner input section, so we do not show it.\n    -->\n    <div ng-show="isInteractionInline && isCurrentCardAtEndOfTranscript() && !waitingForOppiaFeedback &&\n    ((activeCard.interactionHtml && !activeCard.destStateName) || activeCard.destStateName) &&\n    (!isOnTerminalCard() || !isIframed || activeCard.destStateName)">\n      <div class="conversation-skin-inline-interaction">\n        <!-- The seemingly redundant check for isInteractionInline is necessary\n          because the parent ng-show does not remove the element from the DOM.\n          This can lead to two conflicting copies of the interaction for\n          non-inline interactions. -->\n        <div ng-if="isInteractionInline && activeCard.interactionHtml && !activeCard.destStateName">\n          <div class="protractor-test-conversation-input"\n               angular-html-bind="activeCard.interactionHtml">\n          </div>\n        </div>\n      </div>\n    </div>\n\n    <div ng-if="!isInteractionInline"\n        class="conversation-skin-inline-interaction" style="opacity: 0.8;">\n      <div style="padding: 6px 12px;">\n        <span ng-class="{\'conversation-skin-instruction-disabled\': !interactionIsActive}"> <[interactionInstructions]> </span>\n        <i ng-if="canWindowShowTwoCards()" ng-class="{\'conversation-skin-instruction-disabled\': !interactionIsActive}" class="material-icons md-18" style="position: relative;">&#xE5C8;</i>\n        <i ng-if="!canWindowShowTwoCards()" ng-class="{\'conversation-skin-instruction-disabled\': !interactionIsActive}" class="material-icons md-18" style="position: relative;">&#xE5DB;</i>\n      </div>\n    </div>\n\n    <div ng-if="!activeCard.interactionHtml && !isOnTerminalCard()">\n      <div class="conversation-skin-inline-interaction">\n        <span style="color: red;">\n          <strong>Error</strong>: No interaction specified for \'<[activeCard.stateName]>\'.\n        </span>\n      </div>\n    </div>\n  </div>\n</div>\n\n<style>\n  .conversation-skin-tutor-card {\n    max-width: 100vw;\n    padding-bottom: 18px;\n  }\n\n  .conversation-skin-instruction-disabled {\n    color: gray;\n  }\n\n  .conversation-skin-tutor-card-top-section .conversation-skin-oppia-avatar {\n    height: 100px;\n    left: -87px;\n    top: -20px;\n    width: 100px;\n  }\n\n  .conversation-skin-tutor-card-middle-section .conversation-skin-user-avatar,\n  .conversation-skin-tutor-card-middle-section .conversation-skin-oppia-avatar {\n    display: none;\n  }\n\n  .conversation-skin-tutor-card .instructions-button {\n    background: inherit;\n    border: none;\n    white-space: normal;\n  }\n\n  .conversation-skin-tutor-card.animate-card-width {\n    -webkit-transition: width 500ms;\n    transition: width 500ms;\n  }\n\n  .conversation-skin-tutor-card-top-section {\n    position: relative;\n  }\n\n  .conversation-skin-tutor-card-top-section {\n    padding: 0 20px;\n  }\n\n  .conversation-skin-tutor-card-top-content p:not(:last-child) {\n    line-height: 1.5;\n    margin-bottom: 18px;\n  }\n\n  .conversation-skin-tutor-card-top-content {\n    width: 100%;\n  }\n\n  /* This should match the value defined in AUDIO_HIGHLIGHT_CSS_CLASS. */\n  .conversation-skin-audio-highlight {\n    border: 3px solid #f3d140;\n  }\n\n  .conversation-skin-tutor-card,\n  .conversation-skin-future-tutor-card {\n    background: #fff;\n    border-radius: 2px;\n    padding-top: 20px;\n    text-align: left;\n    margin-left: 87px;\n  }\n\n  .conversation-skin-tutor-card-middle-section .conversation-skin-learner-answer-content {\n    background-color: rgba(236,239,241,0.4);\n  }\n\n  .conversation-skin-tutor-card-middle-section .conversation-skin-oppia-feedback-content {\n    background-color: rgba(224,242,241,0.4);\n  }\n\n  .conversation-skin-tutor-card-middle-section .conversation-skin-oppia-feedback-content::before,\n  .conversation-skin-tutor-card-middle-section .conversation-skin-learner-answer-content::before {\n    display: none;\n  }\n\n  .conversation-skin-tutor-card.ng-hide {\n    opacity: 0;\n    transform: translateX(-1000px);\n  }\n\n  .conversation-skin-tutor-card-content {\n    word-wrap: break-word;\n  }\n\n  .conversation-skin-responses-dropdown-container {\n    border-bottom: 1px solid #ccc;\n    cursor: pointer;\n    line-height: 0.1em;\n    margin: 8px 20px 20px 20px;\n    text-align: center;\n  }\n\n  .conversation-skin-responses-dropdown-text {\n    background-color: #fff;\n    color: #888;\n    font-size: 0.8em;\n    padding: 0 10px;\n  }\n\n  .conversation-skin-responses-dropdown-icon {\n    -moz-transition: all 0.2s;\n    -o-transition: all 0.2s;\n    -webkit-transition: all 0.2s;\n    font-size: 20px;\n    margin-bottom: -2px;\n  }\n\n  .conversation-skin-responses-dropdown-icon-rotated {\n    margin-bottom: -2px;\n    -moz-transform: rotate(90deg);\n    -o-transform: rotate(90deg);\n    -webkit-transform: rotate(90deg);\n    transform: rotate(90deg);\n    transition: transform 0.2s ease-in-out;\n  }\n\n  .conversation-skin-inline-interaction {\n    border-bottom-left-radius: 2px;\n    border-bottom-right-radius: 2px;\n    padding: 8px 20px 0;\n    position: relative;\n  }\n\n  .conversation-skin-inline-interaction .conversation-skin-user-avatar {\n    left: -20px;\n    top: 14px;\n  }\n\n  /* When the size of the browser is reduced, and the answer submitted is\n     correct, the continue button (in the tutor card) hides under the\n     Correctness footer and the page cannot be scrolled down further.\n     So this padding allows to scroll down the tutor card. */\n  @media(max-width: 770px) {\n    .conversation-skin-tutor-card {\n      padding-bottom: 30px;\n    }\n  }\n\n  @media screen and (max-width: 959px) {\n    .conversation-skin-tutor-card .instructions-button {\n      background-color: #0D48A1;\n      color: #ffffff;\n      padding: 6px 12px;\n      white-space: normal;\n    }\n\n    .conversation-skin-tutor-card button.md-button.md-default-theme.instructions-button:focus,\n    .conversation-skin-tutor-card button.md-button.md-default-theme.instructions-button:hover {\n      background-color: #115FD4;\n    }\n  }\n</style>'

blocks = {}
debug_info = ''