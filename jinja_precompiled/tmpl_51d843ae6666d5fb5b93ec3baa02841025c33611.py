from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/continue_button_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<md-button class="oppia-learner-confirm-button protractor-test-continue-to-next-card-button"\n           focus-on="<[::focusLabel]>"\n           ng-click="onClickContinueButton()"\n           style="margin-top: 12px;"\n           aria-label="Continue">\n  <div ng-if="!isLearnAgainButton()">\n    <span translate="I18N_PLAYER_CONTINUE_BUTTON"></span>\n    <i class="fa fa-arrow-right"\n       style="font-size: 19px; padding-top: 1.5px;">\n    </i>\n  </div>\n  <div ng-if="isLearnAgainButton()">\n    <span translate="I18N_PLAYER_LEARN_AGAIN_BUTTON"></span>\n    <i class="fa fa-repeat"\n       style="font-size: 19px; padding-top: 1.5px;">\n    </i>\n  </div>\n</md-button>'

blocks = {}
debug_info = ''