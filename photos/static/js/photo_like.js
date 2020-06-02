window.onload = function () {
    this.photoLike()
    this.commentLike()
}

function photoLike() {
    const photoLikeButton = document.querySelector('#photoLikeButton')
    photoLikeButton.addEventListener('click', function(event) {
        const photoPk = event.target.dataset.photo_pk
        const photoLikeCount = document.querySelector(`#photoLikeCount${photoPk}`)
        axios.get(`/photos/${photoPk}/like/`)
            .then(function(res) {
                if(res.data.is_liked) {
                    event.target.style.color = 'pink'
                    event.target.classList.value = 'fas fa-heart photo-liked-heart mr-3'
                } else {
                    event.target.style.color = 'black'
                    event.target.classList.value = 'far fa-heart photo-unliked-heart mr-3'
                }
                console.log(res.data.like_count)
                photoLikeCount.innerText = res.data.like_count
            })
    })
}

function commentLike() {
    const commentLikeButtons = document.querySelectorAll('.commentLikeButton')
    commentLikeButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            const photoPk = event.target.dataset.photo_pk
            const commentPk = event.target.dataset.comment_pk
            const commentLikeCount = document.querySelector(`#commentLikeCount${commentPk}`)
            axios.get(`/photos/${photoPk}/comments/${commentPk}/like/`)
                .then(function(res) {
                    if(res.data.is_liked) {
                        event.target.style.color = 'pink'
                        event.target.classList.value = 'fas fa-heart comment-liked-heart'
                    } else {
                        event.target.style.color = 'black'
                        event.target.classList.value = 'far fa-heart comment-unliked-heart'
                    }
                    commentLikeCount.innerText = res.data.like_count
                })
        })
    })
}