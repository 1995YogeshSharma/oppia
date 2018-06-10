from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_editors/schema_based_bool_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="input-group">\n  <span ng-if="!expressionMode">\n    <input type="checkbox" ng-model="$parent.localValue" ng-disabled="isDisabled()"\n           focus-on="<[labelForFocusTarget()]>">\n  </span>\n</div>'

blocks = {}
debug_info = ''