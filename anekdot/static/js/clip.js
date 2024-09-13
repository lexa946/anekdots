document.addEventListener("DOMContentLoaded", function () {
    let clipButtons = document.querySelectorAll('.anekdot_manipulation .btn-primary');


    clipButtons.forEach(button => {
        button.addEventListener('click', event => {
            let anekdot_id = button.parentNode.parentNode.parentNode.getAttribute('anekdot_id');
            let inputClip = button.parentNode.querySelector('input');
            let link = location.protocol + "//"+location.host+"/anekdot/"+anekdot_id;
            inputClip.setAttribute('value', link);
//            navigator.clipboard.writeText(location.protocol + "//"+location.host+"/anekdot/"+anekdot_id).then()
            inputClip.select();
            if(document.execCommand('copy')){
                button.setAttribute('title', 'Ссылка скопирована: '+link)
            }else{
                button.setAttribute('title', 'Не удалось поместить ссылку в буфер: '+link)
            }
        });

    });
})