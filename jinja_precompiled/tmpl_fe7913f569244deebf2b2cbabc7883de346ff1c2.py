from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/refresher_exploration_confirmation_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  .oppia-learner-refresher-exploration-confirmation-body {\n    word-wrap: break-word;\n  }\n\n  .oppia-learner-refresher-exploration-confirmation-title {\n    color: #00786D;\n    font-family: \'Capriola\', \'Roboto\', \'Arial\', \'sans-serif\';\n    font-size: 1.25em;\n    font-weight: bold;\n    padding-top: 20px;\n    text-align: center;\n  }\n</style>\n<div class="oppia-learner-refresher-exploration-confirmation-title">Would you like a refresher?</div>\n\n<div class="modal-body">\n  <span class="oppia-learner-refresher-exploration-confirmation-body">\n    It looks like you\'re having some trouble with this question. Would you\n    like to try a short exploration to refresh your memory, and return\n    here after you\'ve completed that?\n  </span>\n</div>\n\n<button class="oppia-learner-got-it-button protractor-test-cancel-redirection-button md-button md-default-theme pull-right"\n        ng-click="cancelRedirect()">No\n</button>\n<button class="oppia-learner-got-it-button protractor-test-confirm-redirection-button md-button md-default-theme pull-right"\n        ng-click="confirmRedirect()">Yes\n</button>\n<span class="clearfix"></span>'

blocks = {}
debug_info = ''