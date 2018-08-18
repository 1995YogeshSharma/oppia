from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/exploration_editor/translation_tab/translator_overview_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-translator-overview">\n  <div>\n    <span style="font-size: 16px;">\n      <strong>Translation in language:</strong>\n    </span>\n    <select id="audioTranslationLanguageCodeField" class="oppia-translation-language-selector protractor-test-translation-language-selector" ng-change="changeTranslationLanguage()" ng-model="languageCode"\n            ng-options="language.id as language.description for language in languageCodesAndDescriptions">\n    </select>\n  </div>\n  <div class="oppia-translation-progress">\n    <div class="oppia-progress-info">\n      <strong>Exploration translation progress:</strong>\n    </div>\n    <div class="progress oppia-translation-progess-bar">\n      <div class="progress-bar progress-bar-success" role="progressbar" ng-style="getTranslationProgressStyle()"></div>\n    </div>\n  </div>\n</div>\n\n<style>\n  .oppia-translator-overview {\n    width: 600px;\n    height: 45px;\n    padding-top: 5px;\n    text-align: center;\n    margin: 0 auto;\n  }\n  .oppia-progress-info {\n    display: -webkit-flex;\n    display: flex;\n    width: 250px;\n    font-size: 16px;\n  }\n  .oppia-translation-progress {\n    display: -webkit-flex;\n    display: flex;\n    margin-top: 8px;\n  }\n  .oppia-translation-progess-bar {\n    display: -webkit-flex;\n    display: flex;\n    margin-top: 5px;\n    width: 350px;\n    height: 10px;\n  }\n  .oppia-translation-language-selector {\n    padding: 2px;\n    border-radius: 8px;\n  }\n</style>'

blocks = {}
debug_info = ''