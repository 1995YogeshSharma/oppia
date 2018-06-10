from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_editors/schema_based_dict_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div role="form">\n  <div ng-repeat="property in propertySchemas()">\n    <div class="form-group">\n      <label for="<[fieldIds[property.name]]>"><[getHumanReadablePropertyDescription(property)]></label>\n      <!-- TODO(sll): This is in the wrong place. It should be on the input field. -->\n      <div id="<[fieldIds[property.name]]>">\n        <schema-based-editor schema="property.schema" is-disabled="isDisabled()"\n                             local-value="localValue[property.name]"\n                             label-for-focus-target="$index === 0 ? labelForFocusTarget() : \'\'">\n        </schema-based-editor>\n      </div>\n    </div>\n  </div>\n</div>'

blocks = {}
debug_info = ''