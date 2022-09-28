const texte1 = document.querySelector('.rubber-band');
const texte2 = texte1.textContent;
const texte3 = texte2.replace(/%/g, "%")
const letters = texte3.split('');

let html = "";

const makespan = letter => `<span class="rubber-letter">${letter}</span>`;

letters.forEach(letter => (html += makespan(letter)))

const term = html.replace(/%/g, '<br>');

texte1.innerHTML = term;
