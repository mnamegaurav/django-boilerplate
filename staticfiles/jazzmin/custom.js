$(document).ready(function () {
  all_num_inputs = $("input[type=number]");

  // Add class vTextField to all_num_inputs
  all_num_inputs.addClass("vTextField");

  // Add sticky-top class to navbar
  $("#jazzy-navbar").addClass("sticky-top");

  $(".card .p-5").addClass("p-2 p-md-5").removeClass("p-5");

  // Remove default shadow of some bootstrap elements
  $(".btn").addClass("shadow-none");
  $(".form-control").addClass("shadow-none");
  $(".form-group .col-sm-7").addClass("col-sm-9").removeClass("col-sm-7");
  $("select").addClass("shadow-none custom-select");
  $("input.vTextField").addClass("form-control shadow-none");
  $("input.vTimeField").addClass("form-control shadow-none");
  $("input.vDateField").addClass("form-control shadow-none");
  $("textarea.vLargeTextField").addClass("form-control shadow-none");
  $(".field-extra_data .readonly").html(
    `<pre><code>${JSON.stringify(
      JSON.parse($(".field-extra_data .readonly").text()),
      null,
      4
    )}</code></pre>`
  );
});

$(document).ready(function () {
  // This is code will perform some styling on non expanded style of Jazzmin Sidebar Menus
  // Collect all the Nav Headers inside the #jazzy-sidebar
  var nav_headers = $("#jazzy-sidebar .nav-header");

  // Add border-top to all the Nav Headers
  nav_headers.addClass("border-top my-2");

  // add bold text to all the Nav Headers
  nav_headers.addClass("font-weight-bold");

  // Loop through all the nav headers
  nav_headers.each(function (index) {
    // Collect all the Nav Items as next siblings of the current Nav Header
    var nav_items = $(this).nextUntil(".nav-header");
    // console.log(index, nav_items);
  });
});
