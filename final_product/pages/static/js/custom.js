let products = document.querySelectorAll(".product-item");
const gridTwo = document.getElementById("two_items");
const gridThree = document.getElementById("three_items");


gridTwo.addEventListener("click", (e) => {
    e.preventDefault();
    products.forEach(item => {
        if(item.classList.contains("col-lg-4")) {
             item.classList.remove("col-lg-4");
             item.classList.add("col-lg-6");
        }
    })
})

gridThree.addEventListener("click", (e) => {
    e.preventDefault();
    products.forEach(item => {
        if(item.classList.contains("col-lg-6")) {
             item.classList.remove("col-lg-6");
             item.classList.add("col-lg-4");
        }
    })
})
