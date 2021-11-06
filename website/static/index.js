


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
    // let dataAnggota = "" 
    // for anggota of data.anggota{
    //   dataAnggota += `<tr >
    //     <th scope="row">1</th>
    //     <td>${anggota.nama}</td>
    //     <td>Jabatan</td>
    //     <td>${anggota.nik}</td>
    //     <td style="text-align: center; vertical-align: middle;"><i class="ri-checkbox-circle-line"></i></td>
    //     <td style="text-align: center; vertical-align: middle;"><i class="ri-checkbox-circle-line"></i></td>
    //   </tr>`
    // }
    
    document.getElementById("permitDetailVendor").innerHTML = data.vendor
    document.getElementById("permitDetailDate").innerHTML = data.startDate + " until " + data.endDate
    document.getElementById("permitDetailPurpose").innerHTML = data.purpose
    // document.getElementById("permitDetailAnggota").innerHTML = dataAnggota

    let tableRef = document.getElementById('permitDetailAnggota');
    var tableHeaderRowCount = 1;
    var rowCount = tableRef.rows.length;
    for (var i = tableHeaderRowCount; i < rowCount; i++) {
        tableRef.deleteRow(tableHeaderRowCount);
    }
    let noUrut = 0
    for (anggota of data.anggota) {
    // Insert a row at the end of the table
      let newRow = tableRef.insertRow(-1);

      // Insert a cell in the row at index 0
      let newCell = newRow.insertCell(0);
      let newCell1 = newRow.insertCell(1);
      let newCell2 = newRow.insertCell(2);
      let newCell3 = newRow.insertCell(3);
      // Append a text node to the cell
      noUrut += 1
      let newNo = document.createTextNode(noUrut);

      let newName = document.createTextNode(anggota.Nama);
      let newJabatan = document.createTextNode(anggota.Jabatan);
      let newNik = document.createTextNode(anggota.NIK);
      newCell.appendChild(newNo);
      newCell1.appendChild(newName);
      newCell2.appendChild(newJabatan);
      newCell3.appendChild(newNik);
    
    }



  });
}

// <tr >
//   <th scope="row">1</th>
//   <td>Brandon Jacob</td>
//   <td>Designer</td>
//   <td>2832423456543134</td>
//   <td style="text-align: center; vertical-align: middle;"><i class="ri-checkbox-circle-line"></i></td>
//   <td style="text-align: center; vertical-align: middle;"><i class="ri-checkbox-circle-line"></i></td>
// </tr>