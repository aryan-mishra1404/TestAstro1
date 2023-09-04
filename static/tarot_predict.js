
var lang = document.getElementById('lang');
var lang_value = localStorage.getItem('lang')

document.getElementById(lang_value).setAttribute('selected', true)

// window.onload(()=>{
//     window.scrollTo(0,0)
// })
// window.ready(function(){
//     window.scrollTop(0);
// });

lang.addEventListener('change',()=>{
    lang_value= lang.value;
    // console.log("On change: "+ lang_value);
    localStorage.setItem('lang', lang_value)
    window.location.reload();

})


window.onload = generate_number(0,77);

function generate_number(min, max){
    min = Math.ceil(min);
    max = Math.floor(max);
    let tarot_num= Math.floor(Math.random() * (max - min + 1)) + min;
    let binary_num =  Math.round((Math.random()));
    console.log("Card num : "+tarot_num);
    console.log("Bin_num: "  + binary_num);

    let lang = localStorage.getItem('lang');
    console.log(lang)

    fetchData(tarot_num,binary_num,lang);

}

function fetchData(tarot_num,binary_num, lang){
    fetch (`/tarot/${tarot_num}/${binary_num}`)
    .then(res=>res.json())
    .then(function(data){
        console.log(data)
        document.body.style.visibility= "visible";

        const card_name = data["card_name"];
        const card_image = data["card_image"];
        const property = data["property"];
        const prediction_eng = data["prediction_eng"];
        const prediction_hin = data["prediction_hin"];
    
        property.forEach(ele => {  
            var element =  document.querySelector(".card-points")
            const para = document.createElement("p");
            const node = document.createTextNode(ele);
            para.appendChild(node);
            element.appendChild(para);
        });

        const tc_img = document.getElementById('tc-img');
        tc_img.src =`/static/image/${card_image}`
        document.getElementById('card-name').innerText = `${card_name}`

        if(binary_num == 0){
            tc_img.style.transform ="rotate(180deg)";
            document.getElementById('prediction-heading').innerText ="Prediction Reversed"
        }


        if(lang =="English"){
            document.getElementById('prediction-desc').innerText =prediction_eng
        }
        else{
            document.getElementById('prediction-desc').innerText =prediction_hin
        }
    })
    .catch(error=>console.log(error))



    // fetch (`/tarot_card/${tarot_num}`)
    // .then(async res => {
    //     const data_1 = await res.text();
    //     // console.log(num);
    //     // console.log(data_1);
    //     // parsing of Json string data
    //     const obj = JSON.parse(data_1);
    //     console.log(obj); 
    //     document.body.style.visibility= "visible";

    //     const card_name = obj.card_name;
    //     const card_image = obj.card_image;
    //     const prediction_up_eng = obj.prediction_up_eng;
    //     const prediction_up_hin = obj.prediction_up_hin;
    //     const prediction_down_eng = obj.prediction_down_eng;
    //     const prediction_down_hin = obj.prediction_down_hin;
    //     const property = obj.property;

    //     property.forEach(ele => {
            
    //         var element =  document.querySelector(".card-points")
    //         let div = document.createElement("div")
    //         const para = document.createElement("p");
    //         const node = document.createTextNode(ele);
    //         para.appendChild(node);
    //         element.appendChild(para);
            
    //     });



    //     const tc_img = document.getElementById('tc_img');
    //     tc_img.src =`/static/image/${card_image}`
    //     document.getElementById('card-name').innerText = `${card_name}`

    //     if(binary_num == 0){
            
    //         tc_img.style.transform ="rotate(180deg)";
    //         document.querySelector('.card-upright').style.display="none"
    //     }
    //     else{
    //         document.querySelector('.card-reversed').style.display="none"
    //     }
        

    //     if(lang== "English"){
    //         if(binary_num == 0){
    //             document.getElementById('reversed-prediction').innerHTML=prediction_down_eng
                
    //         }
    //         else{
    //             document.getElementById('upright-prediction').innerHTML = prediction_up_eng
    //         }
    //     }
    //     else{
    //         if(binary_num == 0){
    //             document.getElementById('reversed-prediction').innerHTML=prediction_down_hin
    //         }
    //         else{
    //             document.getElementById('upright-prediction').innerHTML = prediction_up_hin
    //         }
    //     }

    //     // document.querySelector('.tarot-cards').style.visibility= "visible";

    // })
    // .catch(error=>console.log(error))   
    
}