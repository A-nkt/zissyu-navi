function likes(event, user, record) {
    console.log(user)
    if(user != "AnonymousUser"){
        /*alert(myurl.base + 'likes/' + user + '/' + hospital_name);*/
        fetch(myurl.base + 'likes/' + user + '/' + record, {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json; charset=utf-8",
                    "X-CSRFToken": Cookies.get('csrftoken'),
                },
            body: JSON.stringify({"status": "requested by javascript."})
            }
        )
        .then(response => response.json())
        .then(json => {
            // json-value
            console.log(json)
            // state of 'like'
            var is_pressed = (event.target.getAttribute("aria-pressed") === "true");
            event.target.setAttribute("aria-pressed", !is_pressed);
            // count of 'like' ±1
            var tag_span = event.target.getElementsByTagName('span')[0];
            coefficient = !is_pressed ? +1 : -1
            cnt = tag_span.innerHTML.match(/\((.+)\)/)[1]; // e.g. (3) => 3
            tag_span.innerHTML = tag_span.innerHTML.replace(cnt, parseInt(cnt) + coefficient);
        })
    } else {
        location.href=myurl.login;
        alert("test2");
    }
}
