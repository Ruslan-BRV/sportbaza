window.addEventListener('scroll', function () {
    var headerNew = document.querySelector('.header-full');
    if (window.scrollY > 50) {
        headerNew.classList.add("scroll-header-full");
    } else {
        headerNew.classList.remove("scroll-header-full");
    }
});