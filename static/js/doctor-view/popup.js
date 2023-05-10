let popup = document.getElementById("popup");
let blackLayer = document.getElementById("black-layer");

function openPopup() {
  popup.classList.add("open-popup");
}

function closePopup() {
  popup.classList.remove("open-popup");
  blackLayer.style.display = "none";
}

(function makeBlury() {
  blackLayer.style.display = "block";
})();

window.addEventListener("load", function () {
  openPopup();
});
