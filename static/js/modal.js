window.addEventListener('DOMContentLoaded',function(){
  document.getElementById('open').disabled = true;
  document.getElementById('id_review_communication').addEventListener('keyup',function(){
    if (this.value.length < 1) {
    document.getElementById('open').disabled = true;
    } else {
    document.getElementById('open').disabled = false;
    }
    },false);
  document.getElementById('id_review_communication').addEventListener('change',function(){
    if (this.value.length < 1) {
    document.getElementById('open').disabled = true;
    }
    },false);
},false);

'use strict';
{
  const open = document.getElementById('open');
  const close = document.getElementById('close');
  const modal = document.getElementById('modal');
  const mask = document.getElementById('mask');

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
