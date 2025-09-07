// let U_num=prompt('숫자를 입력하세요.');

// if (U_num != null){
//     if (parseInt(U_num)%3===0)
//         console.log('3의 배수입니다.');
//     else
//         console.log('3의 배수가 아닙니다.');
// }
// else
//     console.log('취소됐습니다.');

// let one=parseInt(prompt('숫자를 입력하세요.'));
// let two=parseInt(prompt('숫자를 입력하세요.'));
// let three=parseInt(prompt('숫자를 입력하세요.'));

///////////////////////////////////////////////////

// if ((one+two+three)/3 >= 60)
//     if (one>=40 && two>=40 && three>=40)
//         console.log('합격')
//     else
//         console.log('불합격')
// else
//     console.log('불합격')

///////////////////////////////////////////////////

// let session=prompt("1.이재명 2.김문수 3.감옥 4.이준석")

// switch(session){
//     case "1": document.writeln("드럼통")
//         break;
//     case "2": document.writeln("당당한 대통령")
//         break;
//     case "3": document.writeln("철컹")
//         break;
//     case "4": document.writeln("지능적인 대통령")
//         break;
//     default: alert("잘못 입력했습니다.");
// }

///////////////////////////////////////////////////

// for (let i=2; i<10; i++){
//     for (let j=1; j<10; j++){
//         console.log(`${i}*${j}=${i*j}`);
//     }
// }

// let stars=parseInt(prompt())
// while (stars>0){
//     document.writeln(`*`);
//     stars--;
// }

let num=parseInt(prompt())
let cnt=0
for(let i=1; i<num; i++){
    if(i%3==0){
        document.writeln(`${i}`);
        cnt++;
    }
}

document.write(cnt)