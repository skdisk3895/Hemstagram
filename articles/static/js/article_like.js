window.onload = function article_like() {
    const likeArticleButton = document.getElementById('likeArticleButton')
    likeArticleButton.addEventListener('click', function(event) {
        const articlePk = event.target.dataset.article_pk
        axios.get(`/articles/${articlePk}/like/`)
            .then(function(res) {
                    console.log(res.data.result)
                    // console.log(res.data.result[0].username)
                    const likeUsers = document.querySelector(`#likeUsers${articlePk}`)
                    // console.log(likeUsers)
                    if (res.data.is_liked) {
                        event.target.innerText = '좋아요 해제'
                    }else {
                        event.target.innerText = '좋아요'
                    }
                    var names = ''
                    res.data.result.forEach(username => {
                        names += username.username
                        names += ' '
                    });
                    console.log(names)
                    console.log(likeUsers)
                    likeUsers.innerText = names 
                })
            // .catch(function(err) {
            //     console.error(err)
            // })
    })
}