let numerology_name = localStorage.getItem('numerolgoy_name')
console.log("name:"+ numerology_name)
let numerology_date = localStorage.getItem('numerology_date')
console.log("date:"+ numerology_date)
var lang = document.getElementById('lang');
let bhagyank;
let moolank;
// var lang_value = lang.value
// console.log(lang_value)
lang_value = localStorage.getItem('lang')
console.log(lang_value)
lang.value = lang_value;
console.log("lang: " +lang.value);
document.getElementById(lang_value).setAttribute('selected', true)

lang.addEventListener('change',()=>{
    
    lang_value= lang.value;
    console.log("On change: "+ lang_value);
    localStorage.setItem('lang', lang_value);
    window.location.reload();
})

//Numerology-report
document.getElementById('numerology_name').innerText = numerology_name
document.getElementById('numerology_date').innerText = numerology_date


// Numerology
fetch(`/numerology_prediction/${numerology_date}`)
.then(async res => {
        const data_1 = await res.text();
        // parsing of Json string data
        const obj = JSON.parse(data_1);
        // console.log(obj);
        moolank =obj[0].Moolank;
        bhagyank =obj[0].Bhagyank;
        document.getElementById('moolank').textContent = obj[0].Moolank;
        document.getElementById('bhagyank').textContent = obj[1].Bhagyank;
        
        
        if (lang.value == "English") {
            console.log("Set language english prediction")
            document.getElementById('moolankPrediction').textContent = obj[0].Moolank_Prediction_eng;
            document.getElementById('bhagyankPrediction').textContent = obj[1].Bhagyank_Prediction_eng;
            
        }
        else {
            console.log("Set language hindi prediction")
            document.getElementById('moolankPrediction').textContent  =  obj[0].Moolank_Prediction_hin;
            document.getElementById('bhagyankPrediction').textContent = obj[1].Bhagyank_Prediction_hin;
        }

    })
    .catch(error => console.log(error));

// Chaldean js

let destiny_num_chald = document.getElementById('destiny_num_chald')
let soul_num_chald = document.getElementById('soul_num_chald')
let dream_num_chald = document.getElementById('dream_num_chald')
// console.log(destiny_num_chald, soul_num_chald, dream_num_chald)

// document.getElementById('numerology_name').innerText =numerology_name
fetch(`/chaldean_numerology/${numerology_name}`)
.then(res => res.json())
.then(function (data){
    console.log("Chaldean_Numerology")
    console.log(data)

    destiny_num_chald.innerHTML = data["destiny_number"]
    dream_num_chald.innerHTML = data["dream_number"]
    soul_num_chald.innerHTML = data["soul_number"]

    // console.log(destiny_num)
})
.catch(error => console.log(error));



// pythagorean js

let destiny_num = document.getElementById('destiny_num')
let soul_num = document.getElementById('soul_num')
let dream_num = document.getElementById('dream_num')

// document.getElementById('numerology_name').innerText =numerology_name
fetch(`/pythagorean_numerology/${numerology_name}`)
.then(res => res.json())
.then(function (data){
    console.log("Pythagorean_Numerology")
    console.log(data)
    destiny_num.innerHTML = data["destiny_number"]
    dream_num.innerHTML = data["dream_number"]
    soul_num.innerHTML = data["soul_number"]

    // console.log(destiny_num)
})
.catch(error => console.log(error));



// LOSHUGRID

let grid_container = document.querySelector('.grid-container');

let grid_1 = document.getElementById('1')
let sup_1 = document.querySelector(".one")

let grid_2 = document.getElementById('2')
let sup_2 = document.querySelector(".two")

let grid_3 = document.getElementById('3')
let sup_3 = document.querySelector(".three")

let grid_4 = document.getElementById('4')
let sup_4 = document.querySelector(".four")

let grid_5 = document.getElementById('5')
let sup_5 = document.querySelector(".five")

let grid_6 = document.getElementById('6')
let sup_6 = document.querySelector(".six")

let grid_7 = document.getElementById('7')
let sup_7 = document.querySelector(".seven")

let grid_8 = document.getElementById('8')
let sup_8 = document.querySelector(".eight")

let grid_9 = document.getElementById('9')
let sup_9 = document.querySelector(".nine")


fetch(`/loshugrid_numerology/${numerology_date}`)
    .then(res => res.json())
    .then(function (data) {
        console.log("Loshu Grid\n")
        console.log(data)
        
        if(data["1"]!= 0){
            grid_1.innerHTML = "1"
            sup_1.innerHTML = data["1"]
            // console.log(data["2"])
        }
        
        if(data["2"]!= 0){

            grid_2.innerHTML = "2"
            sup_2.innerText = 2;    
            // console.log(data["2"])
        }


        if(data["3"]!= 0){

            grid_3.innerHTML = "3"
            sup_3.innerHTML = data["3"]
            // console.log(data["2"])
        }


        if(data["4"]!= 0){

            grid_4.innerHTML = "4"
            sup_4.innerHTML = data["4"]
            // console.log(data["2"])
        }


        if(data["5"]!= 0){

            grid_5.innerHTML = "5"
            sup_5.innerHTML = data["5"]
            // console.log(data["2"])
        }


        if(data["6"]!= 0){

            grid_6.innerHTML = "6"
            sup_6.innerHTML = data["6"]
            // console.log(data["2"])
        }


        if(data["7"]!= 0){

            grid_7.innerHTML = "7"
            sup_7.innerHTML = data["7"]
            // console.log(data["2"])
        }


        if(data["8"]!= 0){

            grid_8.innerHTML = "8"
            sup_8.innerHTML = data["8"]
            // console.log(data["2"])
        }

        if(data["9"]!= 0){

            grid_9.innerHTML = "9"
            sup_9.innerHTML = data["9"]
            // console.log(data["2"])
        }

        

        
        
        

        // Object.keys(data).forEach(function(key) {
        //     if(data[key] != 0){
        //         console.log(data[key])

        //         // document.getElementById(key).innerText = key
        //         // document.querySelector(`.${key}`).innerText = data[key]

        //         // for(let i=0; i<data[key]; i++){
        //         //     console.log("into the loop");
        //         //     const gird_item = grid_container.children[key-1];

        //         //     // const div = gird_item.children;
        //         //     const span = document.createElement('span');
        //         //     const text_value = document.createTextNode(key);
        //         //     span.appendChild(text_value)
        //         //     gird_item.appendChild(span)
        //         // }
                
        //         // document.getElementById(key).innerHTML = key;
        //         // document.querySelector(key).innerHTML = data[key];
        //     }
        // });

        // console.log(destiny_num)
    })
    .catch(error => console.log("Loshu error"))









    // button.addEventListner('click',()=>{
    //     show_details();
    // })
    
    // const show_moolank_details = () => {
    
    //     const info = document.createElement("div");
    //     info.classList.add("info");
    //     // info.innerHTML=`
    //     // <h4>Your Moolank is <span id="moolank"></span></h4>
    //     // <h4>Your Moolank Prediction  <br> <span id="moolankPrediction"></span></h4>
    //     // `;
    
    //     info.innerHTML = `
    //         <div>Hello</div>
    //     `
    
    
    //     const moolank_details = document.getElementsByClassName("moolank_details")
    //     moolank_details.style.display="none"
    // }
    
    
    // function show_bhagyank_details() {
    //     const info = document.createElement("div");
    //     info.classList.add("info");
    //     info.innerHTML = `
    //     <h4>Your Bhagyank is <span id="bhagyank"></span></h4>
    //     <h4>Your Bhagyank Prediction says <br> <span id="bhagyankPrediction"></span></h4>
    //     `;
    // }
