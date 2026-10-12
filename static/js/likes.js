(function () {
  function getCookie(name) {
    const match = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
    return match ? decodeURIComponent(match[1]) : '';
  }

  document.addEventListener('submit', function (event) {
    const form = event.target;
    if (!(form instanceof HTMLFormElement) || !form.classList.contains('like-form')) {
      return;
    }

    event.preventDefault();

    const button = form.querySelector('.btn-like');
    if (!button || button.disabled) {
      return;
    }

    button.disabled = true;

    fetch(form.action, {
      method: 'POST',
      headers: {
        'X-Requested-With': 'XMLHttpRequest',
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: new FormData(form),
    })
      .then(function (response) {
        if (!response.ok) {
          throw new Error('Like failed');
        }
        return response.json();
      })
      .then(function (data) {
        const root = form.closest('.pet-card, .detail-info, .detail-layout') || form;
        root.querySelectorAll('[data-like-count]').forEach(function (el) {
          el.textContent = data.likes;
        });
        button.classList.toggle('is-liked', Boolean(data.liked));
        button.setAttribute('aria-pressed', data.liked ? 'true' : 'false');
        const label = button.querySelector('[data-like-label]');
        if (label) {
          label.textContent = data.liked ? 'Liked' : 'Like this pet';
        }
      })
      .catch(function () {
        form.submit();
      })
      .finally(function () {
        button.disabled = false;
      });
  });
})();
