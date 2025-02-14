$(document).ready(function() {
    $('#submit-review').click(function(event) {
        event.preventDefault();

        let form = $('#id-add-review');
        let ksiazkaId = $('#ksiazka_id').val();
        let formData = form.serialize();

        $.ajax({
            url: window.location.pathname,  // Wysyłamy do tego samego widoku
            type: 'POST',
            data: formData,
            dataType: "json",
            headers: {'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()},
            success: function(response) {
                if (response.success) {
                    let recenzjaHTML = `
                        <div class="review border p-3 my-2">
                            <strong>${response.autor}</strong>
                            <span class="text-warning">(${response.ocena} ★)</span>
                            <p>${response.tresc_recenzji}</p>
                        </div>
                    `;
                    $('#recenzje').prepend(recenzjaHTML);
                    $('#srednia-ocena').text(response.srednia_ocena);
                    alert("Recenzja dodana!");
                    form[0].reset();
                } else {
                    alert("Błąd: " + JSON.stringify(response.errors));
                }
            },
            error: function(xhr) {
                if (xhr.status === 403) {
                    alert("Tylko zalogowany użytkownik może dodać recenzję i ocenę!");
                } else {
                    alert("Wystąpił błąd podczas dodawania recenzji.");
                }
            }
        });
    });
});