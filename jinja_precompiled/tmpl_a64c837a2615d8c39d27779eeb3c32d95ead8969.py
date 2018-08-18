from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_viewers/schema_based_list_viewer_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<table class="table">\n  <tr ng-repeat="item in localValue track by $index">\n    <td>\n      <schema-based-viewer schema="itemSchema()" local-value="localValue[$index]">\n      </schema-based-viewer>\n    </td>\n  </tr>\n</table>'

blocks = {}
debug_info = ''