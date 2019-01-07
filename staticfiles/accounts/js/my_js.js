(function($) {
	"use strict"

  // Random Image From Folder
  var path = '/static/accounts/img/',
      imgs = ['bg-01.jpg','bg-02.jpg','bg-03.jpg','bg-04.jpg','bg-05.jpg','bg-06.jpg','bg-07.jpg','bg-08.jpg'],
      i = Math.floor(Math.random()*imgs.length),
      el = document.getElementById('rand-background');
  el.style.cssText = 'background-image: url('+path+imgs[i]+');';
})(jQuery);

// // Example:
// document.getElementById('rand-background').classList.add('login100-more');


// // Examples
// var nFilter = document.createElement('div');
// nFilter.className = 'well';
// nFilter.innerHTML = '<label>'+sSearchStr+'</label>';
//
// // Css styling
// nFilter.style.width = "330px";
// nFilter.style.float = "left";
//
// // or
// nFilter.setAttribute("style", "width:330px;float:left;");
