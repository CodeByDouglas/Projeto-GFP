document.addEventListener('DOMContentLoaded', function() {
    // Select/Deselect all checkboxes
    document.getElementById('select-all').onclick = function() {
        var checkboxes = document.getElementsByName('despesas_selecionadas');
        for (var checkbox of checkboxes) {
            checkbox.checked = this.checked;
        }
    }
});