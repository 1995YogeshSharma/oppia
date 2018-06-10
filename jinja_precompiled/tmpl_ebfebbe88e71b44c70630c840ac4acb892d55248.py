from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/param_changes_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  param-changes-editor .oppia-param-editor-row {\n    position: relative;\n  }\n  param-changes-editor .oppia-param-display-row {\n    margin-bottom: 4px;\n  }\n  param-changes-editor .oppia-param-change-sort-handle {\n    cursor: move;\n    left: -20px;\n    opacity: 0.3;\n    position: absolute;\n    top: 4px;\n  }\n  param-changes-editor .oppia-delete-param-change-button {\n    background: none;\n    border: 0;\n    color: #000;\n    cursor: pointer;\n    height: 30px;\n    opacity: 0.5;\n    width: 30px;\n  }\n  param-changes-editor .oppia-delete-param-change-button {\n    position: absolute;\n  }\n  param-changes-editor .oppia-delete-param-change-button {\n    right: -30px;\n    top: 0;\n  }\n  param-changes-editor .oppia-delete-param-change-button:hover {\n    opacity: 1;\n  }\n</style>\n<!--\n  We do not track by $index here, because if we do, then the select2 dropdown\n  will not update when elements are swapped or deleted.\n-->\n<div ng-if="isParamChangesEditorOpen && EditabilityService.isEditableOutsideTutorialMode()">\n  <div ng-model="paramChangesService.displayed"\n       ui-sortable="PARAM_CHANGE_LIST_SORTABLE_OPTIONS"\n       class="oppia-param-change-draggable-area">\n    <div ng-repeat="paramChange in paramChangesService.displayed"\n         class="oppia-param-editor-row protractor-test-param-changes-list">\n      <span class="oppia-param-change-sort-handle" ng-if="paramChangesService.displayed.length > 1">\n        <img ng-if="EditabilityService.isEditable()" ng-src="<[dragDotsImgUrl]>" width="10">\n      </span>\n      <span>\n        Change\n        <select2-dropdown item="paramChange.name"\n                          choices="paramNameChoices"\n                          placeholder="Param name"\n                          new-choice-regex="^[A-Za-z]+$"\n                          width="143px">\n        </select2-dropdown>\n\n        <select class="form-control" ng-model="paramChange.generatorId"\n                ng-options="key as PREAMBLE_TEXT[key] for (key, value) in PREAMBLE_TEXT"\n                style="width: 110px; display: inline;" required\n                ng-change="onChangeGeneratorType(paramChange)">\n        </select>\n        <value-generator-editor generator-id="paramChange.generatorId"\n                                customization-args="paramChange.customizationArgs"\n                                obj-type="\'UnicodeString\'">\n        </value-generator-editor>\n      </span>\n      <button type="button" class="oppia-delete-param-change-button oppia-transition-200"\n              ng-click="deleteParamChange($index)" title="Delete parameter change">\n        <i class="material-icons md-18" ng-if="EditabilityService.isEditable()">&#xE5CD;</i>\n      </button>\n    </div>\n  </div>\n\n  <div>\n    <button type="button" class="btn btn-default btn-xs protractor-test-add-param-button"\n            ng-click="addParamChange()">\n      Add parameter change\n    </button>\n  </div>\n\n  <div ng-if="warningText" class="oppia-serious-warning-text"\n       style="margin-top: 20px; margin-bottom: 20px;">\n    <i class="material-icons">&#xE002;</i>\n    <[warningText]>\n  </div>\n\n  <button type="button"\n          class="btn btn-success oppia-save-state-item-button pull-right protractor-test-save-param-changes-button"\n          ng-click="saveParamChanges()"\n          ng-disabled="!areDisplayedParamChangesValid()">Save Changes</button>\n  <button type="button" class="btn btn-default pull-right" ng-click="cancelEdit()">Cancel</button>\n  <div style="clear: both;"></div>\n</div>\n\n<div ng-if="!isParamChangesEditorOpen" ng-click="openParamChangesEditor()"\n     ng-class="{\'oppia-editable-section\': EditabilityService.isEditable()}">\n  <i ng-if="EditabilityService.isEditable()" class="material-icons oppia-editor-edit-icon"\n     title="Edit Card Parameter Changes">&#xE254;\n  </i>\n  <div class="oppia-param-changes-display oppia-transition-200"\n       ng-class="{\'oppia-prevent-selection\': EditabilityService.isEditable()}"\n       title="Card Parameter Changes" style="opacity: 0.7;">\n    <span ng-if="paramChangesService.savedMemento.length === 0">\n      <em>No parameter changes.</em>\n    </span>\n    <div class="oppia-param-display-row" ng-repeat="paramChange in paramChangesService.savedMemento track by $index">\n      <[$index + 1]>. Change <span class="label label-info"><[paramChange.name]></span>\n       <[HUMAN_READABLE_ARGS_RENDERERS[paramChange.generatorId](paramChange.customizationArgs)]>\n    </div>\n  </div>\n</div>'

blocks = {}
debug_info = ''