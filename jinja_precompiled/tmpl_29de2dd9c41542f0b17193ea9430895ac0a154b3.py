from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/state_editor/state_content_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div ng-if="!contentEditorIsOpen">\n  <div class="protractor-test-edit-content"\n       ng-class="{\'oppia-editable-section\': isEditable()}"\n       ng-click="openStateContentEditor()">\n    <i ng-if="isEditable()" class="material-icons oppia-editor-edit-icon"\n       title="Edit Card Content">&#xE254;\n    </i>\n    <div class="oppia-state-content-display oppia-transition-200"\n         ng-class="{\'oppia-prevent-selection\': isEditable()}"\n         title="Card Content">\n      <span ng-show="StateContentService.savedMemento.hasNoHtml()" class="oppia-placeholder">\n        <[getStateContentPlaceholder()]>\n      </span>\n      <span>\n        <angular-html-bind html-data="StateContentService.savedMemento.getHtml()"\n                           class="oppia-rte-editor protractor-test-state-content-display">\n        </angular-html-bind>\n      </span>\n    </div>\n    <!-- This is a dummy div created to mask the contents when the user hovers over the content. -->\n    <div class="oppia-editable-section-mask protractor-test-state-edit-content">\n    </div>\n  </div>\n</div>\n\n<div ng-if="contentEditorIsOpen" class="protractor-test-state-content-editor">\n  <!-- TODO(sll): Find a way to do this without resorting to private properties like _html -->\n  <schema-based-editor schema="HTML_SCHEMA" local-value="StateContentService.displayed._html">\n  </schema-based-editor>\n\n  <div style="margin-top: 2px;">\n    <button type="button"\n            class="btn btn-success oppia-save-state-item-button protractor-test-save-state-content pull-right"\n            ng-click="onSaveContentButtonClicked()">\n      Save Content\n    </button>\n    <button type="button" class="btn btn-default pull-right" ng-click="cancelEdit()">Cancel</button>\n    <div style="clear: both;"></div>\n  </div>\n</div>'

blocks = {}
debug_info = ''