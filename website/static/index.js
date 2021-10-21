function nama() {
  fetch('/nama')
  .then((response) => {
    return response.json()
  })
  .then((data) => {
    // Work with JSON data here
    document.getElementById("editData").innerHTML = data.nama
    
  })
  .catch((err) => {
    // Do something for an error here
  })
  }