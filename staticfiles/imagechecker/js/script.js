const uploadInput = document.getElementById('uploadInput');
  const uploadedImage = document.getElementById('uploadedImage');
  const closeButton = document.getElementById('closeButton');

  uploadInput.addEventListener('change', function() {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        uploadedImage.src = e.target.result;
        uploadedImage.style.display = 'block';
        closeButton.style.display = 'block';
      };
      reader.readAsDataURL(file);
    }
  });

  closeButton.addEventListener('click', function() {
    uploadedImage.src = '';
    uploadedImage.style.display = 'none';
    closeButton.style.display = 'none';
    uploadInput.value = ''; // Clear the selected file
  });