var BucketListViewModel = function(createBucketListURL){
    var self = this;

    self.createBucketListData = {
        name: ko.observable(),
        description: ko.observable()
    };
    self.createBucketListModalID = "#create-bucketlist-modal";
    self.createBucketListModal = utils.ModalHelper(self.createBucketListModalID);

    self.showCreateBucketList = function(){
        $(self.createBucketListModalID).modal();
        self.createBucketListModal.clearAlert();
    }

    self.createBucketList = function(form){
        self.createBucketListModal.startLoadingAnimation();
        var body = ko.toJSON(self.createBucketListData);
        $.ajax({
            url: createBucketListURL,
            type: "POST",
            data: body,
            contentType: 'application/json',
            headers: {Authorization: utils.authHeader()}
        }).done(self.createBucketListSuccess).fail(self.createBucketListFailure);
    }

    self.createBucketListSuccess = function(resp){
        self.createBucketListModal.alertSuccess("BucketList Created!");
        self.createBucketListModal.stopLoadingAnimation();
        window.location.href = siteURL + "signedin";
    }

    self.createBucketListFailure = function(resp){
        var body = resp.responseJSON;
        self.createBucketListModal.alertError(body.detail);
        self.createBucketListModal.stopLoadingAnimation();
    }
}