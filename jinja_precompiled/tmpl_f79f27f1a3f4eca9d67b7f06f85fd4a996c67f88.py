from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/library/search_bar_directive.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'<div class="oppia-same-row-container">\n  <form class="navbar-form navbar-left oppia-search-bar-form" role="search">\n    <div class="form-group">\n      <div class="input-group" style="max-width: 375px; width: auto;">\n        <div class="input-group-addon oppia-search-bar-icon">\n          <i class="material-icons md-18" ng-if="!isSearchInProgress()">&#xE8B6;</i>\n          <span ng-if="isSearchInProgress()">\n            <i class="material-icons md-18 oppia-animate-spin">&#xE863;</i>\n          </span>\n        </div>\n        <input type="text" class="form-control oppia-search-bar-input oppia-search-bar-text-input protractor-test-search-input"\n             ng-attr-placeholder="<[searchBarPlaceholder]>" ng-model="searchQuery"\n             ng-model-options="{ updateOn: \'default blur\', debounce: { \'default\': 1000, \'blur\': 0 } }" aria-label="Search bar">\n      </div>\n    </div>\n  </form>\n</div>\n\n<div class="oppia-same-row-container">\n  <div uib-dropdown class="navbar-left oppia-navbar-button-container oppia-search-bar-category-selector protractor-test-search-bar-category-selector">\n    <button uib-dropdown-toggle type="button" class="btn protractor-test-search-bar-dropdown-toggle oppia-search-bar-input ng-cloak"\n          title="<[selectionDetails.categories.description | translate]>"\n          style="max-width: 130px;">\n      <[categoryButtonText|truncate:14]>\n      <span class="caret"></span>\n    </button>\n    <!-- The $event.stopPropagation() prevents the dropdown from closing after an option is selected. -->\n    <ul uib-dropdown-menu class="protractor-test-search-bar-dropdown-menu" role="menu" style="max-height: 400px; overflow: auto;" ng-click="$event.stopPropagation()">\n      <li ng-repeat="item in selectionDetails.categories.masterList track by $index"\n        ng-if="selectionDetails.categories.selections[item.id]">\n        <a href="" ng-click="toggleSelection(\'categories\', item.id)">\n          <span translate="<[item.text]>" class="protractor-test-selected"></span>\n          <i ng-if="selectionDetails.categories.selections[item.id]" class="material-icons md-18 pull-right oppia-search-bar-category-selection-symbol">&#xE876;</i>\n        </a>\n      </li>\n      <li ng-if="selectionDetails.categories.numSelections > 1">\n        <a href="" ng-click="deselectAll(\'categories\')"><i>Deselect All</i></a>\n      </li>\n      <hr ng-if="selectionDetails.categories.numSelections > 0" style="margin: 2px;">\n      <li ng-repeat="item in selectionDetails.categories.masterList track by $index"\n          ng-if="!selectionDetails.categories.selections[item.id]">\n        <a href="" ng-click="toggleSelection(\'categories\', item.id)">\n          <span translate="<[item.text]>" class="protractor-test-deselected"></span>\n          <i ng-if="selectionDetails.categories.selections[item.id]" class="material-icons md-18 pull-right oppia-search-bar-category-selection-symbol">&#xE876;</i>\n        </a>\n      </li>\n    </ul>\n  </div>\n</div>\n<div uib-dropdown class="navbar-left oppia-navbar-button-container oppia-search-bar-language-selector protractor-test-search-bar-language-selector">\n  <button uib-dropdown-toggle type="button" class="btn protractor-test-search-bar-dropdown-toggle oppia-search-bar-input ng-cloak"\n          style="border-bottom-right-radius: 4px; border-top-right-radius: 4px; max-width: 130px;"\n          title="<[selectionDetails.languageCodes.description | translate]>">\n    <[languageButtonText|truncate:14]>\n    <span class="caret"></span>\n  </button>\n  <!-- The $event.stopPropagation() prevents the dropdown from closing after an option is selected. -->\n  <ul uib-dropdown-menu class="protractor-test-search-bar-dropdown-menu" role="menu" style="max-height: 400px; overflow: auto;" ng-click="$event.stopPropagation()">\n    <li ng-repeat="item in selectionDetails.languageCodes.masterList track by $index"\n        ng-if="selectionDetails.languageCodes.selections[item.id]">\n      <a href="" ng-click="toggleSelection(\'languageCodes\', item.id)">\n        <span translate="<[item.text]>" class="protractor-test-selected"></span>\n        <i ng-if="selectionDetails.languageCodes.selections[item.id]" class="material-icons md-18 pull-right oppia-search-bar-category-selection-symbol">&#xE876;</i>\n      </a>\n    </li>\n    <li ng-if="selectionDetails.languageCodes.numSelections > 1">\n      <a href="" ng-click="deselectAll(\'languageCodes\')"><i>Deselect All</i></a>\n    </li>\n    <hr ng-if="selectionDetails.languageCodes.numSelections > 0" style="margin: 2px;">\n    <li ng-repeat="item in selectionDetails.languageCodes.masterList track by $index"\n        ng-if="!selectionDetails.languageCodes.selections[item.id]">\n      <a href="" ng-click="toggleSelection(\'languageCodes\', item.id)">\n        <span translate="<[item.text]>" class="protractor-test-deselected"></span>\n        <i ng-if="selectionDetails.languageCodes.selections[item.id]" class="material-icons md-18  pull-right oppia-search-bar-category-selection-symbol">&#xE876;</i>\n      </a>\n    </li>\n  </ul>\n</div>\n\n<style>\n  .oppia-search-bar-form {\n    margin-top: 10px;\n    padding-right: 0;\n  }\n\n  .oppia-search-bar-input {\n    background: #04857c;\n    border: 1px solid #018c7f;\n    border-radius: 0;\n    color: white;\n    font-size: 15px;\n    height: 34px;\n  }\n\n  .oppia-search-bar-input.btn {\n    color: rgba(255,255,255,0.7);\n  }\n  .oppia-search-bar-input.btn:hover,\n  .oppia-search-bar-input.btn:focus {\n    color: #fff;\n  }\n\n  .oppia-search-bar-input.btn:focus {\n    outline: 1px dotted #fff;\n    outline: auto 5px -webkit-focus-ring-color;\n  }\n\n  .oppia-search-bar-input::-webkit-input-placeholder {\n    color: rgba(255,255,255,0.7);\n  }\n  .oppia-search-bar-input:-moz-placeholder {\n    color: rgba(255,255,255,0.7);\n  }\n  .oppia-search-bar-input::-moz-placeholder {\n    color: rgba(255,255,255,0.7);\n  }\n  .oppia-search-bar-input:-ms-input-placeholder {\n    color: rgba(255,255,255,0.7);\n  }\n\n  .oppia-search-bar-icon {\n    background: #04857c;\n    border: 1px solid #018c7f;\n    color: rgba(255,255,255,0.7);\n  }\n\n  @media (max-width: 1024px) {\n    .oppia-search-bar-language-selector {\n      display: none;\n    }\n    .oppia-search-bar-category-selector .btn {\n      border-bottom-right-radius: 4px;\n      border-top-right-radius: 4px;\n    }\n  }\n\n  @media (max-width: 767px) {\n    .oppia-search-bar-input {\n      background: #ffffff;\n      color: #04857c;\n    }\n    .oppia-search-bar-input::-webkit-input-placeholder {\n      color: #04857c;\n    }\n    .oppia-search-bar-input:-moz-placeholder {\n      color: #04857c;\n    }\n    .oppia-search-bar-input::-moz-placeholder {\n      color: #04857c;\n    }\n    .oppia-search-bar-input:-ms-input-placeholder {\n      color: #04857c;\n    }\n    .oppia-search-bar-icon {\n      background: #ffffff;\n      color: #04857c;\n    }\n    .oppia-search-bar-input.btn {\n      color: #04857c;\n      margin-left: 10px;\n      margin-top: -64px;\n    }\n    .oppia-search-bar-input.btn:hover, .oppia-search-bar-input.btn:focus {\n      color: #04857c;\n    }\n    .protractor-test-search-bar-dropdown-menu {\n      margin-top: -25px;\n    }\n    .oppia-same-row-container {\n       display: inline-block;\n    }\n  }\n\n  @media (max-width: 629px) {\n    .oppia-search-bar-text-input {\n      border-bottom-right-radius: 4px;\n      border-top-right-radius: 4px;\n    }\n    .oppia-search-bar-category-selector {\n      display: none;\n    }\n  }\n  /* This rule targets only Firefox browsers. */\n  @-moz-document url-prefix() {\n    .oppia-search-bar-category-selection-symbol {\n      margin-top: -18px;\n    }\n  }\n\n</style>'

blocks = {}
debug_info = ''