document.addEventListener('DOMContentLoaded', function() {
    // Verifica se existe alguma mensagem de sucesso
    const messageContainer = document.querySelector('.alert-success');
    if (messageContainer && messageContainer.textContent.trim() !== '') {
        // Mostra o modal de sucesso
        const successModal = new bootstrap.Modal(document.getElementById('successModal'));
        successModal.show();
    }
});