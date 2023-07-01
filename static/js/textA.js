const rubberBands = document.querySelectorAll('.rubber-band');

rubberBands.forEach(rubberBand => {
  const texte2 = rubberBand.textContent;
  const texte3 = texte2.replace(/%/g, "%");
  const letters = texte3.split('');

  let html = "";

  const makespan = letter => `<span class="rubber-letter">${letter}</span>`;

  letters.forEach(letter => (html += makespan(letter)));

  const term = html.replace(/%/g, '<br>');

  rubberBand.innerHTML = term;
});
