var IndexViewModel = function (){
    var self = this;
    var loginURL = apiURL + "auth/login";
    var createBucketListURL = apiURL + 'bucketlist/'

    self.initUserName = ko.observable();

    self.authVM = new AuthViewModel(loginURL, self);
    self.bucketListVM = new BucketListViewModel(createBucketListURL);
}