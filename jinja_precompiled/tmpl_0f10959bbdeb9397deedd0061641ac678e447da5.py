from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound, Namespace
name = 'components/RuleEditorDirective.js'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    if 0: yield None
    pass
    yield u'// Copyright 2014 The Oppia Authors. All Rights Reserved.\n//\n// Licensed under the Apache License, Version 2.0 (the "License");\n// you may not use this file except in compliance with the License.\n// You may obtain a copy of the License at\n//\n//      http://www.apache.org/licenses/LICENSE-2.0\n//\n// Unless required by applicable law or agreed to in writing, software\n// distributed under the License is distributed on an "AS-IS" BASIS,\n// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n// See the License for the specific language governing permissions and\n// limitations under the License.\n\n/**\n * @fileoverview Directive for the rule editor.\n */\n\n// This directive controls an editor for selecting the type and input parameters\n// to a rule. It also includes \'Cancel\' and \'Save Answer\' buttons which call\n// respective \'onCancelRuleEdit\' and \'onSaveRule\' callbacks when called. These\n// buttons only show up if \'isEditingRuleInline\' is true.\noppia.directive(\'ruleEditor\', [\n  \'$log\', \'UrlInterpolationService\', function($log, UrlInterpolationService) {\n    return {\n      restrict: \'E\',\n      scope: {\n        isEditable: \'=\',\n        isEditingRuleInline: \'&\',\n        onCancelRuleEdit: \'&\',\n        onSaveRule: \'&\',\n        rule: \'=\'\n      },\n      templateUrl: UrlInterpolationService.getDirectiveTemplateUrl(\n        \'/components/\' +\n        \'rule_editor_directive.html\'),\n      controller: [\n        \'$scope\', \'$timeout\', \'StateEditorService\',\n        \'ValidatorsService\', \'INTERACTION_SPECS\',\n        \'ResponsesService\', \'StateInteractionIdService\',\n        function(\n            $scope, $timeout, StateEditorService,\n            ValidatorsService, INTERACTION_SPECS,\n            ResponsesService, StateInteractionIdService) {\n          var DEFAULT_OBJECT_VALUES = GLOBALS.DEFAULT_OBJECT_VALUES;\n\n          $scope.currentInteractionId = StateInteractionIdService.savedMemento;\n          $scope.editRuleForm = {};\n\n          // This returns the rule description string.\n          var computeRuleDescriptionFragments = function() {\n            if (!$scope.rule.type) {\n              $scope.ruleDescriptionFragments = [];\n              return \'\';\n            }\n\n            var ruleDescription = (\n              INTERACTION_SPECS[$scope.currentInteractionId].rule_descriptions[\n                $scope.rule.type]);\n\n            var PATTERN = /\\{\\{\\s*(\\w+)\\s*\\|\\s*(\\w+)\\s*\\}\\}/;\n            var finalInputArray = ruleDescription.split(PATTERN);\n            if (finalInputArray.length % 3 !== 1) {\n              $log.error(\'Could not process rule description.\');\n            }\n\n            var result = [];\n            for (var i = 0; i < finalInputArray.length; i += 3) {\n              result.push({\n                // Omit the leading noneditable string.\n                text: i !== 0 ? finalInputArray[i] : \'\',\n                type: \'noneditable\'\n              });\n              if (i === finalInputArray.length - 1) {\n                break;\n              }\n\n              var answerChoices = ResponsesService.getAnswerChoices();\n\n              if (answerChoices) {\n                // This rule is for a multiple-choice, image-click, or item\n                // selection interaction.\n                // TODO(sll): Remove the need for this special case.\n                if (answerChoices.length > 0) {\n                  if (finalInputArray[2] === \'SetOfHtmlString\') {\n                    $scope.ruleDescriptionChoices = answerChoices.map(\n                      function(choice) {\n                        return {\n                          id: choice.label,\n                          val: choice.label\n                        };\n                      }\n                    );\n                    result.push({\n                      type: \'checkboxes\',\n                      varName: finalInputArray[i + 1]\n                    });\n                  } else if (finalInputArray[2] === \'ListOfSetsOfHtmlStrings\') {\n                    $scope.ruleDescriptionChoices = answerChoices.map(\n                      function(choice) {\n                        return {\n                          id: choice.label,\n                          val: choice.label\n                        };\n                      }\n                    );\n                    result.push({\n                      type: \'dropdown\',\n                      varName: finalInputArray[i + 1]\n                    });\n                  } else if (\n                    finalInputArray[i + 2] === \'DragAndDropHtmlString\') {\n                    $scope.ruleDescriptionChoices = answerChoices.map(\n                      function(choice) {\n                        return {\n                          id: choice.label,\n                          val: choice.label\n                        };\n                      }\n                    );\n                    result.push({\n                      type: \'dragAndDropHtmlStringSelect\',\n                      varName: finalInputArray[i + 1]\n                    });\n                  } else if (\n                    finalInputArray[i + 2] === \'DragAndDropPositiveInt\') {\n                    $scope.ruleDescriptionChoices = answerChoices.map(\n                      function(choice) {\n                        return {\n                          id: choice.label,\n                          val: choice.label\n                        };\n                      }\n                    );\n                    result.push({\n                      type: \'dragAndDropPositiveIntSelect\',\n                      varName: finalInputArray[i + 1]\n                    });\n                  } else {\n                    $scope.ruleDescriptionChoices = answerChoices.map(\n                      function(choice) {\n                        return {\n                          id: choice.val,\n                          val: choice.label\n                        };\n                      }\n                    );\n                    result.push({\n                      type: \'select\',\n                      varName: finalInputArray[i + 1]\n                    });\n                    if (!$scope.rule.inputs[finalInputArray[i + 1]]) {\n                      $scope.rule.inputs[finalInputArray[i + 1]] = (\n                        $scope.ruleDescriptionChoices[0].id);\n                    }\n                  }\n                } else {\n                  $scope.ruleDescriptionChoices = [];\n                  result.push({\n                    text: \' [Error: No choices available] \',\n                    type: \'noneditable\'\n                  });\n                }\n              } else {\n                result.push({\n                  type: finalInputArray[i + 2],\n                  varName: finalInputArray[i + 1]\n                });\n              }\n            }\n\n            // The following is necessary in order to ensure that the\n            // object-editor HTML tags load correctly when the rule type is\n            // changed. This is an issue for, e.g., the MusicNotesInput\n            // interaction, where the rule inputs can sometimes be integers and\n            // sometimes be lists of music notes.\n            $scope.ruleDescriptionFragments = [];\n            $timeout(function() {\n              $scope.ruleDescriptionFragments = result;\n            }, 10);\n\n            return ruleDescription;\n          };\n\n          $scope.$on(\'updateAnswerGroupInteractionId\', function(\n              evt, newInteractionId) {\n            $scope.currentInteractionId = newInteractionId;\n          });\n\n          $scope.onSelectNewRuleType = function(newRuleType) {\n            var oldRuleInputs = angular.copy($scope.rule.inputs) || {};\n            var oldRuleInputTypes = angular.copy($scope.rule.inputTypes) || {};\n\n            $scope.rule.type = newRuleType;\n            $scope.rule.inputs = {};\n            $scope.rule.inputTypes = {};\n\n            var tmpRuleDescription = computeRuleDescriptionFragments();\n            // This provides the list of choices for the multiple-choice and\n            // image-click interactions.\n            var answerChoices = ResponsesService.getAnswerChoices();\n\n            // Finds the parameters and sets them in $scope.rule.inputs.\n            var PATTERN = /\\{\\{\\s*(\\w+)\\s*(\\|\\s*\\w+\\s*)?\\}\\}/;\n            while (true) {\n              if (!tmpRuleDescription.match(PATTERN)) {\n                break;\n              }\n              var varName = tmpRuleDescription.match(PATTERN)[1];\n              var varType = null;\n              if (tmpRuleDescription.match(PATTERN)[2]) {\n                varType = tmpRuleDescription.match(PATTERN)[2].substring(1);\n              }\n              $scope.rule.inputTypes[varName] = varType;\n\n              // TODO(sll): Find a more robust way of doing this. For example,\n              // we could associate a particular varName with answerChoices\n              // depending on the interaction. This varName would take its\n              // default value from answerChoices, but other variables would\n              // take their default values from the DEFAULT_OBJECT_VALUES dict.\n              if (angular.equals(DEFAULT_OBJECT_VALUES[varType], [])) {\n                $scope.rule.inputs[varName] = [];\n              } else if (answerChoices) {\n                $scope.rule.inputs[varName] = angular.copy(\n                  answerChoices[0].val);\n              } else {\n                $scope.rule.inputs[varName] = DEFAULT_OBJECT_VALUES[varType];\n              }\n\n              tmpRuleDescription = tmpRuleDescription.replace(PATTERN, \' \');\n            }\n\n            for (var key in $scope.rule.inputs) {\n              if (oldRuleInputs.hasOwnProperty(key) &&\n                oldRuleInputTypes[key] === $scope.rule.inputTypes[key]) {\n                $scope.rule.inputs[key] = oldRuleInputs[key];\n              }\n            }\n          };\n\n          $scope.cancelThisEdit = function() {\n            $scope.onCancelRuleEdit();\n          };\n\n          $scope.saveThisRule = function() {\n            $scope.onSaveRule();\n          };\n\n          $scope.init = function() {\n            // Select a default rule type, if one isn\'t already selected.\n            if ($scope.rule.type === null) {\n              $scope.onSelectNewRuleType($scope.rule.type);\n            }\n            computeRuleDescriptionFragments();\n          };\n\n          $scope.init();\n        }\n      ]\n    };\n  }]);'

blocks = {}
debug_info = ''