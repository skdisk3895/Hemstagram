window.onload = function like() {
    const likeArticleButton = document.getElementById('likeArticleButton')
    likeArticleButton.addEventListener('click', function(event) {
        const articlePk = event.target.dataset.article_pk
        axios.get(`/articles/${articlePk}/like/`)
            .then(function(res) {
                    const likeUsers = document.querySelector(`#likeUsers${articlePk}`)
                    if (res.data.is_liked) {
                        event.target.innerText = '좋아요 해제'
                    }else {
                        event.target.innerText = '좋아요'
                    }
                    idx = 0
                    obj = res.data.result
                    var names = ''
                    while (obj[idx]) {
                        names += obj[idx]['username']
                        names += ' '
                        idx++;
                    }
                    console.log(names)
                    console.log(typeof names)
                    likeUsers.innerText = names
                })
            .catch(function(err) {
                console.log(err)
            })
    })
}