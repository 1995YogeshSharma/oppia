from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/preview_tab/preview_tab.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_DEFAULT_TWITTER_SHARE_MESSAGE_PLAYER = resolve('DEFAULT_TWITTER_SHARE_MESSAGE_PLAYER')
    pass
    yield u'<div ng-controller="PreviewTab">\n  <div ng-if="isExplorationPopulated">\n    <div ng-if="previewWarning">\n      <div class="oppia-preview-state-warning"><[previewWarning]></div>\n    </div>\n    <conversation-skin></conversation-skin>\n    <exploration-footer twitter-text="%s"></exploration-footer>\n\n  </div>\n\n  <div class="oppia-preview-bottom-right-container">\n    <div class="oppia-parameter-summary" ng-if="showParameterSummary()">\n      <strong>Parameters:</strong>\n      <table>\n        <tr ng-repeat="(paramName, paramValue) in allParams">\n          <td style="padding: 1px 5px;"><[paramName]>:</td>\n          <td style="padding: 1px 5px;">\n            <[paramValue != "" ? paramValue : "[Not set]"]>\n          </td>\n        </tr>\n      </table>\n    </div>\n    <button class="btn-lg" ng-click="resetPreview()">\n      <i class="material-icons" style="margin-bottom: 2px;">&#xE5D5;</i>\n      <span style="margin-left: 10px; padding-top: 20px;">Restart From Beginning</span>\n    </button>\n  </div>\n\n</div>\n\n<style>\n  .oppia-preview-bottom-right-container {\n    /* Fixed at bottom right corner (before footer) and appear on top of other div*/\n    bottom: 10px;\n    display: block;\n    position: fixed;\n    right: 0;\n    padding-bottom: 2em;\n    z-index: 1060;\n  }\n\n  .oppia-preview-bottom-right-container .oppia-parameter-summary {\n    background-color: #fff;\n    font-size: 16px;\n    margin: 0px 0px 2px 0px;\n    padding: 5px 0px 0px 5px;\n    text-align: left;\n  }\n\n  .oppia-preview-bottom-right-container .btn-lg {\n    background-color: #fff;\n    border: none;\n    border-radius: 0px;\n    display: block;\n    font-size: 20px;\n    text-align: right;\n    margin-top: 10px;\n    padding-top: 10px;\n  }\n\n  .oppia-preview-state-warning {\n    background-color: #fff;\n    border: 1px solid #ccc;\n    border-radius: 4px;\n    display: block;\n    font-size: 16px;\n    font-weight: bold;\n    left: 6px;\n    max-width: 296px;\n    padding: 3px;\n    position: absolute;\n    text-align: left;\n    top: 63px;\n    white-space: normal;\n    z-index: 1060;\n  }\n</style>' % (
        escape((undefined(name='DEFAULT_TWITTER_SHARE_MESSAGE_PLAYER') if l_0_DEFAULT_TWITTER_SHARE_MESSAGE_PLAYER is missing else l_0_DEFAULT_TWITTER_SHARE_MESSAGE_PLAYER)), 
    )

blocks = {}
debug_info = '7=12'