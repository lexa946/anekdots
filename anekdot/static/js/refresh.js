document.addEventListener("DOMContentLoaded", function(){

    let refreshButton = document.querySelector('#refresh');
    let anekdotCards = document.querySelectorAll('.anekdot_card')

    async function clickRefresh(event) {
        for (let i = 0; i < 3; i++){
            let response = await fetch(location.protocol + '//' + location.host+'/anekdot/api/anekdot/random');
            let json = await response.json();

            let anekdotText = json['anekdot']['text'];
            let author = json['anekdot']['author'];

            let anekdotCard = anekdotCards[i];

            let headerLink = anekdotCard.querySelector(".card-header a");
            console.log(author);
            if (author === null){
                headerLink.setAttribute('href', '#');
                headerLink.innerHTML = 'Неизвестный';
            }else{
                headerLink.setAttribute('href', author['link']);
                headerLink.innerHTML = author['name'];
            };


            anekdotCard.querySelector('p.card-text').innerHTML = anekdotText;

            let likeButton = anekdotCard.querySelector('.anekdot_manipulation .btn-success');
            console.log(likeButton);
            likeButton.setAttribute('anekdot_id', json['anekdot']['id']);
            likeButton.innerHTML = 'Like '+ json['anekdot']['likes'];

            let dislikeButton = anekdotCard.querySelector('.anekdot_manipulation .btn-danger');
            dislikeButton.setAttribute('anekdot_id', json['anekdot']['id']);
            dislikeButton.innerHTML = 'Dislike '+ json['anekdot']['dislikes'];

        };



    };


    refreshButton.addEventListener('click', clickRefresh);


});
