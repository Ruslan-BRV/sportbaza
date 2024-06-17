window.addEventListener('scroll', function () {
    var headerNew = document.querySelector('.header-full');
    if (window.scrollY > 50) {
        headerNew.classList.add("scroll-header-full");
    } else {
        headerNew.classList.remove("scroll-header-full");
    }
});
(() => {
    const scrollBtn = document.querySelector('.scroll-btn');
    window.addEventListener('scroll', e => {
        window.scrollY >= 200 ? scrollBtn.style.display = "flex" : scrollBtn.style.display = "none"
    });
    scrollBtn.addEventListener('click', () => window.scrollTo(0,0))
})();