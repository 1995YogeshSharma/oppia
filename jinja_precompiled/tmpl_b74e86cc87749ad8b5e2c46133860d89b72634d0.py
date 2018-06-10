from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/RatingDisplayDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for displaying summary rating information.\n */\n\noppia.directive(\'ratingDisplay\', [\n  \'UrlInterpolationService\', function(UrlInterpolationService) {\n    return {\n      // This will display a star-rating based on the given data. The attributes\n      // passed in are as follows:\n      //  - isEditable: true or false; whether the rating is user-editable.\n      //  - onEdit: should be supplied iff isEditable is true, and be a function\n      //    that will be supplied with the new rating when the rating is\n      //    changed.\n      //  - ratingValue: an integer 1-5 giving the rating\n      restrict: \'E\',\n      scope: {\n        isEditable: \'=\',\n        onEdit: \'=\',\n        ratingValue: \'=\'\n      },\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/components/rating_display_directive.html\'),\n      link: function(scope, element) {\n        // This is needed in order for the scope to be retrievable during Karma\n        // unit testing. See http://stackoverflow.com/a/29833832 for more\n        // details.\n        element[0].getControllerScope = function() {\n          return scope;\n        };\n      },\n      controller: [\'$scope\', function($scope) {\n        var POSSIBLE_RATINGS = [1, 2, 3, 4, 5];\n        $scope.stars = POSSIBLE_RATINGS.map(function(starValue) {\n          return {\n            cssClass: \'fa-star-o\',\n            value: starValue\n          };\n        });\n\n        var STATUS_ACTIVE = \'active\';\n        var STATUS_INACTIVE = \'inactive\';\n        var STATUS_RATING_SET = \'rating_set\';\n        $scope.status = STATUS_INACTIVE;\n\n        var displayValue = function(ratingValue) {\n          for (var i = 0; i < $scope.stars.length; i++) {\n            $scope.stars[i].cssClass = (\n              ratingValue === undefined ? \'fa-star-o\' :\n              ratingValue < $scope.stars[i].value - 0.75 ? \'fa-star-o\' :\n              ratingValue < $scope.stars[i].value - 0.25 ? \'fa-star-half-o\' :\n              \'fa-star\');\n\n            if ($scope.status === STATUS_ACTIVE &&\n                ratingValue >= $scope.stars[i].value) {\n              $scope.stars[i].cssClass += \' oppia-rating-star-active\';\n            }\n          }\n        };\n\n        displayValue($scope.ratingValue);\n        $scope.$watch(\'ratingValue\', function() {\n          displayValue($scope.ratingValue);\n        });\n\n        $scope.clickStar = function(starValue) {\n          if ($scope.isEditable && $scope.status === STATUS_ACTIVE) {\n            $scope.status = STATUS_RATING_SET;\n            $scope.ratingValue = starValue;\n            displayValue(starValue);\n            $scope.onEdit(starValue);\n          }\n        };\n        $scope.enterStar = function(starValue) {\n          var starsHaveNotBeenClicked = (\n            $scope.status === STATUS_ACTIVE ||\n            $scope.status === STATUS_INACTIVE);\n          if ($scope.isEditable && starsHaveNotBeenClicked) {\n            $scope.status = STATUS_ACTIVE;\n            displayValue(starValue);\n          }\n        };\n        $scope.leaveArea = function() {\n          $scope.status = STATUS_INACTIVE;\n          displayValue($scope.ratingValue);\n        };\n\n        $scope.getCursorStyle = function() {\n          return \'cursor: \' + ($scope.isEditable ? \'pointer\' : \'auto\');\n        };\n      }]\n    };\n  }\n]);'

blocks = {}
debug_info = ''