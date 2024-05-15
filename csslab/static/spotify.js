function functionname() {
the_heading = document.getElementById("hello");

heading_text = the_heading.innerText;

if (heading_text != "Hello World!"){
the_heading.innerText = "Hello World!"
}
else {
	the_heading.innerText = "Goodbye"
}}

the_paragraph = document.getElementById("paragraph1");

the_paragraph.onmouseenter = function() { 
	the_paragraph.style.color = "blue";
  the_paragraph.style.backgroundColor = "white";
};

function changeSpotify() {
  the_heading = document.getElementById("hello");
  text_input_element = document.getElementById("user-color");
  new_color = text_input_element.value;
	the_heading.style.color = new_color;
}

/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
