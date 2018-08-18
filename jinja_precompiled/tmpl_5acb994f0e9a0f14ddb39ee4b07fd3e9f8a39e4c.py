from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/summary_list_header_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<style>\n  summary-list-header .oppia-delete-example-button {\n    cursor: pointer;\n    opacity: 0.5;\n    position: absolute;\n    right: 8px;\n    top: 8px;\n    width: 20px;\n  }\n\n  summary-list-header .oppia-delete-example-button:hover {\n    opacity: 1;\n  }\n\n  summary-list-header .oppia-example-header-block {\n    overflow: hidden;\n    padding-left: 24px;\n    white-space: nowrap;\n  }\n\n  summary-list-header .oppia-example-header {\n    float: left;\n    overflow: hidden;\n    text-overflow: ellipsis;\n    white-space: nowrap;\n    width: 80%;\n  }\n\n  /* This is to break the line only when screen is too narrow to have both divs\n     in same line.*/\n  @media screen and (min-width: 370px) {\n    summary-list-header .break-in-mobile {\n      display: none;\n    }\n  }\n</style>\n<div class="oppia-example-header-block">\n  <div class="oppia-example-header">\n    <span ng-if="!isActive()" ng-attr-title="<[getSummary()]>">\n      <[getShortSummary()]>\n      <span ng-if="getNumItems() > 1" class="label label-primary" style="position: relative; bottom: 4px;">\n        +<[getNumItems() - 1]>\n      </span>\n    </span>\n    <span ng-if="isActive()">&nbsp;</span>\n  </div>\n</div>\n\n<span class="oppia-delete-example-button oppia-transition-200"\n      ng-if="isDeleteAvailable() && getOnDeleteFn()"\n      ng-click="deleteItem($event)">\n  <i class="material-icons md-18">&#xE5CD;</i>\n</span>'

blocks = {}
debug_info = ''