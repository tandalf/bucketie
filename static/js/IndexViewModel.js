var IndexViewModel = function (){
    var self = this;
    var loginURL = apiURL + "auth/login";

    self.initUserName = ko.observable();

    self.authVM = new AuthViewModel(loginURL, self);
}