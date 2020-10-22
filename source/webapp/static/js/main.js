
function jqueryParseData (response, status) {
    location.reload(true)

    console.log(response);
    console.log(status);
}

function jqueryAjaxError(response, status) {
    console.log(response);
    console.log(status);
    console.log('error');
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
let csrftoken = getCookie('csrftoken');

function createTasksLoadIndex(text, author, image_id) {
    $.ajax({
        url: 'http://localhost:8000/api/comments/',
        method: 'POST',
        contentType: 'application/json',
        headers: {'X-CSRFToken': csrftoken},
        data: JSON.stringify({text: text, author: author, image: image_id}),
        dataType: 'json',
        success: jqueryParseData,
        error: jqueryAjaxError
    })
}

function deleteTasksLoadIndex(comment_id) {
    $.ajax({
        url: 'http://localhost:8000/api/comments/' + comment_id,
        method: 'DELETE',
        contentType: 'application/json',
        headers: {'X-CSRFToken': csrftoken},
        dataType: 'json',
        success: jqueryParseData,
        error: jqueryAjaxError
    })
}