from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/skill_editor/editor_tab/add_worked_example_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="modal-header">\n  <h3>Add Worked Example</h3>\n</div>\n\n<div class="modal-body">\n  <form name="addWorkedExampleForm.workedExampleTextForm"\n        class="form-inline">\n    <div class="oppia-rule-details-header">\n      <strong>Worked Example</strong>\n      <schema-based-editor schema="WORKED_EXAMPLE_FORM_SCHEMA"\n                           local-value="tmpWorkedExampleHtml">\n      </schema-based-editor>\n    </div>\n  </form>\n</div>\n\n<div class="modal-footer">\n  <button class="btn btn-default" ng-click="cancel()">Cancel</button>\n  <button class="btn btn-success" ng-click="saveWorkedExample()" ng-disabled="!tmpWorkedExampleHtml">Save</button>\n</div>'

blocks = {}
debug_info = ''