function validar_formulario() {
    var username = document.formRegistro.username;
    var email = document.formRegistro.correo;
    var password = document.formRegistro.password;
    var username_len = username.value.length;
    if (username_len == 0 || username_len < 8) {
      alert("Debes ingresar un username con min. 8 caracteres");
      passid.focus();
      return false; //Para la parte dos, que los datos se conserven
    }
  
    var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    if (!email.value.match(formato_email)) {
      alert("Debes ingresar un email electronico valido!");
      email.focus();
      return false; //Para la parte dos, que los datos se conserven
    }
  
    var passid_len = password.value.length;
    if (passid_len == 0 || passid_len < 8) {
      alert("Debes ingresar una password con mas de 8 caracteres");
      passid.focus();
    }
  }
  
  function mostrarPassword(obj) {
    var obj = document.getElementById("password");
    obj.type = "text";
  }
  function ocultarPassword(obj) {
    var obj = document.getElementById("password");
    obj.type = "password";
  }

  function mostrarPassword2(obj) {
    var obj = document.getElementById("password2");
    obj.type = "text";
  }
  function ocultarPassword2(obj) {
    var obj = document.getElementById("password2");
    obj.type = "password";
  }
  
  function showForm() {
    document.getElementById("formRegistro").style.display = "block";
  }
  
  function hideForm() {
    document.getElementById("formRegistro").style.display = "none";
  }


  function buscarPor() {
    var buscar = document.formRegistro.busqueda-input;
    var buscar_len = buscar.value.length;
    if (buscar_len == 0 || buscar_len < 3) {
      alert("Debes ingresar una busqueda con min. 3 caracteres");
      passid.focus();
      return false; 
    }

    
  }


