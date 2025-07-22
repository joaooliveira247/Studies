function process(callbackSuccess, callbackError) {
    // action

    let result = true;

    if (result) {
        callbackSuccess()
    } else {
        callbackError()
    }
}

const saveResult = function(){ 
    console.log("Save result");
};

const error = function(){
    console.log("Error");
};

process(saveResult, error);