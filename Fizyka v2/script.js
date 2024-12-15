// Funkcja do obliczenia Usk i Epsilon Max
function obliczUskEpsilon() {
    // Pobieramy wartości z formularza
    const zwoje = parseFloat(document.getElementById('zwoje').value);
    const poleMagnetyczne = parseFloat(document.getElementById('poleMagnetyczne').value);
    const powierzchnia = parseFloat(document.getElementById('powierzchnia').value);
    const okres = parseFloat(document.getElementById('okres').value);

    // Obliczenie Epsilon Max (maksymalne napięcie indukowane)
    const omega = (2 * Math.PI) / okres
    const epsilonMax = zwoje * powierzchnia * poleMagnetyczne * omega; // wzór: E = N * A * B / T
    const usk = epsilonMax / Math.sqrt(2); // Usk = E_max * sqrt(2) (dla sinusoidalnego pola)

    // Wyświetlanie wyników
    document.getElementById('usk').innerText = usk.toFixed(2);
    document.getElementById('epsilonMax').innerText = epsilonMax.toFixed(2);

    // Rysowanie wykresu sinusoidalnego
    rysujWykresSinusoidalny(okres);
}

// Funkcja do rysowania wykresu sinusoidalnego
function rysujWykresSinusoidalny(okres) {
    const ctx = document.getElementById('chart').getContext('2d');
    const t = [];
    const y = [];

    // Generowanie danych do wykresu
    for (let i = 0; i <= 2 * Math.PI; i += 0.1) {
        t.push(i);
        y.push(Math.sin(i));
    }

    // Tworzenie wykresu
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: t.map(val => (val * okres / (2 * Math.PI)).toFixed(2)), // Przekształcamy jednostki czasowe
            datasets: [{
                label: 'Wykres Sinusoidalny',
                data: y,
                borderColor: 'rgba(75, 192, 192, 1)',
                fill: false,
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Czas (s)'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Amplituda'
                    }
                }
            }
        }
    });
}

// Dodanie nasłuchiwania na formularz
document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();
    obliczUskEpsilon();
});
