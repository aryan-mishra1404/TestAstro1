// language setting
var lang = document.getElementById('lang');
lang_value = lang.value;
console.log(lang_value)
localStorage.setItem('lang', lang_value)

lang.addEventListener('change',()=>{
    lang_value= lang.value;
    console.log("On change: "+ lang_value);
    localStorage.setItem('lang', lang_value)
})

function gotoNumerology(){
    window.location ="/numerology"
}

function gotoTarot(){
    window.location = "/tarot"
}
