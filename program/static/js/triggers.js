document.getElementById("input_search").addEventListener("keyup", function(event){
    event.preventDefault();
    if(event.key === "Enter"){
        document.getElementById("button_search").click();
    }
});
