// Render the PayPal button into #paypal-button-container
paypal.Buttons({

    style: {
        layout: 'horizontal'
    },

    // Set up the transaction
    createOrder: function(data, actions) {
        return actions.order.create({
            purchase_units: [{
                amount: {
                    value: parseFloat(total).toFixed(2)
                }
            }]
        });
    },

    // Finalize the transaction
    onApprove: function(data, actions) {
        return actions.order.capture().then(function(details) {
            submitFormData()
        });
    }


}).render('#paypal-button-container');


var form = document.getElementById('checkout_form')
csrftoken = form.getElementsByTagName("input")[0].value


form.addEventListener('submit', function(e){
    e.preventDefault()
    document.getElementById('continue-button').classList.add('hidden')
    document.getElementById('paypal-payment').classList.remove('hidden')
})


function submitFormData(){
    console.log('Payment button clicked')

    var userFormData = {
        'name': null,
        'email': null,
        'total': total
    }

    if(user == 'AnonymousUser'){
        userFormData.name = form.first_name.value + ' ' + form.last_name.value,
        userFormData.email = form.email.value
    }

    var shippingInfo = {
        'address': form.address.value,
        'address2': form.address2.value,
        'city': form.city.value,
        'province': form.province.value,
        'country': form.country.value,
        'postal_code': form.postal_code.value,
    }

    var url = '/user/process-order/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'form': userFormData,
            'shipping': shippingInfo,
        })
    })
    .then((res) => res.json())
    .then((data) => {
        console.log('Success:', data)
        alert('Transaction completed')

        cart = {}
        document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"

        window.location.href = "/"
        })
}
