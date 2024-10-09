const fetchAllTodos = () => { //arrow function
    return fetch('https://jsonplaceholder.typicode.com/todos')
        //check response API 
        .then((response) => {
            if (!response.ok) {
                throw new Error("Network Error");
            }
            return response.json();
        })
        //kalau API datanya 
        .then((data) => {
            console.log(data);
            return data;
        })
        //kalau data API nya tidak ada
        .catch((error) => {
            return error;
        })


};
fetchAllTodos(); //return dari arrow function

//DOM Modification
const containerDisplay = document.getElementById('container');
const cardComponent = (title, id,completed) => {
    //buat card 
    const data = `
    <div class="">
        <div>
            <h1 style="font-family:'Poppins'">${id} </h1> 
            <span style="font-family:'Poppins'"> ${title}</span>
            <p style="font-family:'Poppins'"> ${completed}</p>
        </div>
    </div>
    `

    containerDisplay.insertAdjacentHTML('afterbegin', data)
}

function render() {
    fetchA+llTodos()
        .then((response) => {
            response.forEach(result => {
                cardComponent(result.title, result.id,result.completed);
            });
        })
        .catch((error) => {
            alertComponent(error.message)
        });
}

render();