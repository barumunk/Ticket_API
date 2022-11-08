var formulario = document.getElementById('formulario');
var datas      = document.querySelectorAll('#formulario input');

//expresiones regulares
const expresiones = {
	curp:     /^[a-zA-Z0-9\_\-]{18,18}$/, // Letras, numeros, guion y guion_bajo
	nombre:   /^[a-zA-ZÀ-ÿ\s]{3,40}$/,   // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/,               // 4 a 12 digitos.
	correo:   /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/               // 7 a 14 numeros.
}


// campos para vaidar si van vacios
const datoCampo = {
    f_namecom: [false,''],
    f_curp:    [false,''],
    f_name:    [false,''],
    f_pate:    [false,''],
    f_mate:    [false,''],
    f_tele:    [false,''],
    f_celu:    [false,''],
    f_corr:    [false,'']
}


// obtener el nombre del campo y mandar a validar con la expreciones
// para colocar verde o rojo el campo si va correcto
const validacionCase = (e) =>{
    switch(e.target.name){
        //Nombre Completo
        case "f_namecom":
            validar(expresiones.nombre,e.target);
        break;
        //CURP
        case "f_curp":
            validar(expresiones.curp,e.target);
        break;
        //Nombre
        case "f_name":
            validar(expresiones.nombre,e.target);
        break;
        //Paterno
        case "f_pate":
            validar(expresiones.nombre,e.target);
        break;
        //Materno
        case "f_mate":
            validar(expresiones.nombre,e.target);
        break;
        //Telefono
        case "f_tele":
            validar(expresiones.telefono,e.target);
        break;
        //Celular
        case "f_celu":
            validar(expresiones.telefono,e.target);
        break;
        //Correo
        case "f_corr":
            validar(expresiones.correo,e.target);
        break;
    }
}


// validar el campo y colocar el color verde o rojo si es corecto o no
// y asignar al objeto en su correspondiente campo un true o false
// si el campo es correcto
const validar = (expresiones,target) => {
    if(expresiones.test(target.value)){
        target.style.backgroundColor = "#48F01B";
        datoCampo[target.name][0]    = true;
        datoCampo[target.name][1]    = target.value;
    }
    else if(target.value === ""){
        target.style.backgroundColor = "white";
        datoCampo[target.name][0]    = false;
    }
    else{
        target.style.backgroundColor = "#F85146";
        datoCampo[target.name][0]    = false;
    }
}


// recorre las validaciones
datas.forEach((input)=>{
    input.addEventListener('keyup',validacionCase);
    input.addEventListener('blur',validacionCase);
});


//detectar vocal o consonante
var consonante = (texto) =>{
    var text = "";
    for(var i = 0; i < texto.length; i++){
        if(i != 0 ){
            if(texto[i] != "a" || texto[i] != "e" || texto[i] != "i"
            || texto[i] != "o" || texto[i] != "u"){
                text = texto[i];
                break;
            }
        }
    }
    return text;
}
//validar curp
var validarcurp = (datoCampo) =>{
    var charpaterno1 = datoCampo.f_pate[1].substr(0,1);// primer caracter paterno
    var charpaterno2 = datoCampo.f_pate[1].substr(2,1);// tercer caracter paterno
    var charmaterno  = datoCampo.f_mate[1].substr(0,1);// primer caracter materno
    var charnombre   = datoCampo.f_name[1].substr(0,1);// primer caracter nombre
    var charfecha    = datoCampo.f_curp[1].substr(4,6);// fecha que viene en la curp
    var charsexo     = datoCampo.f_curp[1].substr(10,1);// sexo que viene en la curp
    var charentidadf = datoCampo.f_curp[1].substr(11,2);// entidad federativa
    var conspaterno  = consonante(datoCampo.f_pate[1]);// primer consonante interno de paterno
    var consmaterno  = consonante(datoCampo.f_mate[1]);// primer consonante interno de materno
    var consnombre   = consonante(datoCampo.f_name[1]);// primer consonante interno de nombre
    var homoclave    = datoCampo.f_curp[1].substr(16,1);// clave homoclave
    var verificador  = datoCampo.f_curp[1].substr(17,1);// verificador

    if(isNaN(charpaterno1)  && isNaN(charpaterno2) && isNaN(charmaterno)  && isNaN(charnombre)
      && !isNaN(charfecha)  && isNaN(charsexo)     && isNaN(charentidadf) && isNaN(conspaterno)
      && isNaN(consmaterno) && isNaN(consnombre)   && !isNaN(homoclave)   && !isNaN(verificador)){
        return true;
    }
    else{
        return false;
    }
}


function calcularAños(dia, mes, año) {
    var today = new Date();
    if(año >= '00' && año <= today.getFullYear().toString().substr(2,2)){
        año = '20'+ año
    }
    else{
        año = '19'+ año
    }
    //Restamos los años
    años = today.getFullYear() - año;
    // Si no ha llegado su cumpleaños le restamos el año por cumplir (Los meses en Date empiezan en 0, por eso tenemos que sumar 1)
    /*if (mes > (today.getMonth() + 1) || dia > today.getDay())
        años--;*/
    return años;
}


// alertas
var alerta = (fondo,fondo1,texto,llaves) => {
    formulario.reset();
    // generar mensaje toast
    var toasts  = document.getElementById('toasts');
    var toast   = document.getElementById('toast');

    for(var i = 0; i < llaves.length; i++){
        document.getElementById(llaves[i]).style.backgroundColor = "white";
    }
    toasts.style.backgroundColor = fondo;
    toast.style.backgroundColor  = fondo1;
    toast.innerHTML              = texto;
    toast.style.color            = "white";
    toasts.style.display = "block";
    toast.style.display = "block";
    
    setTimeout(()=>{
        toasts.style.display = "none";
        toast.style.display = "none"
        toast.innerHTML = "";
    },3000);
}


var methodPost = (datos) => {
    fetch('php/register.php',{
        method: 'POST',
        body: datos
    }).then(res => res.json())
      .then(data => {
        console.log(data);
      });
}


var formu = document.getElementById('formulario');
// botón del evento
formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    var datos = new FormData(formu);
    // los select nos ayudara a modificar el estilo
    var select1 = document.getElementById('f_info_select1').value;
    var select2 = document.getElementById('f_info_select2').value;
    var select3 = document.getElementById('f_info_select3').value;
    var llaves  = Object.keys(datoCampo);// traer los nombres de llaves
    // variables para calcular edad
    var ano     = datoCampo.f_curp[1].substr(4,2);
    var mes     = datoCampo.f_curp[1].substr(6,2);
    var dia     = datoCampo.f_curp[1].substr(8,2);
    var edad    = calcularAños(dia,mes,ano);
    // valida si el campo NO viene vacío
    if(datoCampo.f_namecom[0] && datoCampo.f_curp[0] && datoCampo.f_name[0] && datoCampo.f_pate[0] 
       && datoCampo.f_mate[0] && datoCampo.f_tele[0] && datoCampo.f_celu[0] && datoCampo.f_corr[0] 
       && select1 != '' && select2 != '' && select3 != ''){

        for(var i = 0; i < llaves.length; i++){
            document.getElementById(llaves[i]).style.backgroundColor = "white";
        }

        // valida si el campo CURP cumple el patrón como esta conformado
        if(validarcurp(datoCampo)){
            if(edad >= 15 && edad <= 18 && select1 === "secundaria"){
                alerta('green','#48F01B','Formulario Completado',llaves);
                /*fetch('php/register.php',{
                    method: 'POST',
                    body: datos
                }).then(res => res.json())
                  .then(data => {
                    console.log(data);
                  });*/
                  window.location='http://localhost:5000/user/ticket/registro';
            }
            else if(edad >= 18 && edad <= 20 && select1 === "preparatoria"){
                alerta('green','#48F01B','Formulario Completado',llaves);
                /*fetch('php/register.php',{
                    method: 'POST',
                    body: datos
                }).then(res => res.json())
                  .then(data => {
                    console.log(data);
                  });*/
                  window.location='http://localhost:5000/user/ticket/registro';
            }
            else if(edad >= 20 && edad <= 60 && select1 === "universidad"){
                alerta('green','#48F01B','Formulario Completado',llaves);
                /*fetch('../php/register.php',{
                    method: 'POST',
                    body: datos
                }).then(res => res.json())
                  .then(data => {
                    console.log(data);
                  });*/
                  window.location='http://localhost:5000/user/ticket/registro';
            }
            else{
                alerta('red','#F85146','NO se podrá agendar cita por el sistema en línea, acudir a las oficinas correspondiente',llaves);
            } // cova970112hclrln02
        }
        // valida si el campo CURP NO cumple el patrón como esta conformado
        else{
            alerta('yellow','#ABAD11','Verificar la CURP',llaves);
        }
    }

    // valida si el campo viene vacío
    else{
        alerta('red','#F85146','Formulario Incompleto',llaves);
    }
});




