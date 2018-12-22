function get_files(tab){
    bed = document.getElementById("iframe_files").src = "/files/" + tab;
}
function check_this(c){
    cbox = c.parentElement.firstElementChild;
    if(cbox.checked){
        cbox.checked = false;
        change_colour(c, true);
    }else{
        cbox.checked = true;
        change_colour(c, false);
    }
}
function sel_all(n){
    //maybe it's related to the function's placement in the file?
    /*s = document.getElementById("span_selected");
    console.log(s);
    console.log(s.innerText);
    console.log(s.innerHTML);*/
    s = $('#span_selected');
    st = s.text();
    console.log(s);
    for(i=0;i<n;i++){
        //document.getElementById("check" + i).checked = true;
        //check_this(document.getElementById(("check" + i)), 1)
        if(s){
            console.log("if 0 also: " + s);
            document.getElementById("check" + i).checked = true;
            change_colour(c, false);
            s.text("1");
        }else{
            console.log("else: " + s);
            document.getElementById("check" + i).checked = false;
            change_colour(c, true);
            s.text("0");
        }
    } //this is flawed because it reverses the selection, not selects all
}
function change_colour(c, n){
    if(n){
        c.parentNode.style.backgroundColor = "#fff";
    }else{
        c.parentNode.style.backgroundColor = "#337ab7";
    }
}
function change_files(val){
    document.getElementById('iframe_files').src = "/files/[" + val + "]";
}
function get_tags(){
    n = document.getElementById('tag_len').value;
    sel_tags = new Array();
    for(x=0;x<n;x++){
        if(document.getElementById('tag_check' + x).checked){
            sel_tags.push(document.getElementById('tag_check' + x).value)
        }
    }
    change_files(sel_tags);
}
function get_search(){
    sel_tags = document.getElementById('input_search').value.split(" ");
    change_files(sel_tags);
}
