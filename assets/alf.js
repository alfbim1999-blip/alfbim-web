/* ALF_BIM · comportamiento común: menú del celular y sección activa en la barra de producto */
(function () {
  var gh = document.getElementById('gh'), btn = document.getElementById('menuBtn');
  if (gh && btn) {
    btn.addEventListener('click', function () {
      var open = gh.classList.toggle('open');
      btn.setAttribute('aria-expanded', open);
    });
    gh.addEventListener('click', function (e) {
      if (e.target.closest('.gh-nav a')) { gh.classList.remove('open'); btn.setAttribute('aria-expanded', false); }
    });
  }
  var links = [].slice.call(document.querySelectorAll('.pbar nav a[href^="#"]'));
  if (links.length && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) links.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id); });
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    links.forEach(function (a) { var t = document.querySelector(a.getAttribute('href')); if (t) io.observe(t); });
  }
})();
