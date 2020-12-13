const nav = document.querySelector('nav');
const menuOpen = document.querySelector('#menu-open');
const menuClose = document.querySelector('#menu-close');
const sideNav = document.querySelector('.left-nav');


menuOpen.addEventListener('click', () =>  {
    sideNav.classList.add('showSide');
    document.body.style.overflow = "hidden";
});

menuClose.addEventListener('click', () => {
    sideNav.classList.remove('showSide');
    sideNav.classList.add('hideSide');
    setTimeout(() => sideNav.classList.remove('hideSide'), 400);
    document.body.style.overflow = "auto";
});

document.querySelector('#search').addEventListener('submit', () => {
    let search = document.querySelector('#searchBar').value;
    sessionStorage.setItem('search', search);
});

window.addEventListener('load', () => {
    $('#searchBar').val(sessionStorage.getItem('search'));
})

// See nav.css for sticky class
window.addEventListener('scroll', function() {
    const url = location.pathname;
    if (url != '/') {
        nav.classList.toggle('sticky', window.scrollY > 80);
    } else {
        nav.classList.toggle('sticky', window.scrollY > window.innerHeight+100);
    }
});
