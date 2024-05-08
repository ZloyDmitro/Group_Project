(function () {

    const btnDelete = document.querySelectorAll(".btnDelete");

    btnDelete.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmation = confirm('Are you sure to remove the supplier');
            if (!confirmation) {
                e.preventDefault();
            }
        });
    });
    
})();