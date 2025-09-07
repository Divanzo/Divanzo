// let heading = document.getElementById('heading');
//     heading.onclick = function() {
//         heading.style.color = 'red';
//     }

// // confirm("우리 홈페이지에 온걸 환영할거임?")
// // alert("우리 홈페이지에 온걸 환영한다.")
// // prompt("사실 환영안함ㅋ 근데 어쩔 수 없이 환영한다고 해야함. 이름은 뭐임?")

// let u_name=prompt("이름을 입력하세요.");
// // document.writeln("<h1>",u_name," 안녕하세요.</h1>");
// console.log(u_name," 안녕하세요.");

// let width = 50;
// let height = 50;
// let area = width * height;
// console.log("사각형의 넓이는 " + area + "입니다.");

// const pi = 3.14;
// let radius = prompt("원의 반지름을 입력하세요.");
// let area = pi * radius * radius;
// console.log("원의 넓이는 " + area + "입니다.");

let U_num=parseInt(prompt('숫자를 입력하세요.'));

if (U_num%3===0)
    console.log('3의 배수입니다.')
else
    console.log('3의 배수가 아닙니다.')