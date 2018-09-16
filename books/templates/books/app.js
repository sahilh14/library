(function () {
'use strict';


function CustomFilterFactory() {
  return function (input) {
    return input * 2

  };
};
var mod = angular.module('myFirstApp', [])
mod.controller('MyFirstController', MyFirstController)    // registering a controller on the module
// angular.module('myFirstApp', [])
//
// .controller('MyFirstController', MyFirstController);

mod.filter('custom', CustomFilterFactory)
MyFirstController.$inject = ['$scope', '$filter', '$injector', 'customFilter', '$http']  /*all these are services */
function MyFirstController($scope, $filter, $injector, customFilter, $http) {
  $scope.name = 'sahil'
  $scope.var = 'sahil'
  $scope.output = $filter('uppercase')($scope.var)    /*$filter is a filter factory return a function*/
  console.log($injector.annotate(MyFirstController))

  // var s = CustomFilterFactory()
  console.log(customFilter(3))

  $scope.display = function () {
    console.log($scope.name)
  }

  var a = $http.get('http://127.0.0.1:8000/books/display/1');
}

})();
