const assertionEl = document.getElementById("assertion");
const newAssertion = document.getElementById("assertion-new");

async function reqAssertion() {
  const assertion = await fetch("https://www.affirmations.dev", {
    method: "GET",
    headers: {
      Accept: "application/json",
    },
  }).then((response) => response.json());
  return await assertion.affirmation;
}

const renderAssertion = () => {
  reqAssertion().then((res) => {
    assertionEl.textContent = res;
  });
};

newAssertion.addEventListener("click", renderAssertion);

renderAssertion();
