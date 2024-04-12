function diz(id){
    console.log(`${id}`);
    fetch(`dizlike/${id}`)
        .then(response => response.text())
        .then(() => window.location.reload())
}

function like(id){
    console.log(`${id}`)
    fetch(`like/${id}`)
        .then(response => response.text())
        .then(() => window.location.reload())
}
