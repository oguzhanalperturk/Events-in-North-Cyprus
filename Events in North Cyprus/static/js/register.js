
const error_container = document.getElementById("error_container");


function validate(){

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let firstname = document.getElementById("firstname").value;
    let lastname = document.getElementById("lastname").value;
    let email = document.getElementById("email").value;

    let error_messages = []

    if(username == "" || password == "" || firstname == "" || lastname == "" || email == ""){
        error_messages.push("Please fill all the input boxes !!");
    }



    if(password.search(/[a-z]/) < 0) { 
        error_messages.push("Please use at least one lowercase character in password!");
    }

    if(password.search(/[A-Z]/) < 0) {  
        error_messages.push("Please use at least one uppercase character in password!");
    }

    if(password.search(/[0-9]/) < 0) {  
        error_messages.push("Please use at least one digit character in password!");
    }
    
    if (password.length < 8){
        error_messages.push("Password length should be at least eight!");
    }

    if(error_container.firstChild){
        error_container.removeChild(error_container.firstChild);
    }


    if(error_messages.length > 0){

        let inner_error_container = document.createElement("div");

        for(let i=0;i<error_messages.length;i++){

            let error_message_block = document.createElement("p");
            error_message_block.innerHTML = error_messages[i];
            inner_error_container.appendChild(error_message_block);
        }


        if(error_container.childNodes.length == 0){
            error_container.appendChild(inner_error_container)
        }
        

        return false;
    }
        

    return true;

}


/*
def passwordControl(password):
    response = []
    upper_count = 0
    lower_count = 0
    decimal_count = 0

    for i in password:
        if (i.isupper()):
            upper_count += 1
        elif (i.islower()):
            lower_count += 1
        elif (i.isdecimal()):
            decimal_count += 1

    if (upper_count < 1):
        response.append(
            "Please use at least one uppercase character in password!")
    if (lower_count < 1):
        response.append(
            "Please use at least one lowercase character in password!")
    if (decimal_count < 1):
        response.append("Please use at least one digit character in password!")
    if (len(password) < 8):
        response.append("Password length should be at least eight!")

    return response


    return true;
}

*/

