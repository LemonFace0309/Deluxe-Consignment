let loader_path = './dev/dist/mdb-addons/preloader.html';
let windowLoaded = false;

$(window).on('load', function () {

  windowLoaded = true;
});

jQuery(function ($) { 
  $('body').attr('aria-busy', true);

  $('#preloader-markup').load(loader_path, function () {

    if (windowLoaded) {
    
      preloaderFading();
    } else {
    
      $(window).on('load', function () {  

       preloaderFading(); 
      });
    }
  });
});

function preloaderFading() {
  $('#mdb-preloader').fadeOut('slow');
  $('body').removeAttr('aria-busy');
};
