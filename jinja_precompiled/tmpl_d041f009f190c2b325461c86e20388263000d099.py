from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_editors/schema_based_int_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  schema-based-int-editor .oppia-blue-on-focus > input:focus {\n    border-bottom-color: rgb(63, 81, 181);\n    border-bottom-width: 2px;\n  }\n</style>\n\n<div class="input-group">\n  <span ng-if="!expressionMode">\n    <md-input-group class="long oppia-blue-on-focus md-default-theme" style="margin: 0px;">\n      <input type="number" ng-model="$parent.localValue" ng-disabled="isDisabled()"\n             required apply-validation="validators()" focus-on="<[labelForFocusTarget()]>"\n             ng-blur="onInputBlur()" ng-focus="onInputFocus()">\n    </md-input-group>\n  </span>\n</div>'

blocks = {}
debug_info = ''