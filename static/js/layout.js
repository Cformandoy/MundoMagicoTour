"use strict";

$(document).ready(function(){

    $('.input-daterange').datepicker({
        
        format: 'dd-mm-yyyy',
        autoclose: true,
        calendarWeeks : false,
        clearBtn: true,
        disableTouchKeyboard: true,
        lenguaje: 'es',
        weekStart: 1
    });
    
    });

eel.expose(cleanData)
function cleanData(){
    location.reload();
}

eel.expose(cargando_tittle)
function cargando_tittle(JSONCargando) {
    if (JSONCargando.status == 0) {
        // $('#loading-modal-message').html(JSONCargando.porcentaje + '%');
        
    }
    if (JSONCargando.status == 1) {
        // Se cierra el modal loading
        document.getElementById('ButtonCloseLoading').click()
        document.getElementById('ButtonOpenMsg').click()
    }
}

eel.expose(alerta_modal)
function alerta_modal(JSONCargando) {
    if (JSONCargando.status == 0) {
        // $('#loading-modal-message').html(JSONCargando.porcentaje + '%');
    }
    if (JSONCargando.status == 1) {
        // Se cierra el modal loading
        document.getElementById('ButtonCloseLoading').click()
        document.getElementById('ButtonOpenAlerta').click()
    }
}

function enableButtonPrecios() {
    document.getElementById('btn-proceso-precio').disabled = true

    if  (document.getElementById('listGroupCheckableRadios7').checked == true &&(
                document.getElementById('listGroupCheckableRadios1').checked == true 
            || document.getElementById('listGroupCheckableRadios2').checked == true 
            || document.getElementById('listGroupCheckableRadios3').checked == true 
            || document.getElementById('listGroupCheckableRadios4').checked == true
            || document.getElementById('listGroupCheckableRadios5').checked == true 
            || document.getElementById('listGroupCheckableRadios6').checked == true)){
        document.getElementById('btn-proceso-precio').disabled = true

    }else if (document.getElementById('listGroupCheckableRadios7').checked == true){
        document.getElementById('btn-proceso-precio').disabled = false
        console.log('enabled')
    }else if  (document.getElementById('listGroupCheckableRadios1').checked == true 
            || document.getElementById('listGroupCheckableRadios2').checked == true 
            || document.getElementById('listGroupCheckableRadios3').checked == true 
            || document.getElementById('listGroupCheckableRadios4').checked == true
            || document.getElementById('listGroupCheckableRadios5').checked == true 
            || document.getElementById('listGroupCheckableRadios6').checked == true){
        document.getElementById('btn-proceso-precio').disabled = false
        console.log('enabled')
    }
}

function ButtonOne() {
    //debugger
    var cb1 = document.getElementById('listGroupCheckableRadios1').checked
    var cb2 = document.getElementById('listGroupCheckableRadios2').checked
    var cb3 = document.getElementById('listGroupCheckableRadios3').checked
    var cb4 = document.getElementById('listGroupCheckableRadios4').checked
    var cb5 = document.getElementById('listGroupCheckableRadios5').checked
    var cb6 = document.getElementById('listGroupCheckableRadios6').checked
    var cb7 = document.getElementById('listGroupCheckableRadios7').checked
    
    eel.opciones(cb1, cb2, cb3, cb4, cb5, cb6, cb7);
}

function ButtonSignIn() { 
    var user = document.getElementById('floatingInput').value
    var pass = document.getElementById('floatingPassword').value
    var usuarioCorrecto = false
    // usuarios
    const usuarios = [
        ['ignacio.soto', 'ignacio', 'Ignacio Soto'],
        ['natacha.soto', 'natacha', 'Natacha Soto'],
        ['scarlett.soto', 'scarlett', 'Scarlett Soto'],
        ['amador.soto', 'amador', 'Amador Soto'],
        ['leonardo.maulen', 'leonardo', 'Leonardo Maulen'],
        ['cristopher.pozas','cristopher', 'Cristopher Pozas']
    ]

    for (let i = 0; i < usuarios.length; i++) {
        const userSelect = usuarios[i];
        if ((userSelect[0] == user) && (userSelect[1] == pass)){
            usuarioCorrecto = true
            break
        }
    }
    
    if (usuarioCorrecto == true){
        document.location.href = 'index-finanzas', true;
    }else{
        document.getElementById('ButtonLoginError').click()
    }
    
}

// function ButtonAddIngreso(){
//     var tipo_i = document.getElementById('tipo_ingreso').value
//     var detalle_i = document.getElementById('detalle_ingreso').value
//     var metodo_i = document.getElementById('metodo_ingreso').value
//     var fecha_i = document.getElementById('fecha_ingreso').value
//     var monto_i = document.getElementById('monto_ingreso').value
    
//     eel.addIngreso(tipo_i,detalle_i,metodo_i,fecha_i,monto_i);
//     document.getElementById('ButtonOpenMsg').click()
// }

// function ButtonAddGasto(){
//     var tipo = document.getElementById('tipo_gasto').value
//     var detalle = document.getElementById('detalle_gasto').value
//     var metodo = document.getElementById('metodo_gasto').value
//     var fecha = document.getElementById('fecha_gasto').value
//     var monto = document.getElementById('monto_gasto').value

//     eel.addGasto(tipo,detalle,metodo,fecha,monto);
//     document.getElementById('ButtonOpenMsg').click()
// }


function ButtonReporteCuentas(){
    eel.reporteCuentas();
}


Frames.init("pk_sbox_XXXX");



//  slider



