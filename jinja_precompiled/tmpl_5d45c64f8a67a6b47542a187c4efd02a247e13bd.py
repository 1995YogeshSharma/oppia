from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_viewers/schema_based_dict_viewer_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div role="form">\n  <div ng-repeat="property in propertySchemas()">\n    <div class="form-group">\n      <label><[getHumanReadablePropertyDescription(property)]></label>\n      <div>\n        <schema-based-viewer schema="property.schema" local-value="localValue[property.name]">\n        </schema-based-viewer>\n      </div>\n    </div>\n  </div>\n</div>'

blocks = {}
debug_info = ''