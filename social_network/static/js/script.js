var mainContent = document.querySelector('main');
if (mainContent.clientHeight < window.innerHeight) {
    document.querySelector('footer').style.display = 'flex';
} else {
    window.addEventListener('scroll', function () {
        var footer = document.querySelector('footer');
        var scrollHeight = document.documentElement.scrollHeight;
        var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
        var clientHeight = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight || 0;
        if (scrollHeight - (scrollTop + clientHeight) < 1) {
            footer.style.display = 'flex';
        } else {
            footer.style.display = 'none';
        }
    });
}