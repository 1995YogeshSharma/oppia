from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/solution_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div style="height: 100%;">\n  <div ng-if="!solutionEditorIsOpen"\n       style="height: 100%;"\n       ng-attr-title="Edit solution">\n    <div class="oppia-readonly-rule-tile"\n         ng-class="{\'oppia-editable-section\': true}">\n      <div class="oppia-rule-preview oppia-transition-200">\n        <div class="oppia-click-to-start-editing"\n             ng-click="onOpenSolutionEditor()">\n          <i class="material-icons oppia-editor-edit-icon pull-right"\n             title="Edit Solution">&#xE254;\n          </i>\n        </div>\n        <strong>\n          <[StateSolutionService.savedMemento.answerIsExclusive ? \'The only\' : \'One\']> solution is...\n        </strong>\n        <span>\n          <angular-html-bind html-data="getAnswerHtml()">\n          </angular-html-bind>\n        </span>\n      </div>\n    </div>\n  </div>\n  <br>\n  <solution-explanation-editor on-save-solution="onSaveSolution"\n                               on-save-content-ids-to-audio-translations="onSaveContentIdsToAudioTranslations">\n  </solution-explanation-editor>\n</div>'

blocks = {}
debug_info = ''