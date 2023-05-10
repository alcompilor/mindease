const copyKeyBtn = document.getElementById("key-copy");

const copyKey = () => {
  // Get the text field
  var copyText = document.getElementById("key-container");

  // Copy the text inside the text field
  navigator.clipboard.writeText(copyText.textContent.trim());
};

copyKeyBtn.addEventListener("click", copyKey); // copy doctor key event listener
