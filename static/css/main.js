var button = document.getElementById('btn');
var scre = document.getElementById('screen');

button.addEventListener('click', showScreen);
window.addEventListener('click', closeScreen);

function showScreen(){
  scre.style.display = 'flex';
  event.preventDefault();
}

function closeScreen(e){
  if (e.target == scre){
    scre.style.display= 'none';
  }
}
