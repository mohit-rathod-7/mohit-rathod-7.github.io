var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    slidesPerView: "auto",
    
    grabCursor: true,
    centeredSlides: true,
    loop: true,

    coverflowEffect: {
        rotate: 45,
        stretch: 0,
        depth: 100,
        modifier: 1,
        slideShadows: true,
    },
    
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },

    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
    },
});