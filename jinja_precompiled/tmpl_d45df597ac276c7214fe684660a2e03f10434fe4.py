from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_editors/schema_based_choices_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<select class="form-control" ng-model="$parent.$parent.localValue"\n        ng-options="choice as choice for choice in choices()" required\n        ng-disabled="isDisabled()">\n</select>'

blocks = {}
debug_info = ''