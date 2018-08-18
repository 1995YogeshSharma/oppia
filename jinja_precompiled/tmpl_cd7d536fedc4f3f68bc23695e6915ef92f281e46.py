from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/forms/html_select_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div uib-dropdown class="oppia-html-select">\n  <button uib-dropdown-toggle class="btn btn-default oppia-html-select-selection" type="button" aria-expanded="false" data-toggle="dropdown">\n    <div>\n      <angular-html-bind class="oppia-html-select-selection-element" html-data="options[getSelectionIndex()].val">\n      </angular-html-bind>\n    </div>\n    <span class="caret oppia-html-select-selection-caret"></span>\n  </button>\n  <ul uib-dropdown-menu style="width: inherit;">\n    <li ng-repeat="choice in options">\n      <a>\n        <angular-html-bind class="oppia-html-select-option protractor-test-html-select-option" html-data="choice.val" ng-click="select(choice.id)">\n        </angular-html-bind>\n      </a>\n    </li>\n  </ul>\n</div>\n\n<style>\n  .oppia-html-select {\n    position: relative;\n    width: 80%;\n  }\n  .oppia-html-select .oppia-html-select-selection-element {\n    overflow: hidden;\n    padding-top: 5px;\n  }\n  .oppia-html-select .oppia-html-select-selection-caret {\n    bottom: 0;\n    color: black;\n    margin: auto;\n    position: absolute;\n    right: 5px;\n    top: 0;\n  }\n  .oppia-html-select .oppia-html-select-selection {\n    padding-right: 20px;\n    position: relative;\n    text-decoration: none;\n    width: inherit;\n  }\n  .oppia-html-select .oppia-html-select-option {\n    padding-top: 10px;\n    overflow: hidden;\n    margin-right: 10px;\n  }\n  .oppia-html-select .oppia-html-select-option:hover {\n    background: #1485E6;\n    color: white;\n  }\n  .oppia-html-select .oppia-html-select-option oppia-noninteractive-image {\n    display: inline-block;\n    margin-bottom: 0;\n  }\n\n</style>'

blocks = {}
debug_info = ''