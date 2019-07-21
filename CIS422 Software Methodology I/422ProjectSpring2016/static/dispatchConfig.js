

function areyousure() {
  ion.sound.play("snap");
  var r = confirm("Are you sure you want to take this action?");
  if (r == true) {
    ion.sound.play("tap");
  } else {
    ion.sound.play("tap");
    return false;
  }
};

function errorCallback(error) {
  alert('ERROR(' + error.code + '): ' + error.message);
};

