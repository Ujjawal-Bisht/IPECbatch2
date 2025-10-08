// If-else

let age = 20;
if (age >= 18){
    console.log("You are eligible.");
}else{
    console.log("You are not eligible.");
}


let marks = 100;
let attendance = 40;
if (marks>100 || marks<0 || attendance>100 || attendance<0){
    console.log("Invalid Marks, Attendance!!!");
}else if(marks>90 && attendance>75){
    console.log("A");
}else if(marks>80 && attendance>65){
    console.log("B");
}else{
    console.log("Passed.")
}

// switch()