function sendArticleComment() {
    // console.log('submit article comment');
    var comment = $('#commentText').val();

    $.get('/articles/add-article-comment', {
        articleComment: comment,
        articleId: 23,
        parentId: null
    }).then(res => {
        console.log(res);
    });

    // ajax => asynchronous javascript and xml
    // json => javascript object notation
}