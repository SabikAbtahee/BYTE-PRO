/**
 * Created by sabik on 5/24/2018.
 */



function validate() {
    valid=false;
    validspace=true;
    projectText=document.getElementById("projectName");
    projectDescription=document.getElementById("projDesc");
    var text1 = $('#projectName').val();
    var text2 = $('#projDesc').val();


    CorrectName=document.getElementById("correctProjectName");
    WrongName=document.getElementById("wrongProjectName");
    helpDescription=document.getElementById("helpBlock2");
    helpName=document.getElementById("helpBlock1");



    if(text2.length==0){
        helpDescription.textContent="Please enter some description.";
    }
    if(text2.length>0){
        helpDescription.textContent="";
    }
    if(text1.length==0){
        WrongName.className="unhidden";
        CorrectName.className="hidden";
        helpName.textContent="No name given";
    }

    if (/\s/.test(text1)) {
        // It has any kind of whitespace
        WrongName.className = "unhidden";
        CorrectName.className = "hidden";
        helpName.textContent = "No space allowed";
        validspace=false;
    }
    else if(text1.length>0){
        WrongName.className = "hidden";
        CorrectName.className = "unhidden";
        helpName.textContent = "";
        validspace=true;
    }

    if(text2.length!=0 && text1.length>0 && validspace==true){
        valid=true;
    }





    return valid;
}


// CorrectName.className="unhidden";

// if(age=="Sabik"){
//     Correct.style.display="inline";
//     Wrong.style.display="none";
// }
// else{
//     Correct.style.display="none";
//     Wrong.style.display="inline";
// }


// var age = $('#projectName').val();


// Correct.style.display="none";
// Wrong.style.display="inline";