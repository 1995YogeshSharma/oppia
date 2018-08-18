from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/audio_bar_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="audio-header" ng-if="isAudioBarAvailable()">\n  <div ng-if="audioBarIsExpanded" class="audio-controls">\n    <div style="width: 560px;">\n      <i class="fa audio-controls-button-icon"\n         ng-click="onPlayButtonClicked()"\n         ng-class="{\'fa-ellipsis-h\': audioLoadingIndicatorIsShown, \'fa-play-circle\': !isAudioPlaying(), \'fa-pause-circle\': isAudioPlaying(), \'audio-controls-audio-not-available\': !isAudioAvailableInCurrentLanguage() || audioIsLoading}"\n         uib-tooltip="<[!isAudioAvailableInCurrentLanguage() ? (\'I18N_PLAYER_AUDIO_NOT_AVAILABLE_IN\' | translate:{languageDescription:getCurrentAudioLanguageDescription()}) : \'\']>"\n         tooltip-append-to-body="true" tooltip-placement="right">\n      </i>\n      <div class="slider-section" ng-if="hasPressedPlayButtonAtLeastOnce">\n        <div ng-if="audioLoadingIndicatorIsShown">\n          <md-progress-linear md-mode="indeterminate"></md-progress-linear>\n        </div>\n        <div ng-if="!audioLoadingIndicatorIsShown">\n          <md-slider ng-model="track.progress" ng-model-options="{ getterSetter: true }" aria-label="audio-slider">\n          </md-slider>\n        </div>\n        <span ng-if="audioLoadingIndicatorIsShown && !doesCurrentAudioTranslationNeedUpdate()" class="audio-controls-message" translate="I18N_PLAYER_AUDIO_LOADING_AUDIO"></span>\n        <span ng-if="isAudioAvailableInCurrentLanguage() && doesCurrentAudioTranslationNeedUpdate()" class="audio-controls-message" translate="I18N_PLAYER_AUDIO_MIGHT_NOT_MATCH_TEXT"></span>\n        <!--Filler space for message-->\n        <span class="audio-controls-message">&zwnj;</span>\n      </div>\n      <select class="audio-language-select"\n              ng-model="selectedLanguage.value"\n              ng-options="o.value as o.displayed for o in languagesInExploration"\n              ng-style="hasPressedPlayButtonAtLeastOnce ? {\'width\': \'30%\'} : {\'width\': \'60%\'}"\n              ng-change="onNewLanguageSelected()">\n      </select>\n    </div>\n    <div class="audio-collapse-button audio-toggle-button" ng-if="audioBarIsExpanded" ng-click="collapseAudioBar()"><i class="fa fa-sort-up"></i></div>\n  </div>\n  <div class="audio-expand-button audio-toggle-button" ng-if="!audioBarIsExpanded" ng-click="expandAudioBar()"><span class="audio-expand-button-text" translate="I18N_PLAYER_AUDIO_EXPAND_TEXT"></span> <i class="audio-expand-icon fa fa-sort-down"></i></div>\n</div>\n\n<style>\n\n  .fa-play-circle:before {\n    font-size: 1.7em;\n  }\n\n  .fa-pause-circle:before {\n    font-size: 1.7em;\n  }\n\n  audio-bar md-progress-linear.md-default-theme .md-bar {\n    background-color: #009688;\n  }\n\n  audio-bar md-slider {\n    height: 5px;\n  }\n\n  audio-bar md-slider.md-default-theme .md-track-fill {\n    background-color: #009688;\n  }\n\n  audio-bar md-slider.md-default-theme .md-thumb:after {\n    border-color: #009688;\n    background-color: #009688;\n  }\n\n  audio-bar md-slider .md-track-container {\n    top: 5px;\n  }\n\n  audio-bar md-slider .md-thumb-container {\n    top: -17px;\n  }\n\n  .audio-header .fa-sort-up, .audio-header .fa-sort-down {\n    transform: translateY(-2px);\n  }\n\n  .audio-expand-button {\n    height: 20px;\n    width: 80px;\n    text-transform: uppercase;\n  }\n\n  .audio-collapse-button {\n    height: 10px;\n    position: absolute;\n    width: 30px;\n    top: 44px;\n  }\n\n  .audio-toggle-button {\n    background-color: #0D48A1;\n    border-bottom-left-radius: 15px;\n    border-bottom-right-radius: 15px;\n    color: white;\n    display: block;\n    font-size: 12px;\n    margin: 0 auto;\n    text-align: center;\n  }\n\n  .audio-controls-button-icon {\n    color: white;\n    font-size: 1.5em;\n    min-width: 6%;\n    text-align: right;\n    vertical-align: middle;\n  }\n\n  .audio-controls-button-image {\n    width: 21px;\n    height: 21px;\n  }\n\n  .audio-controls-button-icon:hover, .audio-controls-button-image:hover {\n    cursor: pointer;\n  }\n\n  .audio-controls-audio-not-available {\n    color: gray;\n  }\n\n  .audio-controls {\n    align-items: center;\n    background-color: #0D48A1;\n    display: flex;\n    flex-direction: row;\n    flex-wrap: nowrap;\n    height: 44px;\n    justify-content: center;\n    padding: 0 4px;\n    width: 100%;\n  }\n\n  .audio-controls.ng-enter,\n  .audio-controls.ng-leave {\n    -webkit-transition: 300ms cubic-bezier(0.250, 0.250, 0.750, 0.750) all;\n    -moz-transition: 300ms cubic-bezier(0.250, 0.250, 0.750, 0.750) all;\n    -ms-transition: 300ms cubic-bezier(0.250, 0.250, 0.750, 0.750) all;\n    -o-transition: 300ms cubic-bezier(0.250, 0.250, 0.750, 0.750) all;\n    transition: 300ms cubic-bezier(0.250, 0.250, 0.750, 0.750) all;\n    position: absolute;\n  }\n\n  .audio-controls.ng-enter {\n    top: -44px;\n  }\n\n  .audio-controls.ng-enter.audio-controls.ng-enter-active {\n    top: 0;\n  }\n\n  .audio-controls.ng-leave {\n    top: 0;\n  }\n\n  .audio-controls.ng-leave.audio-controls.ng-leave-active {\n    top: -44px;\n  }\n\n  .audio-controls-message {\n    font-size: 10px;\n    font-style: italic;\n    color: white;\n  }\n\n  .audio-header {\n    left: 0;\n    margin-top: -128px;\n    position: fixed;\n    top: 184px;\n    transition: margin-top 0.2s ease-in-out;\n    width: 100%;\n    z-index: 100;\n  }\n\n  .audio-language-select {\n    border-radius: 9px;\n    font-size: 15px;\n    margin-left: 5px;\n    padding-left: 3px;\n  }\n\n  audio-bar .slider-section {\n    display: inline-block;\n    margin: 0 auto;\n    padding: 0 4px;\n    transform: translateY(10px);\n    width: 50%;\n  }\n\n  .audio-bar-nav-up {\n    margin-top: -186px;\n  }\n\n  .audio-bar-nav-hidden {\n    margin-top: -270px;\n  }\n\n  @media screen and (max-width: 959px) {\n    .audio-expand-button {\n      height: 32px;\n      width: 100px;\n      text-transform: capitalize;\n    }\n\n    .audio-expand-button-text, .audio-expand-icon {\n      font-size: 18px;\n      line-height: 1.7em;\n    }\n  }\n\n</style>'

blocks = {}
debug_info = ''