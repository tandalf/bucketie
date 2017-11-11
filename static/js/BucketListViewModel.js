var BucketListViewModel = function(createBucketListURL){
    var self = this;

    self.bucketListItems = ko.observableArray();

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
        window.location.href = siteURL + "bucketlist";
    }

    self.createBucketListFailure = function(resp){
        var body = resp.responseJSON;
        self.createBucketListModal.alertError(body.detail);
        self.createBucketListModal.stopLoadingAnimation();
    }

    self.listBucketList = function(){
        $.ajax({
            url: createBucketListURL,
            type: 'GET',
            contentType: 'application/json',
            headers: {Authorization: utils.authHeader()}
        }).done(self.listBucketListSuccess).fail(self.listBucketListFailure);
    }

    self.listBucketListSuccess = function(resp){
        console.log(resp);
        self.bucketListItems = self.bucketListItems(resp);
    }

    self.listBucketListFailure = function(resp){
        self.listBucketList();
    }

    self.splitDate = function(date){
        return date.split('T')[0];
    }

    self.name = function(){return 'sss'}
}