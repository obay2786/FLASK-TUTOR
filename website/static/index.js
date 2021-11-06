


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
    
    document.getElementById("editH").innerHTML = "Username : " + data.userName;
    document.getElementById("userNamee").value = data.userName;
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
function editPhoto(id){
  fetch("/getstaff", {
    method: "POST",
    body: JSON.stringify({ id: id }),
  }).then((response) => {
    return response.json()
  }).then((data) => {
    
    document.getElementById("editPhoto").src = "data:image/png;base64,"+data.photo;
    document.getElementById("editH2").innerHTML = "Username : " + data.userName;
    document.getElementById("userNamePhoto").value = data.userName;
    
  });
}
//data:image/png;base64,{{ user.photo }}

function editPass(id){
  fetch("/getstaff", {
    method: "POST",
    body: JSON.stringify({ id: id }),
  }).then((response) => {
    return response.json()
  }).then((data) => {
    
    
    document.getElementById("editH3").innerHTML = "Username : " + data.userName;
    document.getElementById("userNamePass").value = data.userName;
    
  });
}

//getvisitor
function getVisitor(nik){
  
  fetch("/getvisitor", {
    method: "POST",
    body: JSON.stringify({ nik: nik }),
  }).then((response) => {
    return response.json()
  }).then((data) => {
    
    document.getElementById("idVisitor").value = data.id;
    document.getElementById("nameedit").value = data.nama;
    document.getElementById("nikedit").value = data.nik;
    document.getElementById("companyedit").value = data.company;
    upload(data.photo)
  });
}



function delVisitor(id) {
 
  fetch("/delvisitor", {
    method: "POST",
    body: JSON.stringify({ id: id }),
  }).then((_res) => {
    window.location.href = "/visitor";
  });
}


function editPhotoV(id){
  fetch("/getvisitor", {
    method: "POST",
    body: JSON.stringify({ nik: id }),
  }).then((response) => {
    return response.json()
  }).then((data) => {
   
    document.getElementById("editPhoto").src = "data:image/png;base64,"+data.photo;
    document.getElementById("editH2").innerHTML = "Username : " + data.nama;
    document.getElementById("visitorID").value = data.id;
    
    
    
  });
}


function getPermitdetail(id){
  
  fetch("/permitdetail", {

    method: "POST",
    body: JSON.stringify({ id: id }),
  }).then((response) => {
    return response.json()
  }).then((data) => {
    
    document.getElementById("permitDetailVendor").innerHTML = data.vendor
    
  });
}