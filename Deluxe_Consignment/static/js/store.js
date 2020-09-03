const pages = document.querySelectorAll('.paginate a');
let search = location.search

if (search.indexOf('&') != -1) {
    search = search.substring(0, search.indexOf('&'))
}

pages.forEach(page => {
    if (search != '' && search.substring(0, 5) != '?page') {
        let pageLink = page.getAttribute('href').substring(1)
        page.href = `${search}&${pageLink}`
    }
})
// end pagination

// let catSel = sessionStorage.getItem('catSel')
let catSel =''



const onChangeElements = document.querySelectorAll('.submitonchange');
onChangeElements.forEach(item => {
    item.addEventListener('click', () => {
        sessionStorage.setItem('catSel', item.id)
        // console.log(sessionStorage.getItem('catSel'))
        item.closest('form').submit();
    })
})

window.addEventListener('load', () => {
    setTimeout(() => {
        console.log(localStorage.getItem('catSel'))
        console.log(`#${catSel}`)
        document.querySelector(`#${sessionStorage.getItem('catSel')}`).checked = true;
    }, 0);
}) 


function test() {
    console.log('he')
    const b = document.querySelector('#radio101')
    b.checked = true;
    console.log(b.value)
}