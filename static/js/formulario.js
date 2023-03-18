
//Importando inputs y formulario
const form = document.getElementById('form');
const inputs = document.querySelectorAll('#form input');

const expresion = {
    name: /^[a-zA-ZÁ-ÿñÑ]{4,16}$/,
    email: /^[\w.-]+@[a-zA-Z_-]+?(?:\.[a-zA-Z]{2,6})+$/,
    user: /^[a-zA-Z0-9_-]{4,16}$/,
    password: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,18}$/
};

//Estado final de los campos
const fields = {
    name: false,
    last_name: false,
    second_last_name: false,
    birthday: false,
    email: false,
    user: false,
    password: false,
    password2: false
};

//Recorrer validaciones
const formValidate = (e) => {
    switch (e.target.id) {
        case 'name':
            validateCamp(expresion.name, e.target, 'name');
            break;
        case 'last_name':
            validateCamp(expresion.name, e.target, 'last_name');
            break;
        case 'second_last_name':
            validateCamp(expresion.name, e.target, 'second_last_name');
            break;
        case 'birthday':
            validateAge(e.target.value)
            break;
        case 'email':
            validateCamp(expresion.email, e.target, 'email');
            break;
        case 'address':
            break;
        case 'user':
            validateCamp(expresion.user, e.target, 'user');
            break;
        case 'password':
            validateCamp(expresion.password, e.target, 'password');
            validatePassword2();
            break;
        case 'password2':
            validatePassword2();
            break;
    }
};

//Validacion por Regex
const validateCamp = (expresion, input, field) => {
    if (expresion.test(input.value)) {
        document.getElementById(`group-${field}`).classList.add(`input-group-correct`);
        document.getElementById(`group-${field}`).classList.remove(`input-group-incorrect`);
        document.querySelector(`#group-${field} .form-control-error`).classList.remove(`form-control-error-active`)
        fields[field] = true;
    } else {
        document.getElementById(`group-${field}`).classList.add(`input-group-incorrect`);
        document.getElementById(`group-${field}`).classList.remove(`input-group-correct`);
        document.querySelector(`#group-${field}  .form-control-error`).classList.add(`form-control-error-active`)
        fields[field] = false;
    }
};

//Validacion de Edad
const validateAge = (dateBirthday) => {
    //Fecha actual
    const dateToday = new Date();
    const yearToday = parseInt(dateToday.getFullYear());
    const monthToday = parseInt(dateToday.getMonth);
    const dayToday = parseInt(dateToday.getDay);
    //formato de entrada  YYYY-MM-DD
    const yearBirthday = parseInt(String(dateBirthday).substring(0, 4));
    const monthBirthday = parseInt(String(dateBirthday).substring(5, 7));
    const dayBirthday = parseInt(String(dateBirthday).substring(8, 10));
    //Calculando edad de fecha ingresada
    let age = yearToday - yearBirthday;
    if (monthToday < monthBirthday) {
        age--;
    } else if (monthToday == monthBirthday) {
        if (dayToday < dayBirthday) {
            age--;
        }
    }
    age = Number(age)
    //Validando edad
    if (age > 13 && age <= 120) {
        document.getElementById(`group-birthday`).classList.add(`input-group-correct`);
        document.getElementById(`group-birthday`).classList.remove(`input-group-incorrect`);
        document.querySelector(`#group-birthday .form-control-error`).classList.remove(`form-control-error-active`);
        fields['birthday'] = true;
    } else {
        document.getElementById(`group-birthday`).classList.add(`input-group-incorrect`);
        document.getElementById(`group-birthday`).classList.remove(`input-group-correct`);
        document.querySelector(`#group-birthday  .form-control-error`).classList.add(`form-control-error-active`);
        fields['birthday'] = false;
    }
};
//Validacion de segunda contraseña
const validatePassword2 = () => {
    const inputPassword1 = document.getElementById('password').value;
    const inputPassword2 = document.getElementById('password2').value;
    if (inputPassword1 !== inputPassword2) {
        document.getElementById(`group-password2`).classList.add(`input-group-incorrect`);
        document.getElementById(`group-password2`).classList.remove(`input-group-correct`);
        document.querySelector(`#group-password2  .form-control-error`).classList.add(`form-control-error-active`);
        fields['password2'] = false;
    } else {
        document.getElementById(`group-password2`).classList.add(`input-group-correct`);
        document.getElementById(`group-password2`).classList.remove(`input-group-incorrect`);
        document.querySelector(`#group-password2 .form-control-error`).classList.remove(`form-control-error-active`);
        fields['password2'] = true;
    }
};

//Seleccion de campo
inputs.forEach((input) => {
    input.addEventListener('keyup', formValidate);
    input.addEventListener('blur', formValidate);
});

//Enviar formulario si todos los campos estan correctos
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const termsStatus = document.getElementById('terms_conditions').checked;
    if (fields.user && fields.last_name && fields.second_last_name && fields.birthday && fields.email && fields.user && fields.password && fields.password2 && termsStatus) {
        resetForm();
        form.reset();
        alert('Formulario enviado correctamente');
    }
});

const resetForm = () => {
    //Limpiar campos internos
    form.reset();
    //Limpiar borde verde de correcto
    document.getElementById(`group-name`).classList.remove(`input-group-correct`);
    document.getElementById(`group-last_name`).classList.remove(`input-group-correct`);
    document.getElementById(`group-second_last_name`).classList.remove(`input-group-correct`);
    document.getElementById(`group-birthday`).classList.remove(`input-group-correct`);
    document.getElementById(`group-email`).classList.remove(`input-group-correct`);
    document.getElementById(`group-user`).classList.remove(`input-group-correct`);
    document.getElementById(`group-password`).classList.remove(`input-group-correct`);
    document.getElementById(`group-password2`).classList.remove(`input-group-correct`);
    //Limpiar borde rojo de incorrecto
    document.getElementById(`group-name`).classList.remove(`input-group-incorrect`);
    document.getElementById(`group-last_name`).classList.remove(`input-group-incorrect`);
    document.getElementById(`group-second_last_name`).classList.remove(`input-group-incorrect`);
    document.getElementById(`group-birthday`).classList.remove(`input-group-incorrect`);
    document.getElementById(`group-email`).classList.remove(`input-group-incorrect`);
    document.getElementById(`group-user`).classList.remove(`input-group-incorrect`);
    document.getElementById(`group-password`).classList.remove(`input-group-incorrect`);
    document.getElementById(`group-password2`).classList.remove(`input-group-incorrect`);
    //Limpiar mensaje error de campo
    document.querySelector(`#group-name  .form-control-error`).classList.remove(`form-control-error-active`);
    document.querySelector(`#group-last_name  .form-control-error`).classList.remove(`form-control-error-active`);
    document.querySelector(`#group-second_last_name  .form-control-error`).classList.remove(`form-control-error-active`);
    document.querySelector(`#group-birthday  .form-control-error`).classList.remove(`form-control-error-active`);
    document.querySelector(`#group-email  .form-control-error`).classList.remove(`form-control-error-active`);
    document.querySelector(`#group-user  .form-control-error`).classList.remove(`form-control-error-active`);
    document.querySelector(`#group-password  .form-control-error`).classList.remove(`form-control-error-active`);
    document.querySelector(`#group-password2  .form-control-error`).classList.remove(`form-control-error-active`);
};

//Funcion para resetear formulario
form.addEventListener('reset', () =>{
    resetForm();
});










