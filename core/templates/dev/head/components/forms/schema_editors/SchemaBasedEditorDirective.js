// Copyright 2016 The Oppia Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * @fileoverview Directive for general schema-based editors.
 */

oppia.directive('schemaBasedEditor', [
  'UrlInterpolationService', function(UrlInterpolationService) {
    return {
      scope: {
        schema: '&',
        isDisabled: '&',
        localValue: '=',
        allowExpressions: '&',
        labelForFocusTarget: '&',
        onInputBlur: '=',
        onInputFocus: '='
      },
      templateUrl: UrlInterpolationService.getComponentUrl(
        '/forms/schema_editors/Schema_based_editor_directive.html'),
      restrict: 'E'
    };
  }]);
