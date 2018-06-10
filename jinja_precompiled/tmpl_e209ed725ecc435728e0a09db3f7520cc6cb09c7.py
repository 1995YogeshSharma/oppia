from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/tests/form_entry_point_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<ng-form name="schemaForm">\n  <schema-based-editor local-value="localValue" schema="definition" is-disabled="isDisabled()">\n  </schema-based-editor>\n</ng-form>\n\n<div ng-if="!isDisabled()">\n  <button ng-click="submitValue(localValue)" class="btn btn-success" ng-disabled="schemaForm.$invalid">Submit</button>\n  <button ng-click="cancelEdit()" class="btn btn-default">Cancel</button>\n</div>'

blocks = {}
debug_info = ''