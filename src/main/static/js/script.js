document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.querySelector('.navbar');

    function updateNavbar() {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-sticky'); // Klasa sticky
            navbar.classList.add('bg-darken'); // Jasne tło
            navbar.classList.remove('bg-light');
        } else {
            navbar.classList.remove('navbar-sticky');
            navbar.classList.remove('bg-darken');
            navbar.classList.add('bg-light'); // Pozostaje białe tło
        }
    }

    // Wywołaj funkcję natychmiast przy załadowaniu strony
    updateNavbar();

    // Obsługa scrollowania
    window.addEventListener('scroll', updateNavbar);
});