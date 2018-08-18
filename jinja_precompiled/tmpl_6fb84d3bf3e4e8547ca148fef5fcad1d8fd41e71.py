from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/donate/donate.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('pages/base.html', 'pages/donate/donate.html')
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
    yield u'\n  %s\n  <script src="/templates/dev/head/pages/donate/Donate.js"></script>\n' % (
        escape(context.call(l_0_super)), 
    )

def block_footer(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  '
    template = environment.get_template('pages/footer.html', 'pages/donate/donate.html')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    yield u'\n'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  <div class="oppia-page-card oppia-static-content" ng-controller="Donate">\n    <div class="oppia-donation-card-content-wide">\n      <div class="oppia-donate-options">\n        <div ng-if="windowIsNarrow">\n          <h1 class="oppia-donate-h1">Donate to the <br>\n          Oppia Foundation</h1>\n        </div>\n        <div ng-if="!windowIsNarrow">\n          <h1 class="oppia-donate-h1">Donate to <br>\n          The Oppia Foundation</h1>\n        </div>\n        <div style="text-align: center;">\n          <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top" ng-submit="onDonateThroughPayPal()">\n            <input type="hidden" name="cmd" value="_s-xclick">\n            <input type="hidden" name="hosted_button_id" value="UWKTY87SYU766">\n            <button class="btn oppia-donate-options-button" tabindex="0">\n              PayPal\n            </button>\n          </form>\n        </div>\n        <div style="text-align: center;">\n          <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top" ng-submit="onDonateThroughPayPal()">\n            <input type="hidden" name="cmd" value="_s-xclick">\n            <input type="hidden" name="hosted_button_id" value="UWKTY87SYU766">\n            <button class="btn oppia-donate-options-button" tabindex="0">\n              Credit Card\n            </button>\n          </form>\n        </div>\n        <div style="text-align: center;">\n          <a ng-click="onDonateThroughAmazon()" class="btn oppia-donate-options-button" tabindex="0">Amazon Smile</a>\n        </div>\n        <h2 style="color: #fff; font-size: 20px; margin-bottom: 20px; margin-top: 20px;">\n          Your generous gift funds:\n        </h2>\n        <div style="margin-bottom: 16px; text-align: center;">\n          <img ng-src="<[donateImgUrl]>" alt="Server costs, student outreach, marketing">\n        </div>\n      </div>\n      <div class="oppia-donate-info">\n        <div style="height: 0; margin: 60px auto 0px auto; width: 70%; padding-bottom: 56.25%; position: relative;">\n          <iframe title="Meet Oppia\'s Contributors" width="100%"\n                  height="100%" src="https://www.youtube.com/embed/OConyxG7HaM?rel=0&cc_lang_pref=en&cc_load_policy=1"\n                  frameborder="0" allowfullscreen\n                  style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">\n          </iframe>\n        </div>\n        <h3 class="oppia-donate-h3"><em>Hear from our Oppia community</em></h3>\n        <div style="margin: 0 auto; width: 70%;">\n          <p style="font-size: 0.825em;">\n            In 2012, Oppia started with a simple idea: to improve the education of\n            students around the world while improving the quality of teaching.\n            This vision has since turned into an educational platform with over\n            11,000 explorations that have been used by more than 430,000 users\n            worldwide.\n          </p>\n          <p style="font-size: 0.825em;">\n            Please donate to The Oppia Foundation, a registered 501(c)(3) nonprofit,\n            and join us in bringing the joys of teaching and learning to people\n            everywhere.\n          </p>\n        </div>\n      </div>\n\n    </div>\n  </div>\n  <style>\n    h1.oppia-donate-h1 {\n      color: #fff;\n      font-size: 1.5em;\n      margin-top: 60px;\n      text-align: center;\n      line-height: 1.7em;\n    }\n    h3.oppia-donate-h3 {\n      font-size: .75em;\n      font-weight: normal;\n      margin: 2.33em 0;\n      text-align: center;\n    }\n    .oppia-donation-card-content-wide {\n      margin: 40px auto 80px;\n      min-height: 670px;\n      overflow: auto;\n    }\n    .oppia-donate-options {\n      background-color: #009688;\n      display: block;\n      float: right;\n      font-family: "Capriola", "Roboto", Arial, sans-serif;\n      padding: 10px 10px 35px 10px;\n      width: 340px;\n    }\n    .btn.oppia-donate-options-button {\n      background-color: rgba(0,0,0,0.2);\n      color: rgba(255,255,255,1.0);\n      font-family: "Capriola", "Roboto", Arial, sans-serif;\n      font-size: 16px;\n      height: 40px;\n      margin: 10px auto;\n      width: 180px;\n    }\n    .btn.oppia-donate-options-button:hover,\n    .btn.oppia-donate-options-button:focus {\n      background-color: rgba(5, 190, 178, 1);\n      color: rgba(255,255,255,1);\n    }\n    .oppia-donate-info {\n      float: left;\n      padding-bottom: 30px;\n      width: -webkit-calc(100% - 340px);\n      width: -moz-calc(100% - 340px);\n      width: -o-calc(100% - 340px);\n      width: calc(100% - 340px);\n    }\n    @media only screen and (max-width: 1140px) {\n      .oppia-donation-card-content-wide {\n        margin-bottom: 90px;\n      }\n      .oppia-donate-info {\n        display: block;\n        position: inherit;\n        width: 100%;\n      }\n      .oppia-donate-options {\n        float: clear;\n        width: 100%;\n      }\n    }\n  </style>\n'

def block_maintitle(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'\n  Donate - Oppia\n'

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
    yield u'\n  <ul class="nav navbar-nav oppia-navbar-breadcrumb">\n    <li>\n      <span class="oppia-navbar-breadcrumb-separator"></span>\n      Donate\n    </li>\n  </ul>\n'

blocks = {'footer_js': block_footer_js, 'footer': block_footer, 'content': block_content, 'maintitle': block_maintitle, 'header_js': block_header_js, 'navbar_breadcrumb': block_navbar_breadcrumb}
debug_info = '1=11&153=17&154=24&158=27&159=33&20=38&3=45&7=52&8=59&11=62'