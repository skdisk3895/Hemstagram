window.onload = function article_like() {
    const likeArticleButton = document.getElementById('likeArticleButton')
    likeArticleButton.addEventListener('click', function(event) {
        const articlePk = event.target.dataset.article_pk
        axios.get(`/articles/${articlePk}/like/`)
            .then(function(res) {
                    // console.log(res.data)
                    const likeUsers = document.querySelector(`#likeUsers${articlePk}`)
                    // console.log(likeUsers)
                    if (res.data.is_liked) {
                        event.target.innerText = '좋아요 해제'
                    }else {
                        event.target.innerText = '좋아요'
                    }
                    idx = 0
                    obj = res.data.result
                    var names = ''
                    while (obj[idx]) {
                        const name = obj[idx]['username']
                        names += name
                        names += ' '
                        idx++
                    }
                    console.log(names)
                    likeUsers.innerText = names
                })
            // .catch(function(err) {
            //     console.log(err)
            // })
    })
}