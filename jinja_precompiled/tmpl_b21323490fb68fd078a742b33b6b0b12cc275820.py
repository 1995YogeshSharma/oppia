from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/teach/teach.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/teach/teach.html')
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
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/teach/Teach.js"></script>\n  <script src="/templates/dev/head/components/background/BackgroundBannerDirective.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_subtitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Teach\n'

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  '
    template = environment.get_template('pages/footer.html', 'pages/teach/teach.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div class="oppia-static-header">\n    <h1 translate="I18N_TEACH_PAGE_HEADING"></h1>\n  </div>\n  <background-banner></background-banner>\n  <div ng-controller="Teach">\n    <div class="oppia-static-content-below-banner">\n      <div class="oppia-page-card oppia-static-content">\n        <div class="about-nav md-tab oppia-about-teach-tabs">\n          <ul class="oppia-about-tabs">\n            <li class="oppia-about-tabs-active">\n              <a ng-click="onTabClick(TAB_ID_TEACH)" class="oppia-about-tabs-text" href="" id="teach" translate="I18N_TEACH_PAGE_TAB_TEACH_WITH_OPPIA">\n\n              </a>\n            </li>\n            <li>\n              <a ng-click="onTabClick(TAB_ID_PLAYBOOK)" class="oppia-about-tabs-text" href="" id="playbook" translate="I18N_TEACH_PAGE_TAB_PARTICIPATION_PLAYBOOK">\n              </a>\n            </li>\n          </ul>\n        </div>\n\n        <div class="about-tab-container">\n          <div class="teach oppia-about-tab-content oppia-teach-tab-content oppia-about-visible-content">\n\n            <div class="oppia-static-card-content oppia-static-card-content-narrow">\n              <h2>Teach with Oppia</h2>\n              <p>\n                The Oppia team is currently working hard on a series of free online lessons on <strong>basic mathematics</strong>. These lessons are targeted at students who don\'t have good access to textbooks and teachers, but who do have (low-end) mobile devices. We hope students will be able to learn from these lessons at their own pace, supported by useful, targeted feedback.\n              </p>\n              <p>\n                The story-based lessons we\'re creating relate mathematics to a student\'s real-life experience (similar to this <a href="https://www.oppia.org/explore/DIWZiVgs0km-?collection_id=4UgTQUc1tala">sample lesson</a> on Fractions). We want them to be demonstrably effective, to represent the best that can be done with online teaching, and to be available to anyone free-of-charge. We also plan to improve the lessons over time, so that they\'re as useful for as many students around the world as possible.\n              </p>\n              <p>\n                The <a href="https://goo.gl/forms/tDUx4TS6B8Apkqhq2"><em>Teach with Oppia</em></a> program invites applications from volunteers who can demonstrate a passion and aptitude for helping students learn basic mathematics. Participants will receive personalized feedback on the lessons they create, as well as assistance with playtesting and promoting their lessons. They\'ll also be able to connect with other like-minded creators, as well as the Oppia development team, to ensure their creations are well-realized.\n              </p>\n              <p>\n                Although the program runs year-round, we can only accommodate a limited number of participants. However, we are currently accepting submissions on a rolling basis -- so if you love coming up with engaging stories, explaining a topic clearly, or identifying roadblocks that students may run into and helping them overcome these, please don\'t hesitate to get in touch!\n              </p>\n\n            </div>\n            <a ng-click="onApplyToTeachWithOppia()" class="btn oppia-about-button oppia-teach-button"\n               translate="I18N_ACTION_APPLY_TO_TEACH_WITH_OPPIA" target="_blank" tabindex="0">\n            </a>\n          </div>\n\n          <div class="playbook oppia-about-tab-content">\n            <div class="oppia-static-card-content oppia-static-card-content-narrow">\n              <h2 translate="I18N_TEACH_PAGE_COMMUNITY_GUIDELINES_HEADING"></h2>\n              <ol>\n                <li>\n                  <p translate="I18N_TEACH_PAGE_COMMUNITY_GUIDELINES_GUIDELINE_1">\n                  </p>\n                </li>\n                <li>\n                  <p translate="I18N_TEACH_PAGE_COMMUNITY_GUIDELINES_GUIDELINE_2">\n                  </p>\n                </li>\n                <li>\n                  <p translate="I18N_TEACH_PAGE_COMMUNITY_GUIDELINES_GUIDELINE_3">\n                  </p>\n                </li>\n              </ol>\n              <p translate="I18N_TEACH_PAGE_COMMUNITY_GUIDELINES_TEXT">\n              </p>\n\n              <h2 translate="I18N_TEACH_PAGE_PUBLICATION_INSTRUCTIONS_HEADING"></h2>\n\n              <p translate="I18N_TEACH_PAGE_PUBLICATION_INSTRUCTIONS_PARAGRAPH_1">\n              </p>\n\n              <ul style="margin-left: 25px;">\n                <li translate="I18N_TEACH_PAGE_PUBLICATION_INSTRUCTIONS_INSTRUCTION_1">\n                </li>\n                <li translate="I18N_TEACH_PAGE_PUBLICATION_INSTRUCTIONS_INSTRUCTION_2 ">\n                </li>\n                <li translate="I18N_TEACH_PAGE_PUBLICATION_INSTRUCTIONS_INSTRUCTION_3">\n                </li>\n                <li translate="I18N_TEACH_PAGE_PUBLICATION_INSTRUCTIONS_INSTRUCTION_4">\n                </li>\n                <li translate="I18N_TEACH_PAGE_PUBLICATION_INSTRUCTIONS_INSTRUCTION_5">\n                </li>\n                <li translate="I18N_TEACH_PAGE_PUBLICATION_INSTRUCTIONS_INSTRUCTION_6">\n                </li>\n              </ul>\n\n              <p translate="I18N_TEACH_PAGE_PUBLICATION_INSTRUCTIONS_PARAGRAPH_2">\n              </p>\n\n              <h2 translate="I18N_TEACH_PAGE_PUBLICATION_POLICY_HEADING"></h2>\n\n              <p translate="I18N_TEACH_PAGE_PUBLICATION_POLICY_PARAGRAPH_1">\n              </p>\n              <p translate="I18N_TEACH_PAGE_PUBLICATION_POLICY_PARAGRAPH_2">\n              </p>\n            </div>\n          </div>\n        </div>\n      </div>\n\n      <div class="oppia-about-extra-container about-tab-container">\n        <div class="oppia-about-tab-content oppia-about-visible-content">\n          <div class="oppia-about-extra-info">\n            <div class="oppia-static-content oppia-static-extra-content oppia-about-extra-content">\n              <div class="oppia-static-card-content oppia-static-card-content-wide oppia-about-buttons-container">\n                <a href="/creator_dashboard?mode=create" class="btn oppia-about-button"\n                   translate="I18N_ACTION_CREATE_EXPLORATION">\n                </a>\n                <a href="/library" class="btn oppia-about-button"\n                   translate="I18N_ACTION_BROWSE_EXPLORATIONS">\n                </a>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n  <div class="oppia-footer-padding-below-banner">\n  </div>\n  <style>\n    .oppia-teach-tab-content {\n      padding-bottom: 7%;\n    }\n    .oppia-teach-button{\n      display: block;\n      margin: 0 auto 0 auto;\n    }\n  </style>\n'

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
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      Teach with Oppia\n    </li>\n  </ul>\n'

blocks = {'footer_js': block_footer_js, 'subtitle': block_subtitle, 'footer': block_footer, 'content': block_content, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&151=17&152=24&3=27&157=34&158=40&20=45&7=52&8=59&11=62'