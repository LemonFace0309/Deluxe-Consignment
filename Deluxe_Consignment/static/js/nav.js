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

const nav = document.querySelector('nav');
const navHeader = document.querySelector('.nav-header');
const navMenu = document.querySelector('.menu');
window.addEventListener('scroll', function() {
    if (window.scrollY > window.innerHeight) {
        nav.classList.add('sticky');
        // setTimeout(() => navMenu.style.display = 'none', 200);
        // navMenu.style.display = 'none';
    } else {
        nav.classList.remove('sticky');
        // navMenu.style.display = 'flex'; 
        // setTimeout(() => navMenu.style.display = 'flex', 10);
    }
})

