// let arr1=Array(10);
// let arr2=Array();

// let arr3=[1,2,3,4,5];
// let arr4=Array(1,2,3,4,5);

// for(let i=0; i<arr3.length; i++){
//     console.log(arr3[i]);
// }

/////////////////////////////////////////////////////

// let date_1=new Date("2024");
// let date_2=new Date("2024-02");
// let date_3=new Date("2024-02-03");
// let date_4=new Date("2024-02-03T18:30:00Z");
// let date_5=new Date("02/03/2024");

// console.log(date_5);

// let start=new Date("2025-06-01")
// let today=new Date();

// // let pass_day=today.getDate()-start.getDate();

// let pass_day=today.getTime()-start.getTime();
// pass_day=Math.round(pass_day/1000/60/60/24);

// console.log(pass_day);

// document.querySelector("#p_day").innerText=pass_day;

/////////////////////////////////////////////////////

let people=prompt("응모자 수 몇명임?");

document.querySelector("#all").innerText=people;

let pick=Math.floor(Math.random()*people);
document.querySelector("#select").innerText=pick;

/////////////////////////////////////////////////////

const p_left=window.screenX;
const p_right=window.screenY;

p_left+= 100;
p_right+= 100;
window.open("notice.html", "공지", "width=500", "height=500 , left=${p_left}, top=${p_right}");

function openPopup(params) {
    let newWin=window.open(
        "notice.html",
        "공지",
        "width=500,height=400"
    )
    if (newWin==null){
        alert("팝업이 차단되어 있습니다. 팝업을 허용해주세요.");
    }
}