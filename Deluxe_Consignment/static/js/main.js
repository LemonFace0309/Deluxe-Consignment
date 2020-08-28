var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(e){
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

    var url = "http://127.0.0.1:8000/update-cookie-cart-quantity/"
    if(cart[productId] == undefined){
        itemQuantity = 0
    } else {
        itemQuantity = cart[productId]['quantity']
    }

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
                // Overriding cart cookie
                cart[productId]['quantity'] += 1
                console.log('Cart:', cart)
                document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
            }
        }
        if(result == 'remove'){
            delete cart[productId]
            // Overriding cart cookie
            console.log('Cart:', cart)
            document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
        }
    })

    // Change to use rest API later
    setTimeout(() => {location.reload(true)}, 25)
}


//$(document).ready(
function removeCover(){
    //setTimeout(() => {
    var aTags = document.getElementsByTagName('a')
    for (i = 0; i < aTags.length; i++){
        if (aTags[i].innerText.includes('Free Instagram Feed widget')){
            console.log();
            aTags[i].remove();
            break;
        }
    }
    //}, 500);

}
//)

