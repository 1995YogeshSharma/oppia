from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_player/hint_and_solution_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-learner-hint-and-solution-modal-title"><[isHint ? "Hint" : "Solution"]></div>\n\n<div class="modal-body">\n  <span ng-if="isHint" class="oppia-learner-hint-and-solution-modal-body"\n        angular-html-bind="hint.getHtml()"></span>\n  <div ng-if="!isHint">\n    <label><[shortAnswerHtml.prefix]> solution is: &nbsp; </label>\n    <span class="oppia-learner-hint-and-solution-modal-body"\n          angular-html-bind="shortAnswerHtml.answer"></span>\n    <br><br>\n    <label>Explanation: </label>\n    <span class="oppia-learner-hint-and-solution-modal-body"\n          angular-html-bind="solutionExplanationHtml"></span>\n  </div>\n</div>\n\n<button class="oppia-learner-got-it-button md-button md-default-theme pull-right"\n        ng-click="closeModal()">GOT IT</button>\n<span class="clearfix"></span>\n\n<style>\n  .oppia-learner-hint-and-solution-modal-title {\n    color: #00786D;\n    font-family: \'Capriola\', \'Roboto\', \'Arial\', \'sans-serif\';\n    font-size: 1.75em;\n    font-weight: bold;\n    padding-top: 20px;\n    text-align: center;\n  }\n\n  .oppia-learner-hint-and-solution-modal-body {\n    word-wrap: break-word;\n  }\n</style>'

blocks = {}
debug_info = ''