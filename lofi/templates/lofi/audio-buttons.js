window.addEventListener('keydown', function(e){
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    if(audio){
      audio.currentTime = 0;
      audio.play();
      const div = document.querySelector(`div[data-key="${e.keyCode}"]`);
      div.classList.add("playing");
    }
  });

window.addEventListener('keyup', function(e){
    const div = document.querySelector(`div[data-key="${e.keyCode}"]`);
    div.classList.remove("playing");
})