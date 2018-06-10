from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/editor_tab/state_editor.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div ng-controller="StateEditor" class="oppia-editor-cards-container">\n  <div class="oppia-editor-header">\n    '
    template = environment.get_template('pages/exploration_editor/editor_tab/sidebar_state_name.html', 'pages/exploration_editor/editor_tab/state_editor.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n  </div>\n\n  <div ng-if="areParametersEnabled()">\n    '
    template = environment.get_template('pages/exploration_editor/editor_tab/state_parameter_changes.html', 'pages/exploration_editor/editor_tab/state_editor.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n  </div>\n\n  <md-card class="oppia-editor-card-with-avatar">\n    <div class="oppia-editor-card-body">\n      <img ng-src="<[oppiaBlackImgUrl]>" alt="" class="oppia-editor-card-avatar">\n      <div id="tutorialStateContent" class="oppia-editor-card-section"\n           style="padding-top: 36px; padding-bottom: 36px;">\n        <state-content-editor on-save-content-fn="showInteraction">\n        </state-content-editor>\n      </div>\n    </div>\n  </md-card>\n\n  <div ng-show="interactionIsShown">\n    '
    template = environment.get_template('pages/exploration_editor/editor_tab/state_editor_interaction.html', 'pages/exploration_editor/editor_tab/state_editor.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n  </div>\n\n  <div ng-hide="!interactionIdIsSet || currentStateIsTerminal">\n    '
    template = environment.get_template('pages/exploration_editor/editor_tab/state_editor_responses.html', 'pages/exploration_editor/editor_tab/state_editor.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n    <div>\n      '
    template = environment.get_template('pages/exploration_editor/editor_tab/state_editor_hints.html', 'pages/exploration_editor/editor_tab/state_editor.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n    </div>\n    <div ng-if="currentInteractionCanHaveSolution">\n      '
    template = environment.get_template('pages/exploration_editor/editor_tab/state_editor_solution.html', 'pages/exploration_editor/editor_tab/state_editor.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n    </div>\n  </div>\n\n  <div>\n    '
    template = environment.get_template('pages/exploration_editor/editor_tab/state_statistics.html', 'pages/exploration_editor/editor_tab/state_editor.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n  </div>\n</div>'

blocks = {}
debug_info = '3=11&7=15&22=19&26=23&28=27&31=31&36=35'