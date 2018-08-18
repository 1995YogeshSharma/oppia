from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/collection_editor/collection_editor.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/collection_editor/collection_editor.html')
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
    yield u'\n  %s\n\n  <script src="/templates/dev/head/expressions/ExpressionSyntaxTreeService.js"></script>\n  <script src="/templates/dev/head/expressions/ExpressionEvaluatorService.js"></script>\n  <script src="/templates/dev/head/expressions/ExpressionParserService.js"></script>\n  <script src="/templates/dev/head/expressions/ExpressionInterpolationService.js"></script>\n\n  <script src="/templates/dev/head/pages/collection_editor/CollectionEditor.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/CollectionEditorNavbarBreadcrumbDirective.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/CollectionEditorNavbarDirective.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/CollectionEditorStateService.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/editor_tab/CollectionEditorTabDirective.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/editor_tab/CollectionLinearizerService.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/editor_tab/CollectionNodeCreatorDirective.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/editor_tab/CollectionNodeEditorDirective.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/history_tab/CollectionHistoryTabDirective.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/settings_tab/CollectionDetailsEditorDirective.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/settings_tab/CollectionPermissionsCardDirective.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/settings_tab/CollectionSettingsTabDirective.js"></script>\n  <script src="/templates/dev/head/pages/collection_editor/statistics_tab/CollectionStatisticsTabDirective.js"></script>\n\n  <script src="/templates/dev/head/domain/collection/CollectionNodeObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/collection/CollectionObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/collection/CollectionRightsBackendApiService.js"></script>\n  <script src="/templates/dev/head/domain/collection/CollectionRightsObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/collection/CollectionUpdateService.js"></script>\n  <script src="/templates/dev/head/domain/collection/CollectionValidationService.js"></script>\n  <script src="/templates/dev/head/domain/collection/EditableCollectionBackendApiService.js"></script>\n  <script src="/templates/dev/head/domain/collection/ReadOnlyCollectionBackendApiService.js"></script>\n  <script src="/templates/dev/head/domain/collection/SearchExplorationsBackendApiService.js"></script>\n  <script src="/templates/dev/head/domain/editor/undo_redo/ChangeObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/editor/undo_redo/UndoRedoService.js"></script>\n  <script src="/templates/dev/head/domain/exploration/AudioTranslationObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/state/StateObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/InteractionObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/objects/FractionObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/objects/NumberWithUnitsObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/AnswerGroupObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/ContentIdsToAudioTranslationsObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/SubtitledHtmlObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/EditableExplorationBackendApiService.js"></script>\n  <script src="/templates/dev/head/domain/exploration/ReadOnlyExplorationBackendApiService.js"></script>\n  <script src="/templates/dev/head/domain/exploration/RuleObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/HintObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/TriggerObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/SolutionObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/StatesObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/OutcomeObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/ParamChangeObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/ParamChangesObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/ParamSpecObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/ParamSpecsObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/ParamTypeObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/exploration/ExplorationDraftObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/summary/ExplorationSummaryBackendApiService.js"></script>\n  <script src="/templates/dev/head/domain/utilities/BrowserCheckerService.js"></script>\n\n  <script src="/templates/dev/head/pages/exploration_player/AnswerClassificationService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_player/LearnerParamsService.js"></script>\n\n  <script src="/templates/dev/head/domain/utilities/LanguageUtilService.js"></script>\n  <script src="/templates/dev/head/domain/utilities/AudioLanguageObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/utilities/AutogeneratedAudioLanguageObjectFactory.js"></script>\n\n  <script src="/templates/dev/head/components/loading/LoadingDotsDirective.js"></script>\n\n  <script src="/templates/dev/head/components/forms/FormBuilder.js"></script>\n  <script src="/templates/dev/head/components/forms/Select2DropdownDirective.js"></script>\n\n  \n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationPropertyService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationAutomaticTextToSpeechService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationCategoryService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationCorrectnessFeedbackService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationInitStateNameService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationLanguageCodeService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationObjectiveService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationParamChangesService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationParamSpecsService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationStatesService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationTagsService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationTitleService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ChangeListService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/AutosaveInfoModalsService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationDataService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/AngularNameService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ExplorationEditor.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/RouterService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/ChangesInHumanReadableFormService.js"></script>\n\n  <script src="/templates/dev/head/services/ExplorationHtmlFormatterService.js"></script>\n  <script src="/templates/dev/head/services/GenerateContentIdService.js"></script>\n  <script src="/templates/dev/head/services/LocalStorageService.js"></script>\n\n  <script src="/templates/dev/head/pages/state_editor/StateEditorService.js"></script>\n\n  <script src="/templates/dev/head/pages/exploration_editor/editor_tab/SolutionVerificationService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_editor/editor_tab/SolutionValidityService.js"></script>\n  <script src="/templates/dev/head/domain/classifier/AnswerClassificationResultObjectFactory.js"></script>\n  <script src="/templates/dev/head/domain/classifier/ClassifierObjectFactory.js"></script>\n  <script src="/templates/dev/head/pages/exploration_player/PredictionAlgorithmRegistryService.js"></script>\n  <script src="/templates/dev/head/pages/exploration_player/StateClassifierMappingService.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_local_top_nav_options(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <collection-editor-navbar>\n  </collection-editor-navbar>\n'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div ng-controller="CollectionEditor">\n    <div ng-if="getTabStatuses().active === \'main\'">\n      <collection-main-tab></collection-main-tab>\n    </div>\n\n    <div ng-show="getTabStatuses().active === \'settings\'">\n      <collection-settings-tab></collection-settings-tab>\n    </div>\n\n    <div ng-show="getTabStatuses().active === \'history\'">\n      <collection-history-tab></collection-history-tab>\n    </div>\n\n    <div ng-show="getTabStatuses().active === \'stats\'">\n      <collection-statistics-tab></collection-statistics-tab>\n    </div>\n  </div>\n\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_title = resolve('title')
    pass
    yield u'\n  '
    if (undefined(name='title') if l_0_title is missing else l_0_title):
        pass
        yield u'\n    %s - Oppia Editor\n  ' % (
            escape((undefined(name='title') if l_0_title is missing else l_0_title)), 
        )
    else:
        pass
        yield u'\n    Untitled Collection - Oppia Editor\n  '
    yield u'\n'

def block_header_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('header_js', block_header_js)
    l_0_collection_id = resolve('collection_id')
    l_0_TAG_REGEX = resolve('TAG_REGEX')
    t_1 = environment.filters['js_string']
    pass
    yield u'\n  %s\n  <script type="text/javascript">\n    GLOBALS.collectionId = JSON.parse(\'%s\');\n    GLOBALS.TAG_REGEX = JSON.parse(\'%s\');\n  </script>\n' % (
        escape(context.call(l_0_super)), 
        escape(t_1((undefined(name='collection_id') if l_0_collection_id is missing else l_0_collection_id))), 
        escape(t_1((undefined(name='TAG_REGEX') if l_0_TAG_REGEX is missing else l_0_TAG_REGEX))), 
    )

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <collection-editor-navbar-breadcrumb>\n  </collection-editor-navbar-breadcrumb>\n'

blocks = {'footer_js': block_footer_js, 'local_top_nav_options': block_local_top_nav_options, 'content': block_content, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&50=17&51=24&24=27&29=34&3=41&4=48&5=51&11=58&12=68&14=69&15=70&19=73'