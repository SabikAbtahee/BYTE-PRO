
nameExists=true;
$("#projectName").change(function () {
    var text = $(this).val();
    $.ajax({
        type:"POST",
        url: "/ajax/projectExists/",

        data: {
            'newName': text
        },
        dataType: 'json',
        success: function (data) {
            if (data.check) {
                nameExists=true;
            }

        }
    });

});


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

function validName() {
    CorrectName=document.getElementById("correctProjectName");
    WrongName=document.getElementById("wrongProjectName");
    helpName=document.getElementById("helpBlock1");
    WrongName.className = "unhidden";
    CorrectName.className = "hidden";
    helpName.textContent = "Same name exists try different one";
    document.getElementById("addProjectButton").disabled = true;
}

function validName2(){
    CorrectName=document.getElementById("correctProjectName");
    WrongName=document.getElementById("wrongProjectName");

    WrongName.className = "hidden";
    CorrectName.className = "hidden";
    helpName.textContent = "";
    document.getElementById("addProjectButton").disabled = false;
}
le.display="inline";