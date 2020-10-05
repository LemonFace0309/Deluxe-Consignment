const pages = document.querySelectorAll('.paginate a');
let search = location.search

if (search.indexOf('&page=') != -1) {
    search = search.substring(0, search.lastIndexOf('&'))
}

pages.forEach(page => {
    if (search != '' && search.substring(0, 5) != '?page') {
        let pageLink = page.getAttribute('href').substring(1)
        page.href = `${search}&${pageLink}`
    }
})

$(".paginate a").click(function() {
    saveFilter();
});
// end pagination


$("#filterToggle").click(function() {
    console.log("wokring")
    $(".filter").toggleClass("show")
});







// Filtering
$(".category").change(function() {
    $(".category").not(this).prop('checked', false);
});

function saveFilter() {
    let sortOption = document.querySelector('#sort').value
    let brandOption = document.querySelector('#brand').value
    let categoryOption = document.querySelector('.category:checked')
    let priceOption = document.querySelector('#priceSlider').value

    if (categoryOption != null) {
        categoryOption = categoryOption.id
    }
    
    sessionStorage.setItem('sort', sortOption)
    sessionStorage.setItem('brand', brandOption)
    sessionStorage.setItem('category', categoryOption)
    sessionStorage.setItem('price', priceOption)
};

$(".submit").click(function() {
    saveFilter();
});




window.addEventListener('load', () => {
    setTimeout(() => {
        $('#sort').val(sessionStorage.getItem('sort'));
        $('#brand').val(sessionStorage.getItem('brand'));
        $('#priceSlider').val(sessionStorage.getItem('price'));

        if (sessionStorage.getItem('category') != 'null') {
            document.querySelector(`#${sessionStorage.getItem('category')}`).checked = true;
        }

        if (sessionStorage.getItem('price') == 'null') {
            document.querySelector('#priceSlider').value = 10000;
        }

        sessionStorage.setItem('sort', 'null')
        sessionStorage.setItem('brand', 'null')
        sessionStorage.setItem('category', 'null')
        sessionStorage.setItem('price', 'null')
    }, 0);
}) 








// $(document).on('submit', '#sortForm', function(e){
//     e.preventDefault();
//     console.log("console subm")
//     console.log($('#sort').val())
//     // console.log(token)

//     $.ajax({
//         type: 'GET',
//         url: '/store/',
//         data: {
//             sort:$('#sort').val(),
//             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
//         },
//         // datatype: 'json',
//         success: function () {
//             console.log('sucess')
//             location.reload()
//         }
//     })
// });

