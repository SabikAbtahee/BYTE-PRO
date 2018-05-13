// $(function(){
//     $( '.dropdown-menu li' ).on( 'click', function( event ) {
//         var $checkbox = $(this).find('.checkbox');
//         if (!$checkbox.length) {
//             return;
//         }
//         var $input = $checkbox.find('input');
//         var $icon = $checkbox.find('span.glyphicon');
//         if ($input.is(':checked')) {
//             $input.prop('checked',false);
//             $icon.removeClass('glyphicon-check').addClass('glyphicon-unchecked')
//         } else {
//             $input.prop('checked',true);
//             $icon.removeClass('glyphicon-unchecked').addClass('glyphicon-check')
//         }
//         return false;
//     });
// });


var expanded = false;
var expanded2 = false;
function showCheckboxes() {


    if (!expanded2) {
        checkboxes.style.display = "block";
        checkboxes.style.size=10;
        expanded2 = true;
    }
    else if(expanded2){
        checkboxes.style.display = "none";

        expanded2 = false;
    }

}

function showcheckboxes2() {

    if (!expanded) {
        checkboxes2.style.display = "block";
        checkboxes2.style.size=10;
        expanded = true;
    }
    else if(expanded){
        checkboxes2.style.display = "none";
        expanded = false;
    }
}


