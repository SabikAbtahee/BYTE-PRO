function validate() {
    valid=false;

    var text2 = $('#COMMENT-DESCRIPTION').val();

    if(text2.length===0){
        valid=false;
    }
    if(text2.length>0){
        valid=true;
    }
    return valid;
}