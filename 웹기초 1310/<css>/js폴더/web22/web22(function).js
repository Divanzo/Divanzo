// function add(){
//     let num1=2;
//     let num2=3;
//     let result = num1 + num2;

//     console.log("결과: " + result);
// }

// add();
// add();

////////////////////////////////////////////////////////

// var sum=0;
// var result;

// function add(){
//     sum=10+20;
//     result = 10*20;
// }

// add();
// console.log(result);
// console.log(sum);

/////////////////////////////////////////////////////////

// var x = 10;

// function display() {
//     console.log("x is " + x);
//     console.log("y is " + y);
//     let y = 20;
// }

// display();

////////////////////////////////////////////////////////

// var a=2;
// var a=3;
// console.log(a);

// let b=2;
// b=5;
// console.log(b);

/////////////////////////////////////////////////////////

// function add(num1,num2){
//     let sum = num1 + num2;
//     return sum;
// }

// let result=add(2,3);

// console.log("결과: " + result);

/////////////////////////////////////////////////////////

// function multiply(a,b=5,c=10){
//     return a*b+c;
// }

// console.log(multiply(5,10,20));
// console.log(multiply(10,20));
// console.log(multiply(30));

/////////////////////////////////////////////////////////

// let sum=function(a,b){
//     return a + b;
// }
// console.log(sum(10,20));

// (function(a,b){
//     sum=a+b;
// }(100,200));
// console.log(sum);

let sum = (a,b) => a + b;

console.log(sum(10,20));
