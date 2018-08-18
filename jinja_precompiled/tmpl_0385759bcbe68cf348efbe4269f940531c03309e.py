from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/splash/splash_ah2.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/splash/splash_ah2.html')
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
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/splash/Splash.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_prerender(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <link rel="prerender" href="/library">\n'

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  '
    template = environment.get_template('pages/footer.html', 'pages/splash/splash_ah2.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div ng-controller="Splash">\n    <div class="oppia-splash-section-one text-center">\n      <h1 class="oppia-splash-h1" style="max-width: 800px; font-size: 2.3em; line-height: 1.5em; padding-bottom: 0.5em;">Students don\'t want to do homework?</h1>\n\n      <div class="oppia-splash-button-heading">\n        <h2 style="max-width: 400px; color: #005c53; font-size: 1.6em; font-family: Capriola; line-height: 1.5em;">\n          Transform your existing homework exercises into fun online activities.\n        </h2>\n      </div>\n\n      <div style="position: relative;">\n        <div style="padding-left: 200px;">\n          <div class="oppia-splash-background-icon-row">\n            <img ng-src="<[getStaticImageUrl(\'/splash/books.svg\')]>" class="oppia-splash-books" style="margin-left: -250px; width: 500px; top: 95px;" alt="">\n\n            <img ng-src="<[getStaticSubjectImageUrl(\'Humor\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Combinatorics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Cooking\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Government\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Architecture\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'History\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Microbiology\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Engineering\')]>" class="oppia-splash-background-icon" alt="">\n\n            <img ng-src="<[getStaticSubjectImageUrl(\'Algorithms\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Economics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Computing\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Reading\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Art\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Creativity\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Physics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Language\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Arithmetic\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Chess\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Astronomy\')]>" class="oppia-splash-background-icon" alt="">\n\n            <img ng-src="<[getStaticSubjectImageUrl(\'Religion\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Mathematics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Philosophy\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Humor\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Combinatorics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Cooking\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Government\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Architecture\')]>" class="oppia-splash-background-icon" alt="">\n          </div>\n\n          <div class="oppia-splash-background-icon-row">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Genetics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Space\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Algebra\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Music\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Chemistry\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Poetry\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Puzzles\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Calculus\')]>" class="oppia-splash-background-icon" alt="">\n\n            <img ng-src="<[getStaticSubjectImageUrl(\'Business\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Geography\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Biology\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Genetics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Space\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Algebra\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Music\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Chemistry\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Poetry\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Puzzles\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Calculus\')]>" class="oppia-splash-background-icon" alt="">\n\n            <img ng-src="<[getStaticSubjectImageUrl(\'Business\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Geography\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Biology\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Genetics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Space\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Algebra\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Music\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Chemistry\')]>" class="oppia-splash-background-icon" alt="">\n          </div>\n\n          <div class="oppia-splash-background-icon-row">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Economics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Algorithms\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Creativity\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Astronomy\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Chess\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Arithmetic\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Language\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Physics\')]>" class="oppia-splash-background-icon" alt="">\n\n            <img ng-src="<[getStaticSubjectImageUrl(\'Combinatorics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Humor\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Philosophy\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Mathematics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Religion\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Cooking\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Engineering\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Microbiology\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'History\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Architecture\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Government\')]>" class="oppia-splash-background-icon" alt="">\n\n            <img ng-src="<[getStaticSubjectImageUrl(\'Art\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Reading\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Computing\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Economics\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Algorithms\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Creativity\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Astronomy\')]>" class="oppia-splash-background-icon" alt="">\n            <img ng-src="<[getStaticSubjectImageUrl(\'Chess\')]>" class="oppia-splash-background-icon" alt="">\n          </div>\n        </div>\n\n        <div class="oppia-splash-button-container">\n          <!-- User must complete the registration process. -->\n          <button type="button"\n                  ng-if="!userIsLoggedIn"\n                  ng-click="onRedirectToLogin(\'/creator_dashboard?mode=create\')"\n                  class="btn oppia-splash-button oppia-splash-button-create oppia-transition-200"\n                  style="left: -webkit-calc(130px + 15%); left: -moz-calc(130px + 15%); left: -o-calc(130px + 15%); left: calc(130px + 15%); bottom: 210px; z-index: 10;"\n                  translate="I18N_ACTION_CREATE_LESSON">\n          </button>\n          <button type="button"\n                  ng-if="userIsLoggedIn"\n                  ng-click="onClickCreateExplorationButton()"\n                  class="btn oppia-splash-button oppia-splash-button-create oppia-transition-200"\n                  style="left: -webkit-calc(130px + 15%); left: -moz-calc(130px + 15%); left: -o-calc(130px + 15%); left: calc(130px + 15%); bottom: 210px; z-index: 10;"\n                  translate="I18N_ACTION_CREATE_LESSON">\n          </button>\n          <button type="button" ng-click="onClickBrowseLibraryButton()"\n                  class="btn oppia-splash-button oppia-splash-button-browse oppia-transition-200"\n                  style="left: -webkit-calc(130px + 15%); left: -moz-calc(130px + 15%); left: -o-calc(130px + 15%); left: calc(130px + 15%); bottom: 150px; font-size: 0.93em; z-index: 10;"\n                  translate="I18N_ACTION_BROWSE_LESSONS">\n          </button>\n        </div>\n      </div>\n\n      <div class="oppia-splash-h2-container">\n        <h2 class="oppia-splash-h2" style="padding-bottom: 30px; font-size: 1.6em; padding-top: 100px; max-width: 700px;">\n        </h2>\n      </div>\n    </div>\n\n    <div class="oppia-splash-section-two">\n      <div class="oppia-splash-section-two-content" style="padding-top: 0;">\n        <div class="oppia-splash-bullet" style="overflow: visible;">\n          <div class="oppia-splash-bullet-block oppia-splash-block-left-image">\n            <img ng-src="<[getStaticImageUrl(\'/splash/bullet1icon.svg\')]>" class="oppia-splash-overlapping-image-1" alt="">\n          </div>\n          <div class="oppia-splash-bullet-block oppia-splash-block-right-text"\n               translate="I18N_SPLASH_FIRST_EXPLORATION_DESCRIPTION">\n          </div>\n        </div>\n\n        <div class="oppia-splash-bullet" style="clear: both;">\n          <div class="oppia-splash-bullet-block oppia-splash-block-right-image">\n            <img ng-src="<[getStaticImageUrl(\'/splash/bullet2icon.svg\')]>" alt="">\n          </div>\n          <div class="oppia-splash-bullet-block oppia-splash-block-left-text"\n               translate="I18N_SPLASH_SECOND_EXPLORATION_DESCRIPTION">\n          </div>\n        </div>\n\n        <div class="oppia-splash-bullet">\n          <div class="oppia-splash-bullet-block oppia-splash-block-left-image">\n            <img ng-src="<[getStaticImageUrl(\'/splash/bullet3icon.svg\')]>" alt="">\n          </div>\n          <div class="oppia-splash-bullet-block oppia-splash-block-right-text"\n               translate="I18N_SPLASH_THIRD_EXPLORATION_DESCRIPTION">\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <style>\n    @media (min-width: 608px) {\n      .oppia-splash-overlapping-image-1 {\n        margin-top: -105px;\n      }\n    }\n\n    @media (max-width: 608px) {\n      .oppia-splash-overlapping-image-1 {\n        margin-top: -30px;\n      }\n    }\n  </style>\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  I18N_SPLASH_PAGE_TITLE\n'

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
    yield u'\n'

blocks = {'footer_js': block_footer_js, 'prerender': block_prerender, 'footer': block_footer, 'content': block_content, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&211=17&212=24&3=27&207=34&208=40&18=45&7=52&11=59&12=66&15=69'