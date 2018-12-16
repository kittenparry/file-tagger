function get_files(tab){
    bed = document.getElementById("iframe_files").src = "/files/" + tab;
}
function check_this(c){
    cbox = c.parentElement.firstElementChild;
    if(cbox.checked){
        cbox.checked = false;
        c.parentNode.style.backgroundColor = "#fff";
    }else{
        cbox.checked = true;
        c.parentNode.style.backgroundColor = "#337ab7";
    }
}
