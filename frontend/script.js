async function load_fruits() {
  try {
    // Daten aus dem Backend abrufen mit fetch ...
    let response = await fetch("http://127.0.0.1:8000/fruit/");
    // Daten in response nun mit json() in ein JSON umwandeln ...
    let data = await response.json();
    console.log("Daten vom Backend:");
    console.log(data);
    let list = document.getElementById("fruit_list");

    data.fruits.forEach(function (fruit) {
      let listItem = document.createElement("li");
      listItem.textContent =
        "Name: " +
        fruit.name +
        " | Gewicht: " +
        fruit.weight +
        " g" +
        " | Farbe; " +
        fruit.color;
      list.appendChild(listItem);
    });
  } catch (error) {
    console.log("Fehler: ", error);
  }
}

load_fruits();
