// Updates delivery information
var delivery_forms = document.getElementsByClassName('delivery-form')
csrftoken = delivery_forms[0].getElementsByTagName("input")[0].value

for(let i = 0; i < delivery_forms.length; i++){
    delivery_forms[i].addEventListener('submit', function(e){
        e.preventDefault()


        // is_layaway returns true or false
        try{
            is_layaway = this.layaway.checked
            delivery = 'Shipping'
        } catch (error){
        }
        try {
            is_layaway = this.layaway2.checked
            delivery = 'Pick-up'
        } catch (error){
        }

        var userFormData = {
            'name': null,
            'email': null,
            'total': total
        }

        if(user == 'AnonymousUser'){
            userFormData.name = this.first_name.value + ' ' + this.last_name.value,
            userFormData.email = this.email.value
        }

        var shippingInfo = {
            'address': this.address.value,
            'address2': this.address2.value,
            'city': this.city.value,
            'province': this.province.value,
            'country': this.country.value,
            'postal_code': this.postal_code.value,
        }

        let url = '/user/update-delivery/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'delivery': delivery,
                'is_layaway': is_layaway,
                'form': userFormData,
                'shipping': shippingInfo,
            })
        })
        .then((res) => res.json())
        .then((data) => {
            // updating html
            console.log(data)

            if (data.delivery == 'Shipping'){
                // updating shipping cost
                shipping_cost = document.getElementById('shipping-cost')
                shipping_cost.textContent = '$' + data.shipping_cost.toFixed(2)
                // updating total cost
                total_cost = document.getElementById('total-cost')
                total_cost.textContent = '$' + data.get_cart_total.toFixed(2)
            } else if (data.delivery == 'Pick-up') {
                total_cost = document.getElementById('total-cost-2')
                total_cost.textContent = '$' + data.get_cart_total.toFixed(2)
            }
            total = data.get_cart_total

            // sets form data for order processing in submitFormData function
            document.getElementById('paypal-payment').classList.add(data.delivery)
        })

        // hiding delivery submission form and revealing payment options
        document.getElementById('continue-button').classList.add('hidden')
        for(let i = 0; i < delivery_forms.length; i++){
            delivery_forms[i].classList.add('hidden')
            delivery_forms[i].parentElement.parentElement.classList.remove('col-md-8')
            delivery_forms[i].parentElement.parentElement.classList.add('col-md-4')
        }
        nav_tabs = document.getElementsByClassName('nav-tabs')
        for(let i = 0; i < nav_tabs.length; i++){
            nav_tabs[i].classList.add('hidden')
        }
        document.getElementById('paypal-payment').classList.remove('hidden')
    })
}


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


// sets form data for order processing in submitFormData function
form = document.getElementById.on('submit')


// Processes Order
function submitFormData(){
    console.log('Payment button clicked')

    var userFormData = {
        'name': null,
        'email': null,
        'total': total
    }

    // retrieves form data
    paypal = document.getElementById('paypal-payment')
    if (paypal.classList.contains('Shipping')){
        form = document.getElementById('shipping_form')
    } else if (paypal.classList.contains('Pick-up')){
        form = document.getElementById('pick_up_form')
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

    let url = '/user/process-order/'
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
