$(document).ready(function() {
  //drop down menu
  $(".nav_drop-down").hover(function() {
    $('.nav_mega-menu').addClass('display-on');
  });
  $(".nav_drop-down").mouseleave(function() {
    $('.nav_mega-menu').removeClass('display-on');
  });

  $(".acc_drop-down").click(function() {
    $('.acc_mega-menu').addClass('display-on');
  });
  $(".acc_drop-down").mouseleave(function() {
    $('.acc_mega-menu').removeClass('display-on');
  });

});
