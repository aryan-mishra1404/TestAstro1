var lang = document.getElementById('lang');
var lang_value = lang.value
console.log(lang_value)
lang_value = localStorage.getItem('lang')
console.log(lang_value)
document.getElementById(lang_value).setAttribute('selected', true)

lang.addEventListener('change',()=>{
    lang_value= lang.value;
    console.log("On change: "+ lang_value);
    localStorage.setItem('lang', lang_value)
})

//Numerology Form


let form = document.getElementById("form");
var numerology_name = document.getElementById("name");
var name_value = numerology_name.value;

var date = document.getElementById("date");
var date_value = date.value;


let uid = localStorage.getItem('uid')
let userid = document.getElementById("userid")

// let numerology_history = document.querySelector('.history-details')
let numerology_history = document.getElementById('history-details')
let historyBtn = document.getElementById('history-btn')
let name_data=[];
let date_data=[];



window.addEventListener("load", () => {
    userid.value = uid;

    // The event listner is not working but why?
    document.getElementById('submit-button').addEventListener('click',()=>{

        let name_value = numerology_name.value;
        let date_value = date.value;
   
        localStorage.setItem('numerolgoy_name', name_value)
        localStorage.setItem('numerology_date',date_value)
        // alert(name_value+ date_value)
        window.location.assign("/numerology_prediction")
    })

    document.getElementById('history-btn').addEventListener('click',()=>{
        if(historyBtn.innerText == "Hide History"){
           
            // numerology_history.style.display ="none";
            // historyBtn.innerText = "Show Horoscopic Predictions"
            
         // this will led to again and again fetching of data form the db instead of showing the already fetched data
            window.location.reload()
        }
        else{
            // alert("Show History")

            fetch(`/PredictionHistory/${uid}`)
            .then(res=> res.json())
            .then(function (data){
                console.log(data); 
                if(data.length == 0){
                    alert("No Previous History")
                }
                else{
                    data.forEach(ele => {

                        name_data.push(ele[1])
                        date_data.push(ele[3])

                        // console.log(name_data);
                        // console.log(date_data);
                        // since element is in list Format
                        // para.setAttribute("id",`prediction${count}`)
                        var para = document.createElement('p')
                        var text_node = document.createTextNode(`${ele[1]} - ${ele[3]} (${ele[4]})`)
                        para.appendChild(text_node)
                        numerology_history.appendChild(para)    

                    });
                    numerology_history.style.display ="block";
                    document.getElementById('history-btn').innerText="Hide History"

                    let children = numerology_history.children;
                    // console.log(numerology_history)
                
                    for(let i=0; i<children.length; i++){
                        
                        // var child = children[i];
                        // console.log(child)
                        children[i].addEventListener('click',()=>{
                            
                            // console.log(name_data[i])
                            // console.log(date_data[i])
                        

                            localStorage.setItem('numerolgoy_name', name_data[i])
                            localStorage.setItem('numerology_date',date_data[i])
                            
                            window.location.assign("/numerology_prediction")
                        })
                    }
                }
            
            })
            .catch(function (error){
                console.log(error)
                alert("No Previous Predictions");
            })
        }
        
    })


    
    // function sendData() {
    //   const XHR = new XMLHttpRequest();
  
    //   // Bind the FormData object and the form element
    //   const FD = new FormData(form);
  
    //   // Define what happens on successful data submission
    //   XHR.addEventListener("load", (event) => {
    //     // alert(event.target.responseText);
    //     alert("Heading to Servers")
    //     window.location.assign("/testNumerology")
    //   });
  
    //   // Define what happens in case of error
    //   XHR.addEventListener("error", (event) => {
    //     alert("Oops! Something went wrong.");
    //   });
   
    //   // Set up our request
    //   XHR.open("POST", "testNumerology");
  
    //   // The data sent is what the user provided in the form
    //   XHR.send(FD);
    // }
  
    // Get the form element
  
    // Add 'submit' event handler
    // form.addEventListener("submit", (event) => {
    //   event.preventDefault();
  
    // //   sendData();
    // });
});
  







// form.addEventListener("submit", (Event)=>{
//     Event.preventDefault();

  
    // let name = document.getElementById("name");
    // let name_value = name.value;

    // let date = document.getElementById("date");
    // let date_value = date.value;

    // localStorage.setItem('numerolgoy_name', name_value)
    // localStorage.setItem('numerology_date',date_value)
    
    // window.location.assign("/numerology_prediction")

// })