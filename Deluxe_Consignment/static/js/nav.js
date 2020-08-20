const nav = document.querySelector('nav');
const menuOpen = document.querySelector('#menu-open');
const menuClose = document.querySelector('#menu-close');
const sideNav = document.querySelector('.left-nav');
const searchBar = document.querySelector('#searchBar');

menuOpen.addEventListener('click', () =>  {
    console.log("asd");
    sideNav.classList.add('showSide');
    // document.querySelector('#menu-open').style.color = 'green';
    document.body.style.overflow = "hidden";
});

menuClose.addEventListener('click', () => {
    sideNav.classList.remove('showSide');
    sideNav.classList.add('hideSide');
    setTimeout(() => sideNav.classList.remove('hideSide'), 400);
    document.body.style.overflow = "auto";
});

searchBar.addEventListener('intput', () => {

});

window.addEventListener('scroll', function() {
    // console.log({{request.path}});
    if (!window.location.href.includes('store')) {
        nav.classList.toggle('sticky', window.scrollY > window.innerHeight-150);
    } else {
        nav.classList.toggle('sticky', window.scrollY > 100);
    }
    resizeNav();
});


const navBack = document.querySelector('.nav-back');
function resizeNav() {
    navBack.style.height = `${nav.clientHeight}px`;
} 
window.addEventListener('resize', resizeNav);


document.addEventListener("DOMContentLoaded", function(){
    resizeNav();
});