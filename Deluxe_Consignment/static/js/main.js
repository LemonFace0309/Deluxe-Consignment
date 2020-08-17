$(document).ready(() => {
    new WOW().init();
});

document.addEventListener('DOMContentLoaded', function() {
    let elems = document.querySelectorAll('.carousel');
    let items = document.querySelectorAll('.carousel-item');
    // items.forEach();
    let instances = M.Carousel.init(elems, {
        numVisible: 3,
        dist: -50,
    });
});
