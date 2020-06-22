console.log("hello world");
if (localStorage.getItem("cart") == null) {
  let cart = {};
}
else{
  cart = JSON.parse(localStorage.getItem("cart"));
}

$ ('.cart').click(function(){
   console.log("clicked");
});

console.log("ji")


document.querySelector("#lblCartCount").textContent = itemno
document.getElementById('cart').innerHTML = Object.keys(cart).length;


"http://127.0.0.1:8000/media/mobile_image/galaxy_m31.jpg"



function addRow()
{
// get input values
var fname = document.getElementById('fname').value;
var lname = document.getElementById('lname').value;
var age = document.getElementById('age').value;

// get the html table
// 0 = the first table
var table = document.getElementsByTagName('table')[0];

// add new empty row to the table
// 0 = in the top
// table.rows.length = the end
// table.rows.length/2+1 = the center
var newRow = table.insertRow(table.rows.length);

// add cells to the row
var cel1 = newRow.insertCell(0);
var cel2 = newRow.insertCell(1);
var cel3 = newRow.insertCell(2);

// add values to the cells
cel1.innerHTML = fname;
cel2.innerHTML = lname;
cel3.innerHTML = age;
}

            <tr>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Age</th>
            </tr>

            <tr>
                <td>AAAAAA</td>
                <td>BBBBBB</td>
                <td>10</td>
            </tr>

             <tr>
                <td>CCC</td>
                <td>DDDD</td>
                <td>20</td>
            </tr>

             <tr>
                <td>EEE</td>
                <td>FFFFF</td>
                <td>30</td>
            </tr>

             <tr>
                <td>GGGGG</td>
                <td>HHHH</td>
                <td>40</td>
            </tr>

             <tr>
                <td>MMMMMM</td>
                <td>NNNN</td>
                <td>50</td>
            </tr>

        </table>

    </body>

</html>

function myFunction() {
  var x, i;
  x = document.querySelectorAll(".example");
  for (i = 0; i < x.length; i++) {
    x[i].style.backgroundColor = "red";
  }
}


function updateCart(){
  var price = cart[item][2];
  var cost = parseInt(price);
  console.log(typeof(cost));
    if(document.getElementById('op1')){
      document.getElementById('cost').innerHTML = `<i class="fas fa-rupee-sign"></i>${cost*1}`;
    }else if(document.getElementById('op2')){
      document.getElementById('cost').innerHTML = `<i class="fas fa-rupee-sign"></i>${cost*2}`;
  }else if(document.getElementById('op3')){
    document.getElementById('cost').innerHTML = `<i class="fas fa-rupee-sign"></i>${cost*3}`;
}else{
      document.getElementById('cost').innerHTML = `<i class="fas fa-rupee-sign"></i>${cost*4}`;
}};

updateCart();

\
