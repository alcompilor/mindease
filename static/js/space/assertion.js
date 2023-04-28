const assertionEl = document.getElementById("assertion");

async function reqAssertion() {
  const assertion = await fetch("https://www.affirmations.dev", {
    method: "GET",
    headers: {
      Accept: "application/json",
    },
  }).then((response) => response.json());
  return await assertion.affirmation;
}

reqAssertion().then((res) => {
  assertionEl.textContent = res;
});
