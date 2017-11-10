var ModalHelper = function(id){
    var self = this;
    var alert = $(id).find(".alert");
    var loading = $(id).find("#anim-ball");

    alert.hide();
    loading.hide();

    self.alert = function(message){
        console.log(message);
        if(message) ;
        else return;
        alert.removeClass("alert-danger");
        alert.removeClass("alert-success");
        alert.hide();
        alert.fadeIn();
        alert.text(message);
    }

    self.alertError = function(message){
        if(!message)message = "Error!"
        alert.removeClass("alert-success");
        alert.addClass("alert-danger");
        alert.hide();
        alert.fadeIn();
        alert.text(message);
    }

    self.alertSuccess = function(message){
        if(!message)message = "Success!"
        alert.removeClass("alert-danger");
        alert.addClass("alert-success");
        alert.hide();
        alert.fadeIn();
        alert.text(message);
    }

    self.clearAlert = function(){
        alert.hide();
    }

    self.startLoadingAnimation = function(){
        loading.fadeOut();
        loading.fadeIn();
    }

    self.stopLoadingAnimation = function(){
        loading.fadeIn();
        loading.fadeOut();
    }

    self.close = function(){
        self.clearAlert();
        self.stopLoadingAnimation();
        $(id).modal('hide');
    }
}

var storeUserDetails = function(user){
    if(typeof(Storage) !== undefined){
        localStorage.setItem("token", user.token);
        localStorage.setItem("username", user.name);
        return user.token;
    }
    alert("This browser is not supported. Cannot save session.");
}

var storageUserDetails = function(){
    if(typeof(Storage) !== undefined){
        var details = {
            token: localStorage.getItem("token"),
            name: localStorage.getItem("username")
        };
        if(details.token == null) return null;
        return details;
    }
    alert("Browser not supported for storing user details.");
}

var deleteStorageUser = function(){
    localStorage.removeItem("token");
    localStorage.removeItem("username");
}

utils = {
    ModalHelper: function(id){
        return new ModalHelper(id)
    },
    storeUserDetails: storeUserDetails,
    storageUserDetails: storageUserDetails,
    deleteStorageUser: deleteStorageUser,
}