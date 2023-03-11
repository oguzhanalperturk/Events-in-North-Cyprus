
const create_event_button = document.getElementById("create_event_button");
const date_time_block = document.getElementById("date_time");
const error_container = document.getElementById("error_container");


adjustDateInput();



function adjustDateInput(){
    let today = new Date();
    let today_str = ""

    month = 1 + parseInt(today.getMonth());
    month = month.toString();
    hours = today.getHours().toString();
    minutes = today.getMinutes().toString();
    day = today.getDate().toString();

    if(hours.length == 1){
        hours = "0" + hours;
    }

    if(minutes.length == 1){
        minutes = "0" + minutes;
    }

    if(day.length == 1){
        day = "0" + day;
    }

    if(month.length == 1){
        month = "0" + month;
    }


    today_str = today.getFullYear() + "-" + month + "-" + day  + "T" + hours + ":" + minutes;


    date_time_block.min = today_str;

}



function validate(){

    let event_name = document.getElementById("event_name").value;
    let description = document.getElementById("description").value;
    let location = document.getElementById("location").value;
    let city = document.getElementById("cities");
    city = city.options[city.selectedIndex].text;
    let ticket_price = document.getElementById("ticket_price").value;
    let date_time = date_time_block.value;

 
    let error_messages = [];


    if(event_name == "" || description == "" || location == "" || city == "" || ticket_price == "" || date_time == ""){

        error_messages.push("Please fill all the input boxes !!");

    }
   
    if(isNaN(ticket_price)){

        error_messages.push("Please enter a integer or float value for ticket price value !!");

    }

    if(ticket_price < 0){

        error_messages.push("Please enter a positive value for ticket price value !!");

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



