from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/exploration_editor_tab.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div ng-controller="ExplorationEditorTab" class="oppia-editor-cards-container">\n  <div class="oppia-editor-header">\n    <state-name-editor></state-name-editor>\n  </div>\n\n  <div ng-if="areParametersEnabled()">\n    <state-param-changes-editor></state-param-changes-editor>\n  </div>\n\n  <state-editor on-save-state-content="saveStateContent"\n                on-save-content-ids-to-audio-translations="saveContentIdsToAudioTranslations"\n                on-save-interaction-customization-args="saveInteractionCustomizationArgs"\n                on-save-interaction-id="saveInteractionId"\n                on-save-interaction-default-outcome="saveInteractionDefaultOutcome"\n                on-save-interaction-answer-groups="saveInteractionAnswerGroups"\n                on-save-solution="saveSolution"\n                on-save-hints="saveHints"\n                recompute-graph="recomputeGraph"\n                state-content-placeholder="getStateContentPlaceholder()"\n                navigate-to-state="navigateToState"\n                add-state="addState"\n                refresh-warnings="refreshWarnings"\n                interaction-is-shown="interactionIsShown">\n  </state-editor>\n</div>'

blocks = {}
debug_info = ''