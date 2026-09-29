let cart = [];

function addToCart(name, price) {

    let existingItem = cart.find(item => item.name === name);

    if (existingItem) {
        existingItem.quantity++;
    } else {
        cart.push({
            name: name,
            price: price,
            quantity: 1
        });
    }

    displayCart();
}


function displayCart() {

    let cartDiv = document.getElementById("cart");

    cartDiv.innerHTML = "";

    let total = 0;

    cart.forEach(item => {

        let itemDiv = document.createElement("div");

        itemDiv.innerHTML =
            item.name +
            " - ₹" +
            item.price +
            " × " +
            item.quantity;

        cartDiv.appendChild(itemDiv);

        total += item.price * item.quantity;
    });

    let totalDiv = document.createElement("h3");

    totalDiv.innerHTML = "Total: ₹" + total;

    cartDiv.appendChild(totalDiv);
}


function placeOrder() {

    let address = document.getElementById("address").value;

    if (cart.length === 0) {
        alert("Cart is empty!");
        return;
    }

    if (address.trim() === "") {
        alert("Please enter your delivery address!");
        return;
    }

    let orderDetails = {
        cart: cart,
        address: address
    };

    fetch("/place_order", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(orderDetails)
    })
    .then(response => response.json())
    .then(data => {

        alert(data.message);

        cart = [];

        displayCart();

        document.getElementById("address").value = "";
    })
    .catch(error => {

        console.error("Error:", error);

        alert("Something went wrong!");

    });
}