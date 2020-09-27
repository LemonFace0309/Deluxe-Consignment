var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(e){
        if(user == 'AnonymousUser'){
            var productId = this.dataset.product
            var action = this.dataset.action
            
            // console.log('productId:', productId, 'action:', action)
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

    if(cart[productId] == undefined){
        itemQuantity = 0
    } else {
        itemQuantity = cart[productId]['quantity']
    }

    var url = "/update-cookie-cart-quantity/"
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productId': productId,
            'itemQuantity': itemQuantity,
            'action': action,
        })
    })
    .then((response) => {
        return response.json()
    })
    .then((result) => {
        console.log('Result:', result)
        if(result == 'add'){
            if(cart[productId] == undefined) {
                cart[productId] = {'quantity': 1}
                // Overriding cart cookie
                console.log('Cart:', cart)
                document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
            }else{
                cart[productId]['quantity'] += 1
                console.log('Cart:', cart)
                document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
            }
        }
        else if(result == 'subtract'){
            if(cart[productId]['quantity'] > 1){
                cart[productId]['quantity'] -= 1
                console.log('Cart:', cart)
                document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
            } else {
                delete cart[productId]
                console.log('Cart:', cart)
                document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
            }
        }
        else if(result == 'remove'){
            delete cart[productId]
            console.log('Cart:', cart)
            document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
        }
    })

    // Change to use rest API later
    setTimeout(() => {location.reload(true)}, 25)
}


function removeCover(){
    setTimeout(() => {
        let aTags = document.getElementsByTagName('a')
        for (i = 0; i < aTags.length; i++){
            // console.log(aTags[i].href);
            if (aTags[i].innerText.includes('Free Instagram Feed widget')){
                aTags[i].remove();
            }

            if (aTags[i].innerText.includes('Widget is deactivated')){
                aTags[i].remove();
            }
        }
    }, 1000);
}

window.onload = function () {
    removeCover();
    setTimeout(() => {
        removeCover();
    }, 10000);
};