const assertionEl = document.getElementById("assertion"); // assertion container
const newAssertion = document.getElementById("assertion-new"); // new assertion btn

// Async function to get assertion from external api
async function reqAssertion() {
  const assertion = await fetch("https://www.affirmations.dev", {
    method: "GET",
    headers: {
      Accept: "application/json",
    },
    mode: "no-cors",
  }).then((response) => response.json());
  return await assertion.affirmation;
};

// Function to render assertion fetched from the async function
const renderAssertion = () => {
  reqAssertion().then((res) => {
    assertionEl.textContent = res;
  });
};

newAssertion.addEventListener("click", renderAssertion); // event listener for assertion btn
renderAssertion(); // render assertion on first page load
