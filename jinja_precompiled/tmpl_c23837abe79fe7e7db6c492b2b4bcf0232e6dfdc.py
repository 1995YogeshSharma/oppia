from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/add_hint_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header protractor-test-hint-modal">\n  <h3>Add Hint</h3>\n</div>\n\n<div class="modal-body">\n  <form name="addHintForm.hintTextForm"\n        class="form-inline">\n    <div class="oppia-rule-details-header">\n      <strong>Hint #<[hintIndex]> is...</strong>\n      <schema-based-editor class="protractor-test-hint-text"\n                           schema="HINT_FORM_SCHEMA"\n                           local-value="tmpHint">\n      </schema-based-editor>\n    </div>\n  </form>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default protractor-test-cancel-hint" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success protractor-test-save-hint" ng-click="saveHint()" ng-disabled="!tmpHint">Save Hint</button>\n</div>'

blocks = {}
debug_info = ''