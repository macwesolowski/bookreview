document.addEventListener('DOMContentLoaded', function() {
    const clearButton = document.getElementById('clear-filters');
    const filterForm = document.getElementById('filter-form');

    // Funkcja do czyszczenia filtrów
    if (clearButton) {
        clearButton.addEventListener('click', function() {
            // Resetuje wszystkie pola formularza
            event.preventDefault();
            filterForm.reset();

            // Zresetuj wszystkie selecty (jeśli są używane)
            const selects = filterForm.querySelectorAll('select');
            selects.forEach(select => select.value = '');

            // Opcjonalnie: Możesz także wyczyścić URL, by odświeżyć filtry
            window.location.href = window.location.pathname;
        });
    }
});