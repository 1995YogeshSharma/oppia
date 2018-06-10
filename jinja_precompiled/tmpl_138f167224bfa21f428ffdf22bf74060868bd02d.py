from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'pages/about/About.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2016 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Controllers for the about page.\n */\n\noppia.controller(\'About\', [\n  \'$scope\', \'UrlInterpolationService\',\n  function($scope, UrlInterpolationService) {\n    // Define constants\n    $scope.TAB_ID_ABOUT = \'about\';\n    $scope.TAB_ID_FOUNDATION = \'foundation\';\n    $scope.TAB_ID_CREDITS = \'credits\';\n\n    var activeTabClass = \'oppia-about-tabs-active\';\n    var hash = window.location.hash.slice(1);\n    var visibleContent = \'oppia-about-visible-content\';\n\n    var activateTab = function(tabName) {\n      $("a[id=\'" + tabName + "\']").parent().addClass(\n        activeTabClass\n      ).siblings().removeClass(activeTabClass);\n      $(\'.\' + tabName).addClass(visibleContent).siblings().removeClass(\n        visibleContent\n      );\n    };\n\n    if (hash === $scope.TAB_ID_FOUNDATION || hash === \'license\') {\n      activateTab($scope.TAB_ID_FOUNDATION);\n    }\n\n    if (hash === $scope.TAB_ID_CREDITS) {\n      activateTab($scope.TAB_ID_CREDITS);\n    }\n\n    if (hash === $scope.TAB_ID_ABOUT) {\n      activateTab($scope.TAB_ID_ABOUT);\n    }\n\n    window.onhashchange = function() {\n      var hashChange = window.location.hash.slice(1);\n      if (hashChange === $scope.TAB_ID_FOUNDATION || hashChange === \'license\') {\n        activateTab($scope.TAB_ID_FOUNDATION);\n        // Ensure page goes to the license section\n        if (hashChange === \'license\') {\n          location.reload(true);\n        }\n      } else if (hashChange === $scope.TAB_ID_CREDITS) {\n        activateTab($scope.TAB_ID_CREDITS);\n      } else if (hashChange === $scope.TAB_ID_ABOUT) {\n        activateTab($scope.TAB_ID_ABOUT);\n      }\n    };\n\n    var listOfNamesToThank = [\n      \'Alex Kauffmann\', \'Allison Barros\',\n      \'Amy Latten\', \'Brett Barros\',\n      \'Crystal Kwok\', \'Daniel Hernandez\',\n      \'Divya Siddarth\', \'Ilwon Yoon\',\n      \'Jennifer Chen\', \'John Cox\',\n      \'John Orr\', \'Katie Berlent\',\n      \'Michael Wawszczak\', \'Mike Gainer\',\n      \'Neil Fraser\', \'Noah Falstein\',\n      \'Nupur Jain\', \'Peter Norvig\',\n      \'Philip Guo\', \'Piotr Mitros\',\n      \'Rachel Chen\', \'Rahim Nathwani\',\n      \'Robyn Choo\', \'Tricia Ngoon\',\n      \'Vikrant Nanda\', \'Vinamrata Singal\',\n      \'Yarin Feigenbaum\'];\n\n    $scope.onTabClick = function(tabName) {\n      // Update hash\n      window.location.hash = \'#\' + tabName;\n      activateTab(tabName);\n    };\n    $scope.listOfNames = listOfNamesToThank\n      .slice(0, listOfNamesToThank.length - 1).join(\', \') +\n      \' & \' + listOfNamesToThank[listOfNamesToThank.length - 1];\n    $scope.getStaticImageUrl = UrlInterpolationService.getStaticImageUrl;\n    $scope.aboutPageMascotImgUrl = UrlInterpolationService.getStaticImageUrl(\n      \'/general/about_page_mascot.png\');\n  }\n]);'

blocks = {}
debug_info = ''