// Codi Javascript de la WebApp de viatges 
// HackUPC 2024

// User data
var user_name = "";
var user_location = "";
var selected_interests = [];

// Trip specific data
var trip_destination = "";


function register_step(number) {

    if (number == 0) {

        user_name = document.getElementById("register_name").value;
        user_location = document.getElementById("register_location").value;

        document.getElementById("register_image").style.display = "none";

        document.getElementById("register_header").innerHTML = "Què t'agrada?";
        document.getElementById("register_header").style.marginTop = "40px";
        document.getElementById("register_subheader").innerHTML = "Tria les teves preferències";
    
        document.getElementById("register_form_1").style.display = "none";
        document.getElementById("register_form_2").style.display = "block";

    }

    else if (number == 1) {

        document.getElementById("register").style.display = "none";
        document.getElementById("location_search").style.display = "block";

    }
    
}



function add_interest(number) {

    if (selected_interests.includes(number)) {

        selected_interests.splice(selected_interests.indexOf(number), 1);

        document.getElementById("interest_" + number.toString()).style.backgroundColor = "white";

        document.getElementById("interest_" + number.toString()).style.color = "rgb(17 24 39/var(--tw-text-opacity))";


    }

    else {

        selected_interests.push(number);

        document.getElementById("interest_" + number.toString()).style.backgroundColor = "rgb(243 244 246/var(--tw-bg-opacity))";

        document.getElementById("interest_" + number.toString()).style.color = "rgb(26 86 219/var(--tw-text-opacity))";

    }

}



// Location search

var search_token = "";

document.getElementById("location_search_form").addEventListener('submit', function(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    search_token = document.getElementById("city_search").value;

    token_amadeus();
});

/* AMADEUS TOKENS REQUEST */

function token_amadeus() {
    const url = 'https://test.api.amadeus.com/v1/security/oauth2/token';
const parametros = new URLSearchParams();
parametros.append('grant_type', 'client_credentials');
parametros.append('client_id', 'Ose9ob5IIeinc6vUKXX92l9oBZy85TTr');
parametros.append('client_secret', 'kahbv7Nw0zGMq1dt');

const opciones = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: parametros.toString()
};

fetch(url, opciones)
  .then(response => {
    if (!response.ok) {
      throw new Error('Error en la solicitud: ' + response.status);
    }
    return response.json();
  })
  .then(data => {
    console.log('Respuesta:', data["access_token"]);
    // Haz algo con los datos recibidos aquí
    handle_action_amadeus(data["access_token"]);

  })
  .catch(error => {
    console.error('¡Hubo un error!', error);
  });
}


// Once we get the token, make the request!
function handle_action_amadeus(token) {

    // Decide action segons variable global
    get_location(search_token, token);

}








function get_location(keyword_user, token_user) {


// Construct the URL with the custom keyword
const url = `https://test.api.amadeus.com/v1/reference-data/locations/cities?max=10&keyword=${encodeURIComponent(keyword_user)}`;

// Make the API request
fetch(url, {
  headers: {
    'Authorization': `Bearer ${token_user}`
  }
})
.then(response => {
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
})
.then(data => {
  // Process the response
  console.log(data["data"]); // This will log the cities starting with the custom keyword

  // Create dynamic cards for each result
  create_location_cards(data["data"]);
})
.catch(error => {
  console.error('There was a problem with the fetch operation:', error);
});


}




// Dynamically add city selection buttons to the page
function create_location_cards(cities) {

    for (var element of cities) {

        var name = element["name"];
        var state = element["address"]["countryCode"];
        var code = element["iataCode"];

        var card = `
        <button onclick="select_destination('${name}');" type="button" id="${name}" class="city_button py-2.5 px-5 me-2 mb-2 text-sm font-medium text-gray-900 focus:outline-none bg-white rounded-full border border-gray-200 hover:bg-gray-100 hover:text-blue-700 focus:z-10 focus:ring-4 focus:ring-gray-100 dark:focus:ring-gray-700 dark:bg-gray-800 dark:text-gray-400 dark:border-gray-600 dark:hover:text-white dark:hover:bg-gray-700">${name}</button>
        </div>
        `;

        // Append to city_search_results
        document.getElementById("city_search_results").innerHTML += card;

    }
    
}




function select_destination(destination) {

    trip_destination = destination;

    document.getElementById("location_search").style.display = "none";
    document.getElementById("date_selector").style.display = "block";

}


function save_dates() {

    document.getElementById("date_selector").style.display = "none";
    document.getElementById("budget_selector").style.display = "block";
}


