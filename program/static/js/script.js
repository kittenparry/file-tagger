function get_files(tab){
    bed = document.getElementById("iframe_files").src = "/files/" + tab;
}
function check_this(c, i){
    if(i == 0){
        cbox = c.parentElement.firstElementChild;
    }else{
        cbox = c;
    }
    if(cbox.checked){
        cbox.checked = false;
        c.parentNode.style.backgroundColor = "#fff";
    }else{
        cbox.checked = true;
        c.parentNode.style.backgroundColor = "#337ab7";
    }
}
function sel_all(n) {
    document.innerHTML += n;
    for(i=0;i<n;i++){
        //document.getElementById("check" + i).checked = true;
        check_this(document.getElementById(("check" + i)), 1)
    } //this is flawed because it reverses the selection, not selects all
}
