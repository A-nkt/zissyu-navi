function Event1() {
  if (this.value.length < 1) {
    document.getElementById('open').disabled = true;
    }
  else {
    document.getElementById('open').disabled = false;
    }
}

function Event2() {
  if (this.value.length < 1) {
    document.getElementById('open').disabled = true;
  }
}

function Event_par() {
  document.getElementById('open').disabled = true;
  document.getElementById('id_review_communication').addEventListener('keyup',Event1,false);
  document.getElementById('id_review_communication').addEventListener('change',Event2,false);
}

window.addEventListener('DOMContentLoaded',Event_par,false);



'use strict';
{
  const open = document.getElementById('open');
  const close = document.getElementById('close');
  const modal = document.getElementById('modal');
  const mask = document.getElementById('mask');
  const params = document.getElementById('submited');
  if (params != NaN) {
    open.addEventListener('click', function () {
      modal.classList.remove('hidden');
      mask.classList.remove('hidden');
    });
    close.addEventListener('click', function () {
      modal.classList.add('hidden');
      mask.classList.add('hidden');
    });
    mask.addEventListener('click', function () {
      modal.classList.add('hidden');
      mask.classList.add('hidden');
    });
  }
}
