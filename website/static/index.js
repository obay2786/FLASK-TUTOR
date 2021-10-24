function nama() {

  setInterval(function () {
  fetch('https://www.motogp.com/en/json/event_bar')
  .then((response) => {
    return response.json()
  })
  .then((data) => {
    // Work with JSON data here
    document.getElementById("editData").innerHTML = data.next_session
    
  })
  .catch((err) => {
    // Do something for an error here
  })
  },1000);
}

  window.addEventListener('DOMContentLoaded', (event) => {
   nama();
});
