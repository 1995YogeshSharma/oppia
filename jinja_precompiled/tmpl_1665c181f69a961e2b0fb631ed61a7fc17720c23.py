from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/library/library.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/library/library.html')
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
    yield u'\n  %s\n  <script src="%s/services/SearchService.js"></script>\n  <script src="%s/components/RatingComputationService.js"></script>\n  <script src="%s/domain/learner_dashboard/LearnerDashboardIdsBackendApiService.js"></script>\n  <script src="%s/domain/learner_dashboard/LearnerDashboardActivityIdsObjectFactory.js"></script>\n  <script src="%s/domain/learner_dashboard/LearnerPlaylistService.js"></script>\n  <script src="%s/components/profile_link/ProfileLinkImageDirective.js"></script>\n  <script src="%s/components/loading/LoadingDotsDirective.js"></script>\n  <script src="%s/components/summary_tile/ExplorationSummaryTileDirective.js"></script>\n  <script src="%s/components/summary_tile/CollectionSummaryTileDirective.js"></script>\n  <script src="%s/components/summary_tile/CircularImageDirective.js"></script>\n\n  <script src="%s/pages/library/Library.js"></script>\n  <script src="%s/pages/library/LibraryFooter.js"></script>\n  <script src="%s/domain/learner_dashboard/LearnerDashboardIconsDirective.js"></script>\n  <script src="%s/pages/library/ActivityTilesInfinityGridDirective.js"></script>\n  <script src="%s/pages/library/SearchBarDirective.js"></script>\n  <script src="%s/pages/library/SearchResultsDirective.js"></script>\n' % (
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
    )

def block_local_top_nav_options(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <search-bar></search-bar>\n'

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div ng-controller="LibraryFooter">\n    <div ng-if="pageMode !== LIBRARY_PAGE_MODES.SEARCH">\n      '
    template = environment.get_template('pages/footer.html', 'pages/library/library.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n    </div>\n  </div>\n'

def block_base_url(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <base href="/search/">\n'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div ng-controller="Library" class="oppia-library-container">\n    <div style="position: relative; z-index: 3;">\n      <div>\n        <div class="oppia-exp-summary-tiles-container" ng-if="pageMode === LIBRARY_PAGE_MODES.SEARCH">\n          <search-results></search-results>\n        </div>\n\n        <div class="oppia-exp-summary-tiles-container"\n             ng-if="pageMode === LIBRARY_PAGE_MODES.GROUP"\n             style="margin-bottom: 20px;">\n          <div ng-if="activityList.length === 0"\n               style="font-size: 1.2em; padding-bottom: 40px; padding-top: 40px;">\n              <p style="text-align: center;">\n                <span translate="I18N_LIBRARY_NO_EXPLORATIONS"></span>\n              </p>\n          </div>\n\n          <div ng-if="activityList.length > 0"\n               style="margin-right: auto; margin-left: auto; max-width: 856px;">\n            <h2 class="oppia-group-page-header" style="font-size: 2em;">\n              <span translate="<[groupHeaderI18nId]>"></span>\n            </h2>\n\n            <div ng-repeat="tile in activityList" style="display: inline-block;">\n              <exploration-summary-tile ng-if="tile.activity_type == \'exploration\'"\n                                        exploration-id="tile.id"\n                                        exploration-title="tile.title"\n                                        last-updated-msec="tile.last_updated_msec"\n                                        objective="tile.objective"\n                                        category="tile.category"\n                                        ratings="tile.ratings"\n                                        num-views="tile.num_views"\n                                        thumbnail-icon-url="tile.thumbnail_icon_url"\n                                        thumbnail-bg-color="tile.thumbnail_bg_color"\n                                        class="protractor-test-exp-summary-tile">\n              </exploration-summary-tile>\n            </div>\n          </div>\n        </div>\n\n        <div class="oppia-exp-summary-tiles-container" ng-if="pageMode === LIBRARY_PAGE_MODES.INDEX">\n          <img ng-src="<[bannerImageFileUrl]>" align="center"\n               width="100%" alt="">\n          <div style="text-align: center; width: 100%;">\n            <h1 class="oppia-library-h1" translate="I18N_LIBRARY_MAIN_HEADER"></h1>\n            <h2 class="oppia-library-h2" translate="I18N_LIBRARY_SUB_HEADER"></h2>\n          </div>\n\n          <div class="visible-xs" style="margin: 0 auto; width: fit-content; padding-right: 15px">\n            <search-bar></search-bar>\n          </div>\n\n          <div ng-if="libraryGroups.length === 0"\n               style="margin: 150px auto; text-align: center; width: 100%;"\n               translate="I18N_LIBRARY_NO_EXPLORATION_GROUPS">\n          </div>\n\n          <div class="oppia-library-group" ng-repeat="group in libraryGroups track by $index" ng-mouseenter="setActiveGroup($index)" ng-mouseleave="clearActiveGroup()">\n            <div class="row oppia-library-group-header-container">\n              <h2 ng-class="{\'active\': activeGroupIndex === $index}" class="oppia-library-group-header">\n                <a ng-if="group.has_full_results_page" class="protractor-test-library-<[group.protractor_id]>" ng-click="showFullResultsPage(group.categories, group.full_results_url)" tabindex="0">\n                  <span translate="<[group.header_i18n_id]>"></span>\n                  <span ng-show="activeGroupIndex === $index"><i class="material-icons md-32">&#xE315;</i></span>\n                </a>\n                <span ng-if="!group.has_full_results_page" translate="<[group.header_i18n_id]>">\n                </span>\n              </h2>\n            </div>\n\n            <!-- TODO(sll): Add card at end of the row that, when clicked, does showFullResultsPage(group.categories)" -->\n            <div ng-if="!libraryWindowIsNarrow">\n              <md-button class="md-no-ink oppia-library-carousel-scroller"\n                         ng-click="scroll($index, true)"\n                         ng-hide="leftmostCardIndices[$index] == 0">\n                <i class="material-icons">&#xE314;</i>\n              </md-button>\n              <div class="oppia-library-carousel-scroller" ng-if="leftmostCardIndices[$index] == 0" aria-hidden="true">\n              </div>\n\n              <div class="oppia-library-carousel"\n                   ng-swipe-right="scroll($index, true)"\n                   ng-swipe-left="scroll($index, false)">\n                <div class="oppia-library-carousel-tiles">\n                  <div ng-repeat="tile in group.activity_summary_dicts" style="display: inline-block;">\n                    <collection-summary-tile ng-if="tile.activity_type == \'collection\'"\n                                             collection-id="tile.id"\n                                             collection-title="tile.title"\n                                             last-updated-msec="tile.last_updated_msec"\n                                             objective="tile.objective"\n                                             node-count="tile.node_count"\n                                             category="tile.category"\n                                             thumbnail-icon-url="tile.thumbnail_icon_url"\n                                             thumbnail-bg-color="tile.thumbnail_bg_color"\n                                             activity-is-owned-by-current-user="activitiesOwned.collections[tile.id]"\n                                             show-learner-dashboard-icons-if-possible="true">\n                    </collection-summary-tile>\n                    <exploration-summary-tile ng-if="tile.activity_type == \'exploration\'"\n                                              exploration-id="tile.id"\n                                              exploration-title="tile.title"\n                                              last-updated-msec="tile.last_updated_msec"\n                                              objective="tile.objective"\n                                              category="tile.category"\n                                              ratings="tile.ratings"\n                                              num-views="tile.num_views"\n                                              thumbnail-icon-url="tile.thumbnail_icon_url"\n                                              thumbnail-bg-color="tile.thumbnail_bg_color"\n                                              class="protractor-test-exp-summary-tile"\n                                              activity-is-owned-by-current-user="activitiesOwned.explorations[tile.id]"\n                                              show-learner-dashboard-icons-if-possible="true">\n                    </exploration-summary-tile>\n                  </div>\n                </div>\n              </div>\n\n              <md-button class="md-no-ink oppia-library-carousel-scroller"\n                         ng-click="scroll($index, false)"\n                         ng-hide="(group.activity_summary_dicts.length - tileDisplayCount) <= leftmostCardIndices[$index]"\n                         aria-hidden="true">\n                <i class="material-icons">&#xE315;</i>\n              </md-button>\n              <div class="oppia-library-carousel-scroller"\n                   ng-if="(group.activity_summary_dicts.length - tileDisplayCount) <= leftmostCardIndices[$index]"></div>\n            </div>\n\n            <div ng-if="libraryWindowIsNarrow && leftmostCardIndices">\n              <md-button class="md-no-ink oppia-library-carousel-scroller"\n                         ng-click="decrementLeftmostCardIndex($index)"\n                         ng-hide="leftmostCardIndices[$index] == 0"\n                         aria-hidden="true">\n                <i class="material-icons">&#xE314;</i>\n              </md-button>\n              <div class="oppia-library-carousel-scroller" ng-if="leftmostCardIndices[$index] == 0"></div>\n\n              <div class="oppia-library-carousel">\n                <div class="oppia-library-carousel-tiles">\n                  <collection-summary-tile ng-if="group.activity_summary_dicts[leftmostCardIndices[$index]].activity_type == \'collection\'"\n                      collection-id="group.activity_summary_dicts[leftmostCardIndices[$index]].id"\n                      collection-title="group.activity_summary_dicts[leftmostCardIndices[$index]].title"\n                      last-updated-msec="group.activity_summary_dicts[leftmostCardIndices[$index]].last_updated_msec"\n                      objective="group.activity_summary_dicts[leftmostCardIndices[$index]].objective"\n                      node-count="group.activity_summary_dicts[leftmostCardIndices[$index]].node_count"\n                      category="group.activity_summary_dicts[leftmostCardIndices[$index]].category"\n                      thumbnail-icon-url="group.activity_summary_dicts[leftmostCardIndices[$index]].thumbnail_icon_url"\n                      thumbnail-bg-color="group.activity_summary_dicts[leftmostCardIndices[$index]].thumbnail_bg_color"\n                      show-learner-dashboard-icons-if-possible="true"\n                      container-is-narrow="true">\n                  </collection-summary-tile>\n                  <exploration-summary-tile ng-if="group.activity_summary_dicts[leftmostCardIndices[$index]].activity_type == \'exploration\'"\n                      exploration-id="group.activity_summary_dicts[leftmostCardIndices[$index]].id"\n                      exploration-title="group.activity_summary_dicts[leftmostCardIndices[$index]].title"\n                      last-updated-msec="group.activity_summary_dicts[leftmostCardIndices[$index]].last_updated_msec"\n                      objective="group.activity_summary_dicts[leftmostCardIndices[$index]].objective"\n                      category="group.activity_summary_dicts[leftmostCardIndices[$index]].category"\n                      ratings="group.activity_summary_dicts[leftmostCardIndices[$index]].ratings"\n                      num-views="group.activity_summary_dicts[leftmostCardIndices[$index]].num_views"\n                      thumbnail-icon-url="group.activity_summary_dicts[leftmostCardIndices[$index]].thumbnail_icon_url"\n                      thumbnail-bg-color="group.activity_summary_dicts[leftmostCardIndices[$index]].thumbnail_bg_color"\n                      class="protractor-test-exp-summary-tile"\n                      show-learner-dashboard-icons-if-possible="true"\n                      container-is-narrow="true">\n                  </exploration-summary-tile>\n                </div>\n              </div>\n\n              <md-button class="md-no-ink oppia-library-carousel-scroller"\n                         ng-click="incrementLeftmostCardIndex($index)"\n                         ng-hide="(group.activity_summary_dicts.length - tileDisplayCount) <= leftmostCardIndices[$index]">\n                <i class="material-icons">&#xE315;</i>\n              </md-button>\n              <div class="oppia-library-carousel-scroller"\n                   ng-if="(group.activity_summary_dicts.length - tileDisplayCount) <= leftmostCardIndices[$index]">\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_page_mode = resolve('page_mode')
    pass
    yield u'\n  '
    if (undefined(name='page_mode') if l_0_page_mode is missing else l_0_page_mode) in ['group', 'search']:
        pass
        yield u'\n    Find explorations to learn from - Oppia\n  '
    else:
        pass
        yield u'\n    I18N_LIBRARY_PAGE_TITLE\n  '
    yield u'\n'

def block_header_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('header_js', block_header_js)
    l_0_page_mode = resolve('page_mode')
    l_0_SEARCH_DROPDOWN_CATEGORIES = resolve('SEARCH_DROPDOWN_CATEGORIES')
    l_0_LANGUAGE_CODES_AND_NAMES = resolve('LANGUAGE_CODES_AND_NAMES')
    t_1 = environment.filters['js_string']
    pass
    yield u'\n  %s\n  <script type="text/javascript">\n    GLOBALS.LANGUAGE_CODES_AND_NAMES = JSON.parse(\n      \'%s\');\n    GLOBALS.SEARCH_DROPDOWN_CATEGORIES = JSON.parse(\n      \'%s\');\n    GLOBALS.PAGE_MODE = JSON.parse(\'%s\');\n  </script>\n\n  <style>\n    html, body {\n      background-color: #afd2eb;\n    }\n  </style>\n' % (
        escape(context.call(l_0_super)), 
        escape(t_1((undefined(name='LANGUAGE_CODES_AND_NAMES') if l_0_LANGUAGE_CODES_AND_NAMES is missing else l_0_LANGUAGE_CODES_AND_NAMES))), 
        escape(t_1((undefined(name='SEARCH_DROPDOWN_CATEGORIES') if l_0_SEARCH_DROPDOWN_CATEGORIES is missing else l_0_SEARCH_DROPDOWN_CATEGORIES))), 
        escape(t_1((undefined(name='page_mode') if l_0_page_mode is missing else l_0_page_mode))), 
    )

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n'

blocks = {'footer_js': block_footer_js, 'local_top_nav_options': block_local_top_nav_options, 'footer': block_footer, 'base_url': block_base_url, 'content': block_content, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&229=17&230=25&231=26&232=27&233=28&234=29&235=30&236=31&237=32&238=33&239=34&240=35&242=36&243=37&244=38&245=39&246=40&247=41&14=44&221=51&224=57&18=62&39=69&3=76&4=83&22=91&23=102&26=103&28=104&29=105&11=108'