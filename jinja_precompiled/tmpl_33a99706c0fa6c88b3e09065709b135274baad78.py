from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/schema_editors/schema_based_float_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<span ng-model="localValue" ui-validate="\'validate($value)\'">\n  <span ng-form="floatForm">\n    <span ng-if="!expressionMode">\n      <input type="number" step="any" ng-model="$parent.localValue" class="form-control protractor-test-float-form-input"\n             name="floatValue" ng-attr-placeholder="<[\'I18N_FORMS_TYPE_NUMBER\' | translate]>" ng-disabled="isDisabled()"\n             require-is-float apply-validation="validators()"\n             focus-on="<[labelForFocusTarget()]>" ng-keypress="onKeypress($event)"\n             ng-blur="onBlur()" ng-focus="onFocus()" style="display: inline;">\n\n      <span ng-if="hasLoaded && !isUserCurrentlyTyping && hasFocusedAtLeastOnce"\n            style="font-size: 0.85em; position: absolute;"\n            tabindex="-1" focus-on="<[labelForErrorFocusTarget]>">\n        <span ng-if="floatForm.floatValue.$error.isFloat && floatForm.floatValue.$viewValue" class="oppia-form-error" aria-live="assertive" translate="I18N_FORMS_TYPE_NUMBER_INVALID_DECIMAL"></span>\n        <span ng-if="!floatForm.floatValue.$error.isFloat && floatForm.floatValue.$error.isAtLeast"\n              class="oppia-form-error" aria-live="assertive" translate="I18N_FORMS_TYPE_NUMBER_AT_LEAST" translate-values="{minValue: <[minValue]>}">\n        </span>\n        <span ng-if="!floatForm.floatValue.$error.isFloat && floatForm.floatValue.$error.isAtMost"\n              class="oppia-form-error" aria-live="assertive" translate="I18N_FORMS_TYPE_NUMBER_AT_MOST" translate-values="{maxValue: <[maxValue]>}">\n        </span>\n      </span>\n    </span>\n  </span>\n</span>'

blocks = {}
debug_info = ''