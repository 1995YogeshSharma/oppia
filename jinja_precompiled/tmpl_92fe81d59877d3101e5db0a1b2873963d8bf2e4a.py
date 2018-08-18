from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/skill_editor/editor_tab/worked_example_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div style="height: 100%">\n  <div ng-if="!editorIsOpen"\n       style="height: 100%"\n       ng-attr-title="Edit worked example">\n    <div class="oppia-readonly-rule-title"\n         ng-class="{\'oppia-editable-section\': isEditable()}">\n      <div class="oppia-rule-preview">\n        <div class="oppia-click-to-start-editing" ng-click="openEditor()">\n          <i ng-if="isEditable()"\n             class="material-icons oppia-editor-edit-icon pull-right"\n             title="Edit Worked Example">&#xE254;\n          </i>\n        </div>\n\n        <strong>Worked Example</strong>\n        <angular-html-bind html-data="container.workedExample"></angular-html-bind>\n      </div>\n    </div>\n  </div>\n\n  <div ng-if="isEditable() && editorIsOpen">\n    <form role="form"\n          class="form-inline"\n          name="editWorkedExampleForm"\n          ng-submit="saveWorkedExample()">\n      <div class="oppia-rule-details-header">\n        <strong>Worked Example</strong>\n        <schema-based-editor schema="WORKED_EXAMPLE_FORM_SCHEMA"\n                             local-value="container.workedExample">\n        </schema-based-editor>\n      </div>\n    </form>\n\n    <div class="oppia-rule-save-cancel-buttons">\n      <div class="pull-right">\n        <button type="button"\n                class="btn btn-default"\n                ng-click="cancelEdit()">\n          Cancel\n        </button>\n        <button type="button"\n                class="btn btn-success"\n                ng-disabled="!container.workedExample || editWorkedExampleForm.$invalid"\n                ng-click="saveWorkedExample()">\n          Save\n        </button>\n      </div>\n      <div style="clear: both;"></div>\n    </div>\n  </div>\n</div>'

blocks = {}
debug_info = ''