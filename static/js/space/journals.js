const saveBtn = document.getElementById("journal-btn"); // journal save btn
const journalForm = document.getElementById("journal-form"); // journal form
const journalSubmissionDate = document.getElementById(
  "journal-submission-date"
); // journal submission date (hidden)

const journalSearchInput = document.getElementById("journal-search-input"); // journal search bar
const journalSearchButton = document.getElementById("journal-searchbtn"); // journal search btn

const cardsContainer = document.getElementById("myspace-journals-cards"); // journal cards main container

saveBtn.addEventListener("click", () => {
  journalSubmissionDate.value = new Date().toLocaleDateString("sv-SE");
  journalForm.submit();
}); // event listener for save btn to trigger form submit

// Function to create a journal card element
const createCard = (title, content, date) => {
  const cardDiv = document.createElement("div");
  const cardDetails = document.createElement("details");
  const cardSummary = document.createElement("summary");
  const cardPara = document.createElement("p");

  cardDiv.id = "journal-card";

  cardSummary.innerHTML = `${title} <span id="journal-date">${date}</span>`;
  cardPara.textContent = content;

  cardDetails.append(cardSummary, cardPara);
  cardDiv.appendChild(cardDetails);

  cardsContainer.appendChild(cardDiv);
};

if (journals.length > 0) {
  // if theres at least one journal
  const reversedJournals = journals.reverse(); // reorder journals

  reversedJournals.forEach((element) => {
    // create card for each journal
    const title = element["journal_content"]["title"];
    const content = element["journal_content"]["content"];
    const date = new Date(
      element["journal_content"]["date"]
    ).toLocaleDateString("sv-SE");

    createCard(title, content, date);
  });
}

// Fetch all the details element.
const details = document.querySelectorAll("details");

// Add the onclick listeners.
details.forEach((targetDetail) => {
  targetDetail.addEventListener("click", () => {
    // Close all the details that are not targetDetail.
    details.forEach((detail) => {
      if (detail !== targetDetail) {
        detail.removeAttribute("open");
      }
    });
  });
});

const searchParams = new URLSearchParams(window.location.search); // store url params
const isSearch = searchParams.has("q"); // check if theres a search param

const card = document.getElementById("journal-card"); // check if theres any rendered journal cards

if (!card && !isSearch) {
  // if no rendered cards & if no search param
  document.getElementById("journals-none").textContent =
    "You have no journals. Add a few but keep in mind that journals can't be deleted nor edited 😉";
}

if (!card && isSearch) {
  // if no rendered cards & if search param exists
  document.getElementById("journals-none").textContent =
    "There were no journals found 👀";
}

if (isSearch) {
  // if search param
  query = searchParams.get("q");
  if (query != "") {
    // if search param not empty
    journalSearchInput.value = searchParams.get("q"); // update search bar with param value
  }
}
