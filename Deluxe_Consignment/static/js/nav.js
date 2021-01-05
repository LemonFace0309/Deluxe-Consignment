const nav = document.querySelector('nav');
const menuOpen = document.querySelector('#menu-open');
const menuClose = document.querySelector('#menu-close');
const sideNav = document.querySelector('.left-nav');


// Responsive: Open Side Menu
menuOpen.addEventListener('click', () =>  {
    sideNav.classList.add('showSide');
    document.body.style.overflow = "hidden";
});

// Responsive: Close Side Menu
menuClose.addEventListener('click', () => {
    sideNav.classList.remove('showSide');
    sideNav.classList.add('hideSide');
    setTimeout(() => sideNav.classList.remove('hideSide'), 400);
    document.body.style.overflow = "auto";
});


// Search for item
document.querySelector('#search').addEventListener('submit', () => {
    let search = document.querySelector('#searchBar').value;
    sessionStorage.setItem('search', search);
});

// Load search term after refresh
window.addEventListener('load', () => {
    $('#searchBar').val(sessionStorage.getItem('search'));
})


// Collapse Navbar when scrolling
// See nav.css for sticky class
window.addEventListener('scroll', function() {
    const url = location.pathname;
    if (url != '/') {
        nav.classList.toggle('sticky', window.scrollY > 80);
    } else {
        nav.classList.toggle('sticky', window.scrollY > window.innerHeight+100);
    }
});
