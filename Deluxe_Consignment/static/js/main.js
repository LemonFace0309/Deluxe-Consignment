$(document).ready(() => {
    new WOW().init();
    $('#modalCookie1').modal('show')
});

function removeCover(){
<<<<<<< HEAD
    console.log('hi')
    setTimeout(() => {
        var aTags = document.getElementsByTagName('a')
            console.log(aTags.length);
        for (i = 0; i < aTags.length; i++){
            console.log(aTags[i].href);
            if (aTags[i].innerText.includes('Free Instagram Feed widget')){
                console.log();
                aTags[i].remove();
                break;
            }
        }
    }, 1000);
=======
    //setTimeout(() => {
    let aTags = document.getElementsByTagName('a')
        // console.log(aTags.length);
    for (i = 0; i < aTags.length; i++){
        // console.log(aTags[i].href);
        if (aTags[i].innerText.includes('Free Instagram Feed widget')){
            // console.log();
            aTags[i].remove();
            break;
        }
    }
    //}, 500);
>>>>>>> home
}

<<<<<<< HEAD
window.onload = removeCover()
=======
const onChangeElements = document.querySelectorAll('.submitonchange');
onChangeElements.forEach(item => {
    item.addEventListener('click', () => {
        item.closest('form').submit();
    })
})

>>>>>>> home
