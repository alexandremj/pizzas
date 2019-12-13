function getFormData() {
    var form = document.forms["pizzaForm"];

    // gets relevant data
    var place = form.place.value;
    var grade = form.grade.value;
    var details = form.details.value;

    const url = 'https://alexandremj.github.io/api/pizza/';
    const parameters = {
        headers: {
            "content-type": "application/json; charset=UTF-8"
        },
        body: {
            place: place,
            grade: grade,
            details: details
        },
        method: "POST"
    };

    fetch(url, parameters)
    .then(data=>{ alert(data.json())} )
    .catch(err=>{ alert(err)} );
}

// ToDo implement
function getAllPizzaPlaces() {
    alert("getAllPizzaPlaces()");
}

// ToDo implement
function getSpecificPlace() {
    alert("getSpecificPlace()");
}

function clearTextField() {

}