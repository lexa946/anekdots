document.addEventListener("DOMContentLoaded", function(){


    let likeButtons = document.querySelectorAll('.anekdot_manipulation .btn-success');

    likeButtons.forEach(button =>{
        button.addEventListener('click', event => {
            fetch(location.protocol + '//' + location.host+'/anekdot/api/anekdot/like/' + button.getAttribute('anekdot_id'),
            {
                method: 'POST'
            }).then(response => {

                response.json().then( json => {
                    button.innerHTML = "Like "+ json['likes']
                });
            });
        });
    });

    let dislikeButtons = document.querySelectorAll('.anekdot_manipulation .btn-danger');

    dislikeButtons.forEach(button =>{
        button.addEventListener('click', event => {
            fetch(location.protocol + '//' + location.host+'/anekdot/api/anekdot/dislike/' + button.getAttribute('anekdot_id'),
            {
                method: 'POST'
            }).then(response => {

                response.json().then( json => {
                    button.innerHTML = "Dislike "+ json['dislikes']
                });
            });
        });
    });









});