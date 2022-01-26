function openForm() {
    document.getElementsByClassName("myForm")[0].style.display = "block";
    document.getElementsByClassName("ajcl")[0].style.display = "none";
  }
function closeForm() {
    document.getElementsByClassName("myForm")[0].style.display = "none";
    document.getElementsByClassName("ajcl")[0].style.display = "block";
  }
  function openForm2() {
    document.getElementsByClassName("myForm2")[0].style.display = "block";
    document.getElementsByClassName("ajcl2")[0].style.display = "none";
  }
function closeForm2() {
    document.getElementsByClassName("myForm2")[0].style.display = "none";
    document.getElementsByClassName("ajcl2")[0].style.display = "block";
  }
function clear(){
    document.getElementById("id_full_name").value="";
    document.getElementById("id_num_tel").value="";//
    document.getElementById("id_lien_prof").value="";
    return true;
}
function add_select(id,name){
  return true;
}
function delete_select(id,name){
  alert(id+name)
}
// function azz(){
//     alert("kathe");
// }