
let count = 0;
function color(color){

        document.getElementById("Title").style.backgroundColor= color;
}

let arr = [3,2,5,2,2,43,3];

let person_arr = [];

var person  = {"first_name": "mark", "last_name": "said"};

person_arr.push(person);

document.getElementById("end_p").innerHTML = JSON.stringify(person_arr);


    document.getElementById("ol").innerHTML += "<ol>";
    for(let i in arr){

        document.getElementById("ol").innerHTML += "<li>" + arr[i] + "</li>";

    }
    document.getElementById("ol").innerHTML += "</ol>";
