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
    l_0_TEMPLATE_DIR_PREFIX = resolve('TEMPLATE_DIR_PREFIX')
    pass
    yield u'\n  %s\n\n  <script src="%s/expressions/ExpressionSyntaxTreeService.js"></script>\n  <script src="%s/expressions/ExpressionEvaluatorService.js"></script>\n  <script src="%s/expressions/ExpressionParserService.js"></script>\n  <script src="%s/expressions/ExpressionInterpolationService.js"></script>\n\n  <script src="%s/pages/collection_editor/CollectionEditor.js"></script>\n  <script src="%s/pages/collection_editor/CollectionEditorNavbarBreadcrumbDirective.js"></script>\n  <script src="%s/pages/collection_editor/CollectionEditorNavbarDirective.js"></script>\n  <script src="%s/pages/collection_editor/CollectionEditorStateService.js"></script>\n  <script src="%s/pages/collection_editor/editor_tab/CollectionEditorTabDirective.js"></script>\n  <script src="%s/pages/collection_editor/editor_tab/CollectionLinearizerService.js"></script>\n  <script src="%s/pages/collection_editor/editor_tab/CollectionNodeCreatorDirective.js"></script>\n  <script src="%s/pages/collection_editor/editor_tab/CollectionNodeEditorDirective.js"></script>\n  <script src="%s/pages/collection_editor/history_tab/CollectionHistoryTabDirective.js"></script>\n  <script src="%s/pages/collection_editor/settings_tab/CollectionDetailsEditorDirective.js"></script>\n  <script src="%s/pages/collection_editor/settings_tab/CollectionPermissionsCardDirective.js"></script>\n  <script src="%s/pages/collection_editor/settings_tab/CollectionSettingsTabDirective.js"></script>\n  <script src="%s/pages/collection_editor/statistics_tab/CollectionStatisticsTabDirective.js"></script>\n\n  <script src="%s/domain/collection/CollectionNodeObjectFactory.js"></script>\n  <script src="%s/domain/collection/CollectionObjectFactory.js"></script>\n  <script src="%s/domain/collection/CollectionRightsBackendApiService.js"></script>\n  <script src="%s/domain/collection/CollectionRightsObjectFactory.js"></script>\n  <script src="%s/domain/collection/CollectionUpdateService.js"></script>\n  <script src="%s/domain/collection/CollectionValidationService.js"></script>\n  <script src="%s/domain/collection/EditableCollectionBackendApiService.js"></script>\n  <script src="%s/domain/collection/ReadOnlyCollectionBackendApiService.js"></script>\n  <script src="%s/domain/collection/SearchExplorationsBackendApiService.js"></script>\n  <script src="%s/domain/editor/undo_redo/ChangeObjectFactory.js"></script>\n  <script src="%s/domain/editor/undo_redo/UndoRedoService.js"></script>\n  <script src="%s/domain/exploration/AudioTranslationObjectFactory.js"></script>\n  <script src="%s/domain/exploration/StateObjectFactory.js"></script>\n  <script src="%s/domain/exploration/InteractionObjectFactory.js"></script>\n  <script src="%s/domain/objects/FractionObjectFactory.js"></script>\n  <script src="%s/domain/exploration/AnswerGroupObjectFactory.js"></script>\n  <script src="%s/domain/exploration/SubtitledHtmlObjectFactory.js"></script>\n  <script src="%s/domain/exploration/EditableExplorationBackendApiService.js"></script>\n  <script src="%s/domain/exploration/ReadOnlyExplorationBackendApiService.js"></script>\n  <script src="%s/domain/exploration/RuleObjectFactory.js"></script>\n  <script src="%s/domain/exploration/HintObjectFactory.js"></script>\n  <script src="%s/domain/exploration/TriggerObjectFactory.js"></script>\n  <script src="%s/domain/exploration/SolutionObjectFactory.js"></script>\n  <script src="%s/domain/exploration/StatesObjectFactory.js"></script>\n  <script src="%s/domain/exploration/OutcomeObjectFactory.js"></script>\n  <script src="%s/domain/exploration/ParamChangeObjectFactory.js"></script>\n  <script src="%s/domain/exploration/ParamChangesObjectFactory.js"></script>\n  <script src="%s/domain/exploration/ParamSpecObjectFactory.js"></script>\n  <script src="%s/domain/exploration/ParamSpecsObjectFactory.js"></script>\n  <script src="%s/domain/exploration/ParamTypeObjectFactory.js"></script>\n  <script src="%s/domain/exploration/ExplorationDraftObjectFactory.js"></script>\n  <script src="%s/domain/summary/ExplorationSummaryBackendApiService.js"></script>\n  <script src="%s/domain/utilities/BrowserCheckerService.js"></script>\n\n  <script src="%s/pages/exploration_player/AnswerClassificationService.js"></script>\n  <script src="%s/pages/exploration_player/LearnerParamsService.js"></script>\n\n  <script src="%s/domain/utilities/LanguageUtilService.js"></script>\n  <script src="%s/domain/utilities/AudioLanguageObjectFactory.js"></script>\n  <script src="%s/domain/utilities/AutogeneratedAudioLanguageObjectFactory.js"></script>\n\n  <script src="%s/components/loading/LoadingDotsDirective.js"></script>\n\n  <script src="%s/components/forms/FormBuilder.js"></script>\n  <script src="%s/components/forms/Select2DropdownDirective.js"></script>\n\n  \n  <script src="%s/pages/exploration_editor/ExplorationPropertyService.js"></script>\n  <script src="%s/pages/exploration_editor/ChangeListService.js"></script>\n  <script src="%s/pages/exploration_editor/AutosaveInfoModalsService.js"></script>\n  <script src="%s/pages/exploration_editor/ExplorationDataService.js"></script>\n  <script src="%s/pages/exploration_editor/EditorStateService.js"></script>\n  <script src="%s/pages/exploration_editor/AngularNameService.js"></script>\n  <script src="%s/pages/exploration_editor/ExplorationEditor.js"></script>\n  <script src="%s/pages/exploration_editor/RouterService.js"></script>\n  <script src="%s/pages/exploration_editor/ChangesInHumanReadableFormService.js"></script>\n\n  <script src="%s/services/ExplorationHtmlFormatterService.js"></script>\n  <script src="%s/services/LocalStorageService.js"></script>\n\n  <script src="%s/pages/exploration_editor/editor_tab/SolutionVerificationService.js"></script>\n  <script src="%s/pages/exploration_editor/editor_tab/SolutionValidityService.js"></script>\n  <script src="%s/domain/classifier/AnswerClassificationResultObjectFactory.js"></script>\n  <script src="%s/domain/classifier/ClassifierObjectFactory.js"></script>\n  <script src="%s/pages/exploration_player/PredictionAlgorithmRegistryService.js"></script>\n  <script src="%s/pages/exploration_player/StateClassifierMappingService.js"></script>\n' % (
        escape(context.call(l_0_super)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
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
debug_info = '1=11&50=17&51=25&53=26&54=27&55=28&56=29&58=30&59=31&60=32&61=33&62=34&63=35&64=36&65=37&66=38&67=39&68=40&69=41&70=42&72=43&73=44&74=45&75=46&76=47&77=48&78=49&79=50&80=51&81=52&82=53&83=54&84=55&85=56&86=57&87=58&88=59&89=60&90=61&91=62&92=63&93=64&94=65&95=66&96=67&97=68&98=69&99=70&100=71&101=72&102=73&103=74&104=75&106=76&107=77&109=78&110=79&111=80&113=81&115=82&116=83&119=84&120=85&121=86&122=87&123=88&124=89&125=90&126=91&127=92&129=93&130=94&132=95&133=96&134=97&135=98&136=99&137=100&24=103&29=110&3=117&4=124&5=127&11=134&12=144&14=145&15=146&19=149'