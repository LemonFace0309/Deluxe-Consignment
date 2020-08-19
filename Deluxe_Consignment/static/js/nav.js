const menuOpen = document.querySelector('#menu-open');
const menuClose = document.querySelector('#menu-close');
const sideNav = document.querySelector('.left-nav');
const searchBar = document.querySelector('#searchBar');

menuOpen.addEventListener('click', () =>  {
    console.log("asd");
    sideNav.classList.add('toggle');
    document.querySelector('#menu-open').style.color = 'green';
    document.body.style.overflow = "hidden";
});

menuClose.addEventListener('click', () => {
    sideNav.classList.remove('toggle');
    document.body.style.overflow = "auto";
});

searchBar.addEventListener('intput', () => {

});

window.addEventListener('scroll', function() {
    let nav = document.querySelector('nav');
    if (!window.location.href.includes('store')) {
        nav.classList.toggle('sticky', window.scrollY > window.innerHeight-150);
    } else {
        nav.classList.toggle('sticky', window.scrollY > 100);
    }
})

