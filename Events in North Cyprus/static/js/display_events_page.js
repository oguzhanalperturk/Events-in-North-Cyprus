const table_elements = document.querySelectorAll(".table_elements");
const empty_table_message_container = document.getElementById("empty_table_message_container");
const table_container = document.getElementById("table_container");
const deactivate_buttons = document.querySelectorAll(".deactivate_link");
const activate_buttons = document.querySelectorAll(".activate_link");



for(let i=0;i<deactivate_buttons.length;i++){
    let dbutton = deactivate_buttons[i];
    if(dbutton.id.split(";")[1] == 0){
        deactivate_buttons[i].ariaDisabled = true;
    }
}

for(let i=0;i<activate_buttons.length;i++){
    let abutton = activate_buttons[i];
    if(abutton.id.split(";")[1] == 1){
        console.log("dsfsgf")
        activate_buttons[i].ariaDisabled = true;
    }
}


if(table_elements.length == 0){
    empty_table_message_container.style.display = "flex";
    table_container.style.display = "none";
}