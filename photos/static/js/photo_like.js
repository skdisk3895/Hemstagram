window.onload = function photo_like() {
    const photoLikeButton = document.querySelector('#photoLikeButton')
    // console.log(photoLikeButton)
    photoLikeButton.addEventListener('click', function(event) {
        const photoPk = event.target.dataset.photo_pk
        axios.get(`/photos/${photoPk}/like/`)
            .then(function(res) {
                const likeCount = document.querySelector(`#likeCount${photoPk}`)
                if(res.data.is_liked) {
                    event.target.style.color = 'pink'
                    event.target.classList.value = 'fas fa-heart mr-3'
                } else {
                    event.target.style.color = 'black'
                    event.target.classList.value = 'far fa-heart mr-3'
                }
                likeCount.innerText = res.data.like_count
            })
    })
}