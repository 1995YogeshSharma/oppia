from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_viewers/schema_based_viewer_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<schema-based-primitive-viewer ng-if="(schema().type === \'bool\' || schema().type === \'int\' || schema().type == \'float\')" local-value="$parent.localValue">\n</schema-based-primitive-viewer>\n\n<schema-based-custom-viewer ng-if="schema().type === \'custom\'" obj-type="schema().obj_type"\n                            local-value="$parent.localValue">\n</schema-based-custom-viewer>\n\n<schema-based-dict-viewer ng-if="schema().type === \'dict\'" property-schemas="schema().properties"\n                          local-value="$parent.localValue">\n</schema-based-dict-viewer>\n\n<schema-based-html-viewer ng-if="schema().type === \'html\'" local-value="$parent.localValue">\n</schema-based-html-viewer>\n\n<schema-based-list-viewer ng-if="schema().type === \'list\'" item-schema="schema().items"\n                          local-value="$parent.localValue">\n</schema-based-list-viewer>\n\n<schema-based-unicode-viewer ng-if="schema().type === \'unicode\'" local-value="$parent.localValue">\n</schema-based-unicode-viewer>'

blocks = {}
debug_info = ''