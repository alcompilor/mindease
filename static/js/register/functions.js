export function dateLimit(type) {
  switch (type) {
    case "max":
      const [maxDate] = new Date(
        new Date().setFullYear(new Date().getFullYear() - 13)
      )
        .toISOString()
        .split("T");
      return maxDate;
    case "min":
      const [minDate] = new Date(
        new Date().setFullYear(new Date().getFullYear() - 90)
      )
        .toISOString()
        .split("T");
      return minDate;
  }
}
