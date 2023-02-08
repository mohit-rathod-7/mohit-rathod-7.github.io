// --------------------------------------- Flash progress  --------------------------------------- 
window.onload = function(){
    flashes = []

    var flash = document.getElementsByClassName("flash");

    for (let i=0; i<flash.length; i++){
        flashes[i] = flash[i] 
    }
    
    for(let i = 0; i < flashes.length; i++){
        setTimeout(function(){
            var progress = flashes[i].getElementsByClassName("progress")[0];
            
            var width = 0;
            var id = setInterval(frame, 1);

            function frame(){
                if (width.toFixed(1) >= 100){
                    clearInterval(id);
                }
                else if (width < 99.9){
                    width = width + 0.175;
                    progress.style.width = width + "%";
                }
            }
        }, 500)

        $(".flash").css("opacity", 1)
    }
    
    var flash = gsap.timeline();
    var animationDuration = 0.5;

    flash
    .from('.flash', { ease: 'ease.in', duration: animationDuration, y: '-105%' })
    .to('.flash', { ease: 'ease.in', duration: animationDuration, y: '0%'})
    
    var flash_reverse = gsap.timeline();
    flash_reverse
    .from('.flash', { ease: 'ease.out', duration: animationDuration, y: '0%'})
    .to('.flash', { ease: 'ease.out', duration: animationDuration, y: '-105%' }).delay(4.5)

    
    setTimeout(function(){
        $(".flashes").remove();
    }, 6000)
}
