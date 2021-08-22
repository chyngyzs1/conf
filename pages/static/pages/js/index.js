let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".sidebar");
// let searchBtn = document.querySelector(".bx-search");

btn.onclick = function () {
  sidebar.classList.toggle("active");
};
// searchBtn.onclick = function () {
//   sidebar.classList.toggle("active");
// };

// swiper slider js
var swiper = new Swiper(".mySwiper", {
  spaceBetween: 30,
  centeredSlides: true,
  autoplay: {
    delay: 5000,
    disableOnInteraction: false,
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  parallax: true,
  loop: true,
  loopFillGroupWithBlank: true,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

