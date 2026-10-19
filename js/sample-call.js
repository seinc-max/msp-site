(function () {
  if (window.__tlSampleCall) return;
  window.__tlSampleCall = true;

  function clock(value) {
    var total = Math.max(0, Math.round(value || 0));
    var minutes = Math.floor(total / 60);
    var seconds = total % 60;
    return minutes + ':' + (seconds < 10 ? '0' : '') + seconds;
  }

  function init(root) {
    var audio = root.querySelector('audio');
    var button = root.querySelector('.tl-demo-play');
    var range = root.querySelector('.tl-demo-scrub input');
    var time = root.querySelector('.tl-demo-time');
    var lines = root.querySelectorAll('.tl-demo-lines li');
    var card = root.querySelector('.tl-demo-card');
    if (!audio || !button || !range) return;

    var fallback = parseFloat(range.getAttribute('max')) || 0;
    var payoff = card ? parseFloat(card.getAttribute('data-payoff')) : Infinity;
    var scrubbing = false;

    function duration() {
      var live = audio.duration;
      if (isFinite(live) && live > 0) return live;
      return fallback;
    }

    function paint() {
      var now = audio.currentTime || 0;
      var length = duration();
      if (time) time.textContent = clock(now) + ' / ' + clock(length);
      if (!scrubbing && document.activeElement !== range) {
        if (isFinite(length) && length > 0) range.max = String(length);
        range.value = String(Math.min(now, length));
      }
      var active = -1;
      for (var i = 0; i < lines.length; i++) {
        var start = parseFloat(lines[i].getAttribute('data-start'));
        var end = parseFloat(lines[i].getAttribute('data-end'));
        var on = now >= start && now < end;
        lines[i].classList.toggle('is-current', on);
        if (on) {
          lines[i].setAttribute('aria-current', 'true');
          active = i;
        } else {
          lines[i].removeAttribute('aria-current');
        }
      }
      if (active < 0 && lines.length && now >= parseFloat(lines[lines.length - 1].getAttribute('data-end'))) {
        lines[lines.length - 1].classList.add('is-current');
        lines[lines.length - 1].setAttribute('aria-current', 'true');
      }
      if (card) card.classList.toggle('is-revealed', now >= payoff);
      var playing = !audio.paused && !audio.ended && !audio.error;
      button.classList.toggle('is-playing', playing);
      button.setAttribute('aria-label', playing ? 'Pause sample call' : 'Play sample call');
      range.setAttribute('aria-valuetext', clock(now) + ' of ' + clock(length));
    }

    button.addEventListener('click', function () {
      var playing = !audio.paused && !audio.ended && !audio.error;
      if (playing) {
        audio.pause();
        return;
      }
      var pending = audio.play();
      if (pending && pending.catch) pending.catch(function () { paint(); });
    });

    range.addEventListener('pointerdown', function () { scrubbing = true; });
    range.addEventListener('pointerup', function () { scrubbing = false; paint(); });
    range.addEventListener('pointercancel', function () { scrubbing = false; paint(); });
    range.addEventListener('input', function () {
      var next = parseFloat(range.value);
      if (!isNaN(next)) {
        try { audio.currentTime = next; } catch (err) {}
      }
      paint();
    });
    range.addEventListener('change', function () { scrubbing = false; paint(); });

    audio.addEventListener('play', paint);
    audio.addEventListener('pause', paint);
    audio.addEventListener('timeupdate', paint);
    audio.addEventListener('ended', paint);
    audio.addEventListener('error', paint);
    audio.addEventListener('loadedmetadata', paint);
    audio.addEventListener('durationchange', paint);
    paint();
  }

  var players = document.querySelectorAll('.tl-demo');
  for (var n = 0; n < players.length; n++) init(players[n]);
})();
