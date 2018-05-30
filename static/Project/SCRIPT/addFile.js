
function validate() {
    valid=false;

    file=document.getElementById("file");
    projectDescription=document.getElementById("projDesc");

    var text2 = $('#projDesc').val();
    var files = $('#file')[0].files;
    var fileCount=files.length;
    helpDescription=document.getElementById("helpBlock2");
    helpFile=document.getElementById("helpBlock1");



    if(text2.length==0){
        helpDescription.textContent="Please enter some description.";
    }
    if(text2.length>0){
        helpDescription.textContent="";
    }
    if(fileCount==0){
        helpFile.textContent="You need to select atleast one file";
    }
    if(fileCount>0){
        helpFile.textContent="";
    }
    if(text2.length>0 && fileCount>0){
        helpDescription.textContent="";
        helpFile.textContent="";
        valid=true;
    }



    return valid;
}
