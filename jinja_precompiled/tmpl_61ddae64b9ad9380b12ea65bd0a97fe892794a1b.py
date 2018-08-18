from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/topic_editor/subtopics_editor/subtopic_editor_modal_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="subtopic-editor">\n  <div class="modal-header">\n    <h3>\n      Edit Subtopic\n    </h3>\n  </div>\n  <div class="modal-body">\n    <div class="subtopic-title">\n      <span ng-if="!subtopicTitleEditorIsShown" ng-click="openSubtopicTitleEditor()"\n            class="oppia-editable-section">\n        <strong style="font-size: 1.2em;"><[editableTitle]></strong>\n        <i class="material-icons oppia-editor-edit-icon"\n           title="Edit Subtopic Title">&#xE254;\n        </i>\n      </span>\n      <span ng-if="subtopicTitleEditorIsShown">\n        <form class="form-horizontal" role="form" ng-submit="updateSubtopicTitle(editableTitle)">\n          <input type="text" ng-model="editableTitle">\n          <button type="submit" ng-disabled="editableTitle === \'\'" class="btn btn-success btn-sm">Save</button>\n          <button class="btn btn-default btn-sm" ng-click="closeSubtopicTitleEditor()">Cancel</button>\n        </form>\n      </span>\n    </div>\n    <div class="subtopic-page-editor">\n      <strong> Subtopic Page </strong>\n      <div ng-if="!subtopicEditorIsShown" class="preview">\n        <angular-html-bind html-data="htmlData">\n        </angular-html-bind>\n        <div class="pull-right">\n          <button type="button"\n                  class="btn btn-default save-button"\n                  ng-click="closePreviewSubtopicPage(htmlData)">\n            Edit\n          </button>\n        </div>\n      </div>\n      <div ng-if="subtopicEditorIsShown" class="oppia-editor-card-body">\n        <schema-based-editor schema="SUBTOPIC_PAGE_SCHEMA"\n                             local-value="htmlData">\n        </schema-based-editor>\n\n        <div class="pull-right">\n          <button type="button"\n                  class="btn btn-success save-button"\n                  ng-click="updateHtmlData(htmlData)">\n            Save\n          </button>\n          <button type="button"\n                  class="btn btn-default save-button"\n                  ng-click="openPreviewSubtopicPage(htmlData)">\n            Preview\n          </button>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="modal-footer">\n    <button class="btn btn-primary" ng-disabled="editableTitle === \'\'" ng-click="save()"> Done </button>\n    <button class="btn btn-default" ng-click="cancel()"> Cancel </button>\n  </div>\n</div>\n\n<style>\n  .subtopic-editor .subtopic-page-editor {\n    min-height: 20vh;\n  }\n\n  .subtopic-editor .modal-body .subtopic-title {\n    margin-bottom: 3%;\n  }\n</style>'

blocks = {}
debug_info = ''