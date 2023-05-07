let popup = document.getElementById("popup");
let blackLayer = document.getElementById("black-layer");

function openPopup() {
    popup.classList.add("open-popup");
    blackLayer.style.display = "block";
}

function closePopup() {
    popup.classList.remove("open-popup");
    blackLayer.style.display = "none";
}

window.addEventListener('load', function() {
    openPopup();
});