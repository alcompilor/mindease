let popup = document.getElementById("popup");
let blackLayer = document.getElementById("black-layer");

let averageElement = document.getElementById("answer_average");
let answerAverage = averageElement.dataset.answerAverage;

let element = document.querySelector('.progress-circle');
element.style.setProperty('--percent', answerAverage);

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