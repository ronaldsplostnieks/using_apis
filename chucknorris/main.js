async function newJoke() {
    const jokes = await fetch(`https://api.chucknorris.io/jokes/random`);
    data = await jokes.json();
    document.getElementById('jokePlace').innerHTML = data.value;
    // document.getElementById('jokePlace').innerHTML = JSON.stringify(data);
}

