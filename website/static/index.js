


function delStaff(id) {
 
  fetch("/delstaff", {
    method: "POST",
    body: JSON.stringify({ id: id }),
  }).then((_res) => {
    window.location.href = "/staff";
  });
}

function getStaff(id){
  
  fetch("/getstaff", {
    method: "POST",
    body: JSON.stringify({ id: id }),
  }).then((response) => {
    return response.json()
  }).then((data) => {
    
    document.getElementById("editH").innerHTML = data.userName;
    document.getElementById("namee").value = data.firstName;
    document.getElementById("emaile").value = data.email;
    document.getElementById("rolee").innerHTML = `<option value="${data.role}">${data.role}</option>
    <option value="Admin">Admin</option>
    <option value="Host">Host</option>
    <option value="Security">Security</option>`;
    document.getElementById("empIDe").value = data.empID;
    document.getElementById("badgeIDe").value = data.badgeID;
    document.getElementById("departe").value = data.depart;
  });
}