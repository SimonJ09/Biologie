  // Récupérez le message de succès
  var successMessage = document.querySelector('.messages .success');

  // Récupérez le formulaire
  var infoForm = document.getElementById('info-form');

  // Vérifiez si le message de succès existe et masquez le formulaire si nécessaire
  if (successMessage) {
      infoForm.style.display = 'none';
  }