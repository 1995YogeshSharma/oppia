from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/exploration_objective_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<form name="objectiveForm">\n  <p ng-class="{\'has-error\': objectiveForm.$dirty && (!explorationObjectiveService.displayed || explorationObjectiveService.displayed.length < 15 || explorationObjectiveService.displayed.length > 100)}">\n    <label for="explorationObjective" ng-style="<[::formStyle]>"><[::labelText]></label>\n    <input id="explorationObjective" type="text"\n           class="form-control protractor-test-exploration-objective-input"\n           ng-model="explorationObjectiveService.displayed"\n           ng-blur="onInputFieldBlur()" placeholder="Learn how to..." ng-trim="false">\n    <span class="help-block" style="font-size: smaller">\n      <em>In a complete sentence, tell people what they\'ll learn from this exploration.</em>\n      <span ng-if="explorationObjectiveService.displayed.length > 0">\n        <em>Characters used: <[explorationObjectiveService.displayed.length]>/100</em>\n      </span>\n    </span>\n  </p>\n</form>\n<style>\n  @media (min-width: 768px) {\n    exploration-objective-editor p {\n      display: table;\n      margin-bottom: 2%;\n      width: 100%;\n    }\n  }\n  .modal-body exploration-objective-editor .help-block {\n    margin-bottom: -8px;\n  }\n</style>'

blocks = {}
debug_info = ''