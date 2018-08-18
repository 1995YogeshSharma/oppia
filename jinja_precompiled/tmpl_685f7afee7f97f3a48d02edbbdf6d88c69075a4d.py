from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/story_editor/story_editor.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/story_editor/story_editor.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div ng-controller="StoryEditor" class="story-editor">\n    <button class="btn btn-primary back-to-topic-button" ng-click="returnToTopicEditorPage()">\n      <i class="fa fa-arrow-left"></i> &nbsp;Return to topic\n    </button>\n    <story-editor></story-editor>\n  </div>\n\n  <style>\n    .story-editor .back-to-topic-button {\n      margin-top: 1.5%;\n      margin-left: 10%;\n    }\n  </style>\n'

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/mathjaxConfig.js"></script>\n  <script src="/third_party/static/MathJax-2.6.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>\n\n  <script src="/templates/dev/head/components/forms/FormBuilder.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedCustomEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedDictEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedExpressionEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedFloatEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedHtmlEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedIntEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedListEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedUnicodeEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedCustomViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedDictViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedHtmlViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedListViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedPrimitiveViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedUnicodeViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedViewerDirective.js"></script>\n\n  <script src="/extensions/objects/templates/MathLatexStringEditor.js"></script>\n  <script src="/extensions/objects/templates/SanitizedUrlEditor.js"></script>\n  <script src="/extensions/objects/templates/ListOfTabsEditor.js"></script>\n\n  <script src="/templates/dev/head/services/SchemaDefaultValueService.js"></script>\n  <script src="/templates/dev/head/services/SchemaUndefinedLastElementService.js"></script>\n  <script src="/templates/dev/head/services/NestedDirectivesRecursionTimeoutPreventionService.js"></script>\n  <script src="/templates/dev/head/services/GenerateContentIdService.js"></script>\n  <script src="/templates/dev/head/components/loading/LoadingDotsDirective.js"></script>\n\n  <script src="/templates/dev/head/domain/editor/undo_redo/ChangeObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/editor/undo_redo/UndoRedoService.js"></script>\n  <script src="/templates/dev/head/domain/story/EditableStoryBackendApiService.js"></script>\n  <script src="/templates/dev/head/domain/story/StoryObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/story/StoryContentsObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/story/StoryNodeObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/story/StoryUpdateService.js"></script>\n\n  <script src="/templates/dev/head/pages/story_editor/StoryEditor.js"></script>\n  <script src="/templates/dev/head/pages/story_editor/StoryEditorStateService.js"></script>\n  <script src="/templates/dev/head/pages/story_editor/main_editor/StoryEditorDirective.js"></script>\n  <script src="/templates/dev/head/pages/story_editor/main_editor/StoryNodeEditorDirective.js"></script>\n  <script src="/templates/dev/head/pages/story_editor/StoryEditorNavbarBreadcrumbDirective.js"></script>\n  <script src="/templates/dev/head/pages/story_editor/StoryEditorNavbarDirective.js"></script>\n  ' % (
        escape(context.call(l_0_super)), 
    )
    template = environment.get_template('components/rich_text_components.html', 'pages/story_editor/story_editor.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'super': l_0_super})):
        yield event
    yield u'\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_story_title = resolve('story_title')
    pass
    yield u'\n  %s - Oppia\n' % (
        escape((undefined(name='story_title') if l_0_story_title is missing else l_0_story_title)), 
    )

def block_local_top_nav_options(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <story-editor-navbar>\n  </story-editor-navbar>\n'

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <story-editor-navbar-breadcrumb>\n  </story-editor-navbar-breadcrumb>\n'

blocks = {'content': block_content, 'footer_js': block_footer_js, 'maintitle': block_maintitle, 'local_top_nav_options': block_local_top_nav_options, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&17=17&33=24&34=31&80=33&3=38&4=45&12=48&7=55'