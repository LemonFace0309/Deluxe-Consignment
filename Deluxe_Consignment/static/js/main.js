$(document).ready(() => {
    new WOW().init();
    $('#modalCookie1').modal('show')
});

var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        if(user == 'AnonymousUser'){
            var productId = this.dataset.product
            var action = this.dataset.action
            
            console.log('productId:', productId, 'action:', action)
            addCookieItem(productId, action)
        }
    })
}

function addCookieItem(productId, action){
    console.log('Not logged in...')

    /*
    cart = {
        1:{'quantity':4},
        5:{'quantity':6},
        2:{'quantity':1},
        8:{'quantity':3},
    }
    */

    if(action == 'add'){
        if(cart[productId] == undefined) {
            cart[productId] = {'quantity': 1}
        }else{
            cart[productId]['quantity'] += 1
        }
    }

    if(action =='remove'){
        delete cart[productId]
    }

    // Overriding cart cookie
    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    // Change to use rest API later
    location.reload() 
}