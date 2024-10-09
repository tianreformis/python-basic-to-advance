const fetchAllTodos = () => { //arrow function
    return fetch('https://www.amiiboapi.com/api/')
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