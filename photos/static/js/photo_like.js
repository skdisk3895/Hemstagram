window.onload = function like() {
    const photoLikeButton = document.querySelector('#photoLikeButton')
    console.log(photoLikeButton)
    photoLikeButton.addEventListener('click', function(event) {
        console.log(event)
    })
}