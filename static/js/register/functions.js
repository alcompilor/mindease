// Function to get max date and min date based on age reqs

export function dateLimit(type) {
  switch (type) {
    case "max": // Based on minimum age of 13
      const [maxDate] = new Date(
        new Date().setFullYear(new Date().getFullYear() - 13)
      )
        .toISOString()
        .split("T");
      return maxDate;

    case "min": // Based on a max age of 90
      const [minDate] = new Date(
        new Date().setFullYear(new Date().getFullYear() - 90)
      )
        .toISOString()
        .split("T");
      return minDate;
  }
}
