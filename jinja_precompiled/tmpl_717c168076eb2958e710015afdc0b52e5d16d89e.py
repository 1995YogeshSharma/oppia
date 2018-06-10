from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/test_interaction_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="form-inline" style="margin-bottom: 20px;">\n  <table class="preview-conversation-skin-card-row-container">\n    <tr class="preview-conversation-skin-card-row">\n      <td class="preview-conversation-skin-row-avatar" valign="top">\n        <img class="preview-conversation-skin-row-avatar-img" ng-src="<[userBlackImgUrl]>">\n      </td>\n      <td class="preview-conversation-skin-oppia-content">\n        <div angular-html-bind="stateContent()"></div>\n      </td>\n    </tr>\n  </table>\n  <div ng-if="interactionIsInline">\n    <div class="preview-conversation-skin-inline-interaction">\n      <table class="preview-conversation-skin-card-row-container" style="margin-bottom: 0;">\n        <tr class="preview-conversation-skin-card-row">\n          <td class="preview-conversation-skin-row-avatar" valign="top">\n            <img class="preview-conversation-skin-row-avatar-img img-circle" ng-src="<[userBlueImgUrl]>" >\n          </td>\n          <td class="preview-conversation-skin-learner-input" angular-html-bind="inputTemplate()">\n          </td>\n        </tr>\n      </table>\n    </div>\n  </div>\n  <div class="preview-conversation-skin-supplemental-interaction" ng-if="!interactionIsInline">\n    <div>\n      <md-card class="preview-conversation-skin-supplemental-card">\n        <div angular-html-bind="inputTemplate()">\n        </div>\n      </md-card>\n    </div>\n  </div>\n</div>'

blocks = {}
debug_info = ''