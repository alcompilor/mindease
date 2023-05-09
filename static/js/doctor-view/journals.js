const cardsContainer = document.getElementById("doctor-journals-cards");

const createCard = (title, content, date) => {
  const cardDiv = document.createElement("div");
  const cardDetails = document.createElement("details");
  const cardSummary = document.createElement("summary");
  const cardPara = document.createElement("p");

  cardDiv.id = "doctor-journal-card";

  cardSummary.innerHTML = `${title} <span id="doctor-journal-date">${date}</span>`;
  cardPara.textContent = content;

  cardDetails.append(cardSummary, cardPara);
  cardDiv.appendChild(cardDetails);

  cardsContainer.appendChild(cardDiv);
};

if (journals.length > 0) {
  const reversedJournals = journals.reverse();

  reversedJournals.forEach((element) => {
    const title = element["journal_content"]["title"];
    const content = element["journal_content"]["content"];
    const date = new Date(
      element["journal_content"]["date"]
    ).toLocaleDateString("sv-SE");

    createCard(title, content, date);
  });
}