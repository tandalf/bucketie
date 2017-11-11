var AuthViewModel = function(loginURL, indexVM){
    var self = this;
    var authUser = utils.storageUserDetails();

    self.loginData = {
        username: ko.observable(""),
        password: ko.observable("")
    };
    self.loginModalID = "#login-modal";
    self.loginModal = utils.ModalHelper(self.loginModalID);

    
    self.showLogin = function(){
        $("#login-modal").modal();
        self.loginData.username(indexVM.initUserName());
        self.loginModal.clearAlert();
    };

    self.loginUser = function(form){
        if(authUser){
            alert("You should log out first");
            return null;
        }

        self.loginModal.startLoadingAnimation();
        var body = ko.toJSON(self.loginData);
        $.ajax({
            url: loginURL,
            type: "POST",
            data: body,
            contentType: 'application/json'
        }).done(self.loginSuccess).fail(self.loginFailure);
    }

    self.loginSuccess = function(resp){
        self.loginModal.alertSuccess("Signing in a moment!");
        self.loginModal.stopLoadingAnimation();
        utils.storeUserDetails({
            token: resp.token,
            name: self.loginData.username()
        });
        window.location.href = siteURL + "signedin";
    }

    self.loginFailure = function(resp){
        var body = resp.responseJSON;
        self.loginModal.alertError(body.non_field_errors[0]);
        self.loginModal.stopLoadingAnimation();
    }

    self.logoutUser = function(){
        utils.deleteStorageUser();
        console.log(siteURL);
        window.location.href = siteURL;
    }

    self.isLoggedIn = function(){
        var userDetails = utils.storageUserDetails();
        if(userDetails && userDetails.token) return true
        return false;
    }

    self.isPasswordValid = function(form){
        if(form.password === form.passwordConfirm) return true;
        return false;
    }
}