// Copyright 2018 The Oppia Authors. All Rights Reserved.
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
 * @fileoverview Directive to load content on the base page.
 */

 oppia.directive('blockContentLoader', [ '$http', '$compile', 'UrlInterpolationService',
 	function($http, $compile, UrlInterpolationService) {
 	
 		// trial to load a controller and compile it after the page is 
 		// already compiled.
 		// $http.get('/templates/dev/head/pages/about/About.js').then(
 		// 	function(response) {
 		// 		console.log('hello');
 		// 		console.log(response);
 		// 		angular.element(document).injector().invoke(['$compile', function($compile) {
 		// 			console.log('bello');
 		// 			// create a scope
 		// 			var $scope = angular.element(document.body).scope();
 		// 			// compile the script
 		// 			var $compiled = $compile(response.data)($scope);
 		// 			// signal the scope to digest the data
 		// 			$scope.digest();
 		// 			// append compiled output to the page
 		// 			$compiled.appendTo(document.body);
 		// 		}]);
 		// 	});

	    if( window.location.pathname === '/about') {
	          contentDirectivePath = UrlInterpolationService.getDirectiveTemplateUrl(
	            '/pages/about/about_content.html');
	    } else {
	        contentDirectivePath = (UrlInterpolationService.getDirectiveTemplateUrl(
	          '/pages/empty_page.html'));    
	    }
	      
	    if( window.location.pathname === '/about') {
	        contentControllerName = 'About';
	    } else {
	        contentControllerName = '';
	    }
 		return {
 			restrict: 'E',
 			// somehow not working with isolated scope, need to handle
 			scope: true,
 			templateUrl: contentDirectivePath,
 			controller: contentControllerName
 		};
 	}

]);
