let x = document.getElementsByTagName("input").value;
let y = document.getElementById("num2").value;
x = 9
y = 2
function add(){
    let add = x+y
 document.getElementById("sum").innerHTML= x + " + " + y +" = "+add;
}
function sub(){
    let add = x-y
 document.getElementById("sum").innerHTML=x + " - " + y +" = "+add;
}
function mul(){
    let add = x*y
 document.getElementById("sum").innerHTML=x + " * " + y +" = " +add;
}
function div(){
    let add = x/y
 document.getElementById("sum").innerHTML=x + " / " + y +" = " + add;
}