from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_editors/schema_based_unicode_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<span>\n  <textarea ng-if="!getCodingMode() && getRows()"\n            ng-model="$parent.localValue"\n            rows="<[getRows()]>"\n            placeholder="<[getPlaceholder()]>"\n            ng-disabled="isDisabled()"\n            class="form-control" focus-on="<[labelForFocusTarget()]>"\n            ng-blur="onInputBlur()"\n            ng-focus="onInputFocus()">\n  </textarea>\n\n  <span ng-if="!getCodingMode() && !getRows()">\n    <input type="text" ng-disabled="isDisabled()" class="form-control"\n           ng-model="$parent.localValue" ng-blur="onInputBlur()"\n           ng-focus="onInputFocus()" focus-on="<[labelForFocusTarget()]>"\n           ng-keypress="onKeypress($event)" placeholder="<[getPlaceholder()]>" apply-validation="validators()"\n           style="display: inline;">\n  </span>\n\n  <!-- Note that we do not yet support ng-blur for the code editor. -->\n  <div ng-if="getCodingMode()" style="border: 1px solid #ccc;">\n    <div ui-codemirror\n         ng-model="$parent.localValue"\n         ui-codemirror-opts="codemirrorOptions"\n         ui-refresh="codemirrorStatus">\n    </div>\n  </div>\n</span>'

blocks = {}
debug_info = ''