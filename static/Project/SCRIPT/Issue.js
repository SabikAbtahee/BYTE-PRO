/**
 * Created by sabik on 5/25/2018.
 */
function validate() {
    valid=false;



    var text2 = $('#projDesc').val();


    helpDescription=document.getElementById("helpBlock1");




    if(text2.length==0){
        helpDescription.textContent="Please enter some description.";
        valid=false;
    }
    if(text2.length>0){
        helpDescription.textContent="";
        valid=true;
    }




    return valid;
}