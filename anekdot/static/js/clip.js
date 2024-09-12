document.addEventListener("DOMContentLoaded", function () {
    let clipButtons = document.querySelectorAll('.anekdot_manipulation .btn-primary');


    clipButtons.forEach(button => {
        button.addEventListener('click', event => {
            let anekdot_id = button.parentNode.parentNode.parentNode.getAttribute('anekdot_id');
            let link = location.protocol + "//"+location.host+"/anekdot/"+anekdot_id;
            navigator.clipboard.writeText(location.protocol + "//"+location.host+"/anekdot/"+anekdot_id).then()
            button.setAttribute('title', 'Ссылка скопирована: '+link)
        });

    });
})