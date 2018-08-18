from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/question_editor/question_editor_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-editor-cards-container" ng-if="stateEditorInitialized">\n  <state-editor on-save-state-content="saveStateContent"\n                on-save-content-ids-to-audio-translations="saveContentIdsToAudioTranslations"\n                on-save-interaction-customization-args="saveInteractionCustomizationArgs"\n                on-save-interaction-id="saveInteractionId"\n                on-save-interaction-default-outcome="saveInteractionDefaultOutcome"\n                on-save-interaction-answer-groups="saveInteractionAnswerGroups"\n                on-save-solution="saveSolution"\n                on-save-hints="saveHints"\n                state-content-placeholder="getStateContentPlaceholder()"\n                interaction-is-shown="interactionIsShown"\n                recompute-graph="recomputeGraph"\n                navigate-to-state="navigateToState"\n                add-state="addState"\n                refresh-warnings="refreshWarnings">\n  </state-editor>\n</div>\n\n<style>\n  question-editor .oppia-editor-cards-container {\n    padding-bottom: 5vh;\n  }\n</style>'

blocks = {}
debug_info = ''