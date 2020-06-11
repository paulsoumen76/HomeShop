console.log("hello world");
if (localStorage.getItem("cart") == null) {
  let cart = {};
}
else{
  cart = JSON.parse(localStorage.getItem("cart"));
}

$ ('.cart').click(function(){
   console.log("clicked");
});

console.log("ji")


document.querySelector("#lblCartCount").textContent = itemno
document.getElementById('cart').innerHTML = Object.keys(cart).length;
