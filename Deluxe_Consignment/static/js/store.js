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

const onChangeElements = document.querySelectorAll('.submitonchange');
onChangeElements.forEach(item => {
    item.addEventListener('click', () => {
        item.closest('form').submit();
        item.selected = true;
    })
})