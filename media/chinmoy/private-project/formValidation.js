function isNameFilled() {
    var x = document.forms["myForm"]["fname"].value;
    document.write(x)
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
} 

function myFunction() {
    var inpObj = document.getElementById("id1");
    if (!inpObj.checkValidity()) {
        document.getElementById("demo").innerHTML = inpObj.validationMessage;
    } else {
        document.getElementById("demo").innerHTML = "Input OK";
    } 
} 