from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/exploration_title_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<p ng-class="{\'has-error\': !explorationTitleService.displayed.length > 0}">\n  <label for="explorationTitle" ng-style="<[::formStyle]>"><[::labelText]></label>\n  <input id="explorationTitle" type="text" class="form-control protractor-test-exploration-title-input"\n         ng-model="explorationTitleService.displayed" ng-blur="onInputFieldBlur()"\n         placeholder="Choose a title for your exploration." focus-on="<[::focusLabel]>"\n         maxlength="40" ng-trim="false">\n  <span class="help-block" style="font-size: smaller">\n    <em>Please use at most 40 characters, so that this fits in the summary card.</em>\n    <span ng-if="explorationTitleService.displayed.length > 0">\n      <em>Characters used: <[explorationTitleService.displayed.length]>/40</em>\n    </span>\n  </span>\n</p>\n<style>\n  @media (min-width: 768px) {\n    exploration-title-editor p {\n      display: table;\n      margin-bottom: 2%;\n      width: 100%;\n    }\n  }\n  .modal-body exploration-title-editor .help-block {\n    margin-bottom: -8px;\n  }\n</style>'

blocks = {}
debug_info = ''