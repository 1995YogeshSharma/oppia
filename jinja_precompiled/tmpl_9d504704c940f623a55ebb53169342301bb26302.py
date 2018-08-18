from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/solution_interstitial_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-learner-solution-interstitial-modal-title">Warning!</div>\n\n<div class="modal-body">\n  <span class="oppia-learner-solution-interstitial-modal-body">\n    This will show the full solution. Are you sure?\n  </span>\n</div>\n\n<button class="oppia-learner-got-it-button md-button md-default-theme pull-right protractor-test-continue-to-solution-btn"\n        ng-click="continueToSolution()">\n  Show Solution\n</button>\n<button class="oppia-modal-cancel-button md-button md-default-theme pull-right" ng-click="cancel()">\n  Cancel\n</button>\n\n<span class="clearfix"></span>\n\n<style>\n  .oppia-learner-solution-interstitial-modal-title {\n    color: #00786D;\n    font-family: \'Capriola\', \'Roboto\', \'Arial\', sans-serif;\n    font-size: 1.75em;\n    font-weight: bold;\n    padding-top: 20px;\n    text-align: center;\n  }\n\n  .oppia-learner-solution-interstitial-modal-body {\n    word-wrap: break-word;\n  }\n\n  .md-button.oppia-modal-cancel-button {\n    background: #9a9a9a;\n    color: #ffffff;\n    margin-right: 12px;\n    padding: 6px 12px;\n  }\n  .md-button.md-default-theme.oppia-modal-cancel-button:focus,\n  .md-button.md-default-theme.oppia-modal-cancel-button:hover {\n    background: #7a7a7a;\n  }\n</style>'

blocks = {}
debug_info = ''