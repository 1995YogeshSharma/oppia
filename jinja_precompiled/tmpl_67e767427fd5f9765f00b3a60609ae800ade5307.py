from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/solution_explanation_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div style="height: 100%;">\n  <div ng-if="!explanationEditorIsOpen"\n       style="height: 100%;"\n       ng-attr-title="<[isEditable ? \'Edit explanation\' : \'\']>">\n    <div class="oppia-readonly-rule-tile"\n         ng-class="{\'oppia-editable-section\': isEditable}">\n      <div class="oppia-rule-preview oppia-transition-200">\n        <div class="oppia-click-to-start-editing"\n             ng-if="isEditable" ng-click="openExplanationEditor()">\n          <i class="material-icons oppia-editor-edit-icon pull-right"\n             title="Edit Explanation">&#xE254;\n          </i>\n        </div>\n        <strong>Explanation:</strong>\n        <span>\n          <angular-html-bind class="oppia-rte-editor" html-data="StateSolutionService.savedMemento.explanation.getHtml()">\n          </angular-html-bind>\n        </span>\n      </div>\n    </div>\n  </div>\n\n  <div ng-if="isEditable && explanationEditorIsOpen">\n    <div class="oppia-rule-details-header">\n      <strong>Explanation:</strong>\n      <!-- TODO(sll): Find a way to do this without resorting to private properties like _html -->\n      <schema-based-editor schema="EXPLANATION_FORM_SCHEMA"\n                           local-value="StateSolutionService.displayed.explanation._html">\n      </schema-based-editor>\n    </div>\n\n    <div class="oppia-rule-save-cancel-buttons">\n      <div class="pull-right">\n        <button type="button"\n                class="btn btn-default"\n                ng-click="cancelThisExplanationEdit()">\n          Cancel\n        </button>\n        <button type="button"\n                class="btn btn-success"\n                ng-disabled="!StateSolutionService.displayed.explanation.getHtml()"\n                ng-click="saveThisExplanation()">\n          Save\n        </button>\n      </div>\n\n      <div style="clear: both;"></div>\n    </div>\n  </div>\n</div>'

blocks = {}
debug_info = ''