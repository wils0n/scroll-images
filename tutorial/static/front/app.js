app.controller('mainCtrl', ['$scope', 'UserFactory', 'constants', function ($scope, UserFactory, constants) {

    UserFactory.getAll().then(function(res){
        $scope.users = [];
        console.log(res);
        res.data.results.forEach(function(item){
          $scope.users.push(item);
        })
        return $scope;
    })
}]);

app.service('UserFactory', ['$http', 'constants', function ($http, constants) {
    return {
        getAll: function () {
            return $http.get(constants.userAPIurl);
        }
    }
}]);
