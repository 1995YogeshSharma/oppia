from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/profile/profile.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/profile/profile.html')
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
    yield u'\n  %s\n  <script src="%s/pages/profile/Profile.js"></script>\n\n  <script src="%s/components/RatingComputationService.js"></script>\n  <script src="%s/components/summary_tile/ExplorationSummaryTileDirective.js"></script>\n  <script src="%s/components/summary_tile/CircularImageDirective.js"></script>\n  <script src="%s/components/background/BackgroundBannerDirective.js"></script>\n' % (
        escape(context.call(l_0_super)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
        escape((undefined(name='TEMPLATE_DIR_PREFIX') if l_0_TEMPLATE_DIR_PREFIX is missing else l_0_TEMPLATE_DIR_PREFIX)), 
    )

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  '
    template = environment.get_template('pages/footer.html', 'pages/profile/profile.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <background-banner></background-banner>\n  <div class="oppia-profile-container" ng-controller="Profile">\n    <md-card class="oppia-profile-user-card">\n      <div class="oppia-profile-picture-container">\n        <div ng-if="profileIsOfCurrentUser" class="oppia-profile-picture">\n          <a href="/preferences" class="oppia-profile-prefererences">\n            <div class="oppia-profile-picture-mask">\n              <div class="oppia-profile-picture-edit-prompt">\n                Edit avatar\n                <i class="material-icons md-18" title="Edit Profile Picture">&#xE254;</i>\n              </div>\n            </div>\n          </a>\n          <img ng-src="<[profilePictureDataUrl]>" class="oppia-profile-picture-fullsize" alt="">\n        </div>\n\n        <img ng-if="!profileIsOfCurrentUser" ng-src="<[profilePictureDataUrl]>"\n             class="oppia-profile-picture-fullsize" alt="">\n      </div>\n\n      <h2 class="oppia-profile-username-large-screen">\n        <span popover-placement="right" ng-attr-uib-popover="<[usernameIsLong ? username.helpText : undefined]>"\n            popover-append-to-body popover-trigger="mouseenter">\n          <strong><[username.value| truncate:16]></strong>\n        </span>\n      </h2>\n      <h2 class="oppia-profile-username-small-screen">\n        <span popover-placement="right" ng-attr-uib-popover="<[username.helpText]>" popover-append-to-body popover-trigger="mouseenter">\n          <strong><[username.value| truncate:11]></strong>\n        </span>\n      </h2>\n\n      <p class="oppia-profile-first-contributed" ng-if="firstContributionMsec">\n        Contributing since: <[getLocaleDateString(firstContributionMsec)]>\n      </p>\n\n      <div class="oppia-profile-user-stat-container-large-screen">\n        <div ng-repeat="stat in userDisplayedStatistics" class="oppia-profile-user-stat">\n          <div popover-placement="right" ng-attr-uib-popover="<[stat.helpText]>" popover-append-to-body popover-trigger="mouseenter">\n            <span style="font-size: 16px"><strong><[stat.value || 0]></strong></span>\n            <span><[stat.title]></span>\n          </div>\n        </div>\n      </div>\n\n      <p class="oppia-profile-user-bio">\n        <span ng-if="userBio" style="white-space: pre-wrap;"><[userBio]></span>\n        <span ng-if="!userBio">\n          <em>This user has not supplied a bio yet.</em>\n        </span>\n      </p>\n\n      <p class="oppia-profile-subject-interest-container">\n        Interests:\n        <span ng-if="subjectInterests.length > 0"><br>\n          <span ng-repeat="interest in subjectInterests track by $index">\n            <span class="oppia-profile-subject-interest"><[interest]></span>\n          </span>\n        </span>\n        <span ng-if="subjectInterests.length === 0" class="oppia-profile-no-interests-text">\n          <em>none specified</em>\n        </span>\n      </p>\n\n      <hr class="oppia-profile-stat-container-line-small-screen">\n      <div class="oppia-profile-user-stat-container-small-screen">\n        <div ng-repeat="stat in userDisplayedStatistics" class="oppia-profile-user-stat">\n          <div popover-placement="right" ng-attr-uib-popover="<[stat.helpText]>" popover-append-to-body popover-trigger="mouseenter">\n            <span style="font-size: 16px"><strong><[stat.value || 0]></strong></span>\n            <span><[stat.title]></span>\n          </div>\n        </div>\n      </div>\n      <hr class="oppia-profile-stat-container-line-small-screen">\n\n      <div ng-if="!isUserVisitingOwnProfile" class="oppia-align-center">\n        <button class="btn oppia-subscription-button oppia-transition-200 protractor-test-subscription-button"\n                ng-click="changeSubscriptionStatus()"\n                popover-placement="right"\n                ng-attr-popover="<[subscriptionButtonPopoverText]>"\n                popover-append-to-body\n                popover-trigger="mouseenter">\n                <span translate="I18N_SUBSCRIBE_BUTTON_TEXT" ng-if="!isAlreadySubscribed"></span>\n                <span translate="I18N_UNSUBSCRIBE_BUTTON_TEXT" ng-if="isAlreadySubscribed"></span>\n        </button>\n      </div>\n    </md-card>\n\n    <md-card class="oppia-profile-content-card">\n      <md-content class="oppia-profile-portfolio-container">\n        <exploration-summary-tile ng-repeat="expl in getExplorationsToDisplay()"\n          exploration-id="expl.id"\n          exploration-title="expl.title"\n          last-updated-msec="expl.last_updated_msec"\n          objective="expl.objective"\n          category="expl.category"\n          ratings="expl.ratings"\n          thumbnail-icon-url="expl.thumbnail_icon_url"\n          thumbnail-bg-color="expl.thumbnail_bg_color"\n          num-views="expl.num_views"\n          is-community-editable="expl.community_editable"\n          mobile-cutoff-px="610">\n        </exploration-summary-tile>\n\n        <div ng-if="userEditedExplorations.length === 0" translate="I18N_PROFILE_NO_EXPLORATIONS">\n          <br><em></em>\n        </div>\n      </md-content>\n\n      <span class="oppia-profile-portfolio-pages" ng-if="numUserPortfolioExplorations > 6">\n        <i class="material-icons md-18" ng-disabled="currentPageNumber == 0"\n           ng-click="goToPreviousPage()">&#xE5C4;</i>\n        Showing <[currentPageNumber * PAGE_SIZE + 1]> - <[Math.min(numUserPortfolioExplorations, (currentPageNumber + 1) * PAGE_SIZE)]> of <[numUserPortfolioExplorations]>\n        <i class="material-icons md-18" ng-disabled="(currentPageNumber + 1) * PAGE_SIZE >= userEditedExplorations.length" ng-click="goToNextPage()">&#xE5C8;</i>\n      </span>\n    </md-card>\n  </div>\n  <style>\n    .oppia-profile-h1 {\n      color: #ffffff;\n      display: inline;\n      font-size: 1em;\n      font-weight: normal;\n    }\n  </style>\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Profile - Oppia\n'

def block_header_js(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_super = context.super('header_js', block_header_js)
    l_0_PROFILE_USERNAME = resolve('PROFILE_USERNAME')
    t_1 = environment.filters['js_string']
    pass
    yield u'\n  %s\n  <script type="text/javascript">\n    GLOBALS.PROFILE_USERNAME = JSON.parse(\n      \'%s\');\n  </script>\n' % (
        escape(context.call(l_0_super)), 
        escape(t_1((undefined(name='PROFILE_USERNAME') if l_0_PROFILE_USERNAME is missing else l_0_PROFILE_USERNAME))), 
    )

def block_navbar_breadcrumb(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    l_0_PROFILE_USERNAME = resolve('PROFILE_USERNAME')
    pass
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      Profile\n      <span class="oppia-navbar-breadcrumb-separator" style="padding-left: 10px;"></span>\n      <h1 class="oppia-profile-h1">%s</h1>\n    </li>\n  </ul>\n' % (
        escape((undefined(name='PROFILE_USERNAME') if l_0_PROFILE_USERNAME is missing else l_0_PROFILE_USERNAME)), 
    )

blocks = {'footer_js': block_footer_js, 'footer': block_footer, 'content': block_content, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&158=17&159=25&160=26&162=27&163=28&164=29&165=30&154=33&155=39&26=44&3=51&7=58&8=67&11=68&15=71&21=78'