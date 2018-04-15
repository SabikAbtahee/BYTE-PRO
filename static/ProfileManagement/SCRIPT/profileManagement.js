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

function showCheckboxes() {
  var checkboxes = document.getElementById("checkboxes");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}