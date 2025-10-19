async function display() {
    let response = await fetch('https://www.themealdb.com/api/json/v1/1/filter.php?c=Seafood');
    let data = await response.json();

    let st = "";
    let item = data['meals'];

    item.forEach((item) => {
        st += `
            <div>
                <img src="${item.strMealThumb}" alt="img">
                <p>${item.strMeal}</p>
            </div>
        `;
    });

    document.getElementById("output").innerHTML = st;
}


