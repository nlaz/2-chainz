$(document).ready(function() {
  $("#quote").hide();
  initClicks();
});

selectPos = 1;

function initClicks() {
  $(".image-button").click(function() {
    if (selectPos === 1) {
      $(".selected1").toggleClass("selected1");
      $(this).addClass("selected1");
      selectPos = 2;
    } else if (selectPos === 2) {
      $(".selected2").toggleClass("selected2");
      $(this).addClass("selected2");
      selectPos = 1;
    }
  });

  $("#generate-button").click(function() {
    var selected1 = $(".selected1").attr("id");
    var selected2 = $(".selected2").attr("id");
    $.get(
      $SCRIPT_ROOT + "/swagger",
      {
        p1: selected1,
        p2: selected2
      },
      function(data) {
        $("#prompt").hide();
        $("#quote").show();
        $("#quote").html(data);
      }
    );
    return false;
  });
}
