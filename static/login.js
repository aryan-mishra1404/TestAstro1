



// const form = document.getElementById('form');
// const name = document.getElementById('name');
const signupButton = document.getElementById('signup-button')
const signupInfo = document.getElementById('signup-info')
const signupBtn = document.getElementById('signup')
const loginBtn = document.getElementById('login')

function gotoSignUp(){
    document.getElementById("login-div").style.display="none";
    document.getElementById("signup-div").style.display="block";
    document.getElementById("other-buttons").style.display="none";
    document.getElementById("form-heading").innerText="Sign Up";
    signupBtn.style.display="inline-block";
    loginBtn.style.display = "none";
    signupInfo.style.display ="none";
    signupButton.style.textAlign = "center"
}


//   document.getElementById('box-heading').innerText ="SignUP";
//   document.querySelector('.name-box').style.display ="block";
//   login.style.display ="none";
//   signup.style.width="100%";
// })