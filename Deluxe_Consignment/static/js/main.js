$(document).ready(() => {
    new WOW().init();
    $('#modalCookie1').modal('show')
});

//$(document).ready(
function removeCover(){
    //setTimeout(() => {
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
    //}, 500);

}
//)

