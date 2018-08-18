from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/skill_editor/skill_editor.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/skill_editor/skill_editor.html')
    for name, parent_block in parent_template.blocks.iteritems():
        context.blocks.setdefault(name, []).append(parent_block)
    for event in parent_template.root_render_func(context):
        yield event

def block_footer_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('footer_js', block_footer_js)
    pass
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/skill_editor/editor_tab/SkillEditorMainTabDirective.js"></script>\n  <script src="/templates/dev/head/pages/skill_editor/editor_tab/SkillDescriptionEditorDirective.js"></script>\n  <script src="/templates/dev/head/pages/skill_editor/editor_tab/SkillConceptCardEditorDirective.js"></script>\n  <script src="/templates/dev/head/pages/skill_editor/editor_tab/SkillMisconceptionsEditorDirective.js"></script>\n  <script src="/templates/dev/head/pages/skill_editor/editor_tab/MisconceptionEditorDirective.js"></script>\n  <script src="/templates/dev/head/pages/skill_editor/editor_tab/WorkedExampleEditorDirective.js"></script>\n  <script src="/templates/dev/head/pages/skill_editor/SkillEditor.js"></script>\n  <script src="/templates/dev/head/pages/skill_editor/SkillEditorStateService.js"></script>\n  <script src="/templates/dev/head/pages/skill_editor/SkillEditorNavbarDirective.js"></script>\n\n  <script src="/templates/dev/head/domain/skill/SkillObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/skill/SkillRightsObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/skill/ConceptCardObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/skill/MisconceptionObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/skill/EditableSkillBackendApiService.js"></script>\n  <script src="/templates/dev/head/domain/skill/SkillRightsBackendApiService.js"></script>\n\n  <script src="/templates/dev/head/domain/skill/SkillUpdateService.js"></script>\n  <script src="/templates/dev/head/domain/editor/undo_redo/ChangeObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/editor/undo_redo/UndoRedoService.js"></script>\n\n  <script src="/templates/dev/head/mathjaxConfig.js"></script>\n  <script src="/third_party/static/MathJax-2.6.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>\n\n  <script src="/templates/dev/head/components/forms/FormBuilder.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedCustomEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedDictEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedExpressionEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedFloatEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedHtmlEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedIntEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedListEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_editors/SchemaBasedUnicodeEditorDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedCustomViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedDictViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedHtmlViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedListViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedPrimitiveViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedUnicodeViewerDirective.js"></script>\n  <script src="/templates/dev/head/components/forms/schema_viewers/SchemaBasedViewerDirective.js"></script>\n\n  <script src="/extensions/objects/templates/MathLatexStringEditor.js"></script>\n  <script src="/extensions/objects/templates/SanitizedUrlEditor.js"></script>\n  <script src="/extensions/objects/templates/ListOfTabsEditor.js"></script>\n\n  <script src="/templates/dev/head/services/SchemaDefaultValueService.js"></script>\n  <script src="/templates/dev/head/services/SchemaUndefinedLastElementService.js"></script>\n  <script src="/templates/dev/head/services/NestedDirectivesRecursionTimeoutPreventionService.js"></script>\n  <script src="/templates/dev/head/services/GenerateContentIdService.js"></script>\n  <script src="/templates/dev/head/services/ValidatorsService.js"></script>\n\n  <script src="/templates/dev/head/components/SummaryListHeaderDirective.js"></script>\n\n  <script src="/templates/dev/head/components/loading/LoadingDotsDirective.js"></script>\n  ' % (
        escape(context.call(l_0_super)), 
    )
    template = environment.get_template('components/rich_text_components.html', 'pages/skill_editor/skill_editor.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {'super': l_0_super})):
        yield event
    yield u'\n'

def block_local_top_nav_options(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <skill-editor-navbar>\n  </skill-editor-navbar>\n'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div ng-controller="SkillEditor">\n    <skill-editor-main-tab></skill-editor-main-tab>\n  </div>\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Skill Editor\n'

def block_header_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('header_js', block_header_js)
    pass
    yield u'\n  %s\n' % (
        escape(context.call(l_0_super)), 
    )

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n\n'

blocks = {'footer_js': block_footer_js, 'local_top_nav_options': block_local_top_nav_options, 'content': block_content, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&27=17&28=24&84=26&12=31&21=38&3=45&17=52&18=59&8=62'