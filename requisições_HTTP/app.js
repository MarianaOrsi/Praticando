//MÉTODO XMLHttpRequest

/* const listaPosts = document.querySelector("#listaPosts");
const httpRequest = new XMLHttpRequest();
httpRequest.open("GET", "https://jsonplaceholder.typicode.com/posts");
httpRequest.send();
// console.log(httpRequest);
let posts;

httpRequest.onreadystatechange = function () {
    if (httpRequest.readyState === 4 && httpRequest.status === 200) {
        posts = JSON.parse(httpRequest.response);
        // console.log(httpRequest.response);
        exibePosts();
    }

} 
*/



//MÉTODO FETCH

/* const listaPosts = document.querySelector("#listaPosts");

fetch("https://jsonplaceholder.typicode.com/posts")
    .then((response) => response.json())
    .then((json) => {
        posts = json;
    })
    .then(() => {
        exibePosts();
    })

function exibePosts() {
    setTimeout(() => {
        let saida = "";
        posts.forEach((post) => {
            saida += `<li> ${post.title} </li><li> ${post.body} <hr></hr><li>`

        });
        listaPosts.innerHTML = saida;
    }, 3000)
};  */



//MÉTODO POST 

/* const listaPosts = document.querySelector("#listaPosts");

fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    body: JSON.stringify({
        title: "new post",
        body: "corpo do novo post",
        userId: 5,
    }),
    headers: {
        'Content-type': 'aplication/json; charset=UTF-8',
    },
})
    .then((response) => response.json())
    .then((json) => {
        posts = json;
    })
    .then(() => {
        console.log(posts);
        // exibePosts();
    }) */



// MÉTODO PUT

const listaPosts = document.querySelector("#listaPosts");

fetch("https://jsonplaceholder.typicode.com/posts/2", {
    method: "PUT",
    body: JSON.stringify({
        title: "new post",
        body: "corpo do novo post - atualização",
        userId: 5,
    }),
    headers: {
        'Content-type': 'aplication/json; charset=UTF-8',
    },
})
    .then((response) => response.json())
    .then((json) => {
        posts = json;
    })
    .then(() => {
        console.log(posts);
        // exibePosts();
    })