const link1 = document.getElementById("link1");
const link_container = document.getElementById("links");
const tables = document.querySelectorAll(".tables");
const table_titles = document.querySelectorAll(".table_titles");
const no_events_titles = document.querySelectorAll(".no_events_titles");


arrangeLinks();

function arrangeLinks(){
    if(document.getElementById("login_form_container") == null){
        link1.href = link1.href.replace("register_page","logout");
        link1.textContent = "Logout";

        const create_event_link = document.createElement("a");
        create_event_link.href = "/create_event_page";
        create_event_link.className = "link";
        create_event_link.innerHTML = "Create Event";
        link_container.appendChild(create_event_link);

        const display_event_link = document.createElement("a");
        display_event_link.href = "/display_events_page";
        display_event_link.className = "link";
        display_event_link.innerHTML = "Display Events";
        link_container.appendChild(display_event_link);
    }
}



for(let i=0;i<tables.length;i++){
    if(tables[i].rows.length == 1){
        tables[i].style.display = "none";
        no_events_titles[i].style.display = "block";
    }
    console.log(tables[i].rows.length);
}


