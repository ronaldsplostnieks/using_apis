var categoriesArray = ["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music","political","religion","science","sport","travel"];
var dropdown = document.getElementById("categorieSelect");

categoriesArray.forEach(function(category, i) {
    var option = document.createElement("option");
    option.value = category;
    option.text = category;
    option.id = i;
    dropdown.add(option);
});

async function newJoke() {
    var selectedCategory = dropdown.options[dropdown.selectedIndex].value;
    const jokes = await fetch(`https://api.chucknorris.io/jokes/random?category=${selectedCategory}`);
    data = await jokes.json();
    document.getElementById('jokePlace').innerHTML = data.value;
}