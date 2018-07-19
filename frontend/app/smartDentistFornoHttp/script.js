/* variabili di sistema */
var serverUrl = "web:8000";
var updateStatusUrl = "http://" + serverUrl + "/manageDevice/";
var sendDataUrl = "http://" + serverUrl + "/gpsData/";
var checkStatusUrl = "http://" + serverUrl + "/devStatus/";

var id_dev = ""
var errorPres = false;
var on = false;
var timeout_var = null;
var timeout_succ = null;

function emptyError() {
  if(errorPres) {
    $("#errore").empty();
    $("#errore").hide();
  }
}

function showError(msg) {
  emptyError();
  if(timeout_succ != null) {
    $("#successo").empty();
    $("#successo").hide();
  }
  msg = "<p>" + msg + "</p>";
  $("#errore").append(msg);
  $("#errore").show();
  errorPres = true;
}

function showSuccess(msg) {
  if(timeout_succ != null) {
    $("#successo").empty();
  }
  msg = "<p>" + msg + "</p>";
  $("#successo").append(msg);
  $("#successo").show();
  timeout_succ = setTimeout(function () {
    $("#successo").empty();
    $("#successo").hide();
    timeout_succ = null;
  }, 5000);
}

function sendChangeStatus() {
  $.post(updateStatusUrl,
         {
           device_id : id_dev,
           operation : on ? "on" : "off"
         },
         function(data, status) {
            if (status != "success") {
              showError("Errore nell'invio dei dati - " + status);
            }
         });
}

function sendPosition(device_id, device_lat, device_long) {
  $.post(sendDataUrl,
         {
           id : device_id,
           lat : device_lat,
           long: device_long
         },
         function(data, status) {
            if (status != "success") {
              showError("Errore nell'invio dei dati - " + status);
            }
         });
}

function switchStatus() {
  on = !on;
  $("#accendi_spegni").val((on ? "Spegni" : "Accendi") + " il dispositvo");
  $("#lat, #long, #invia").prop("disabled", !on);
  $("#id").prop("disabled", on);
}

function updateStatus() {
  $.get(checkStatusUrl,
         function(data, status) {
            if (status != "success") {
              showError("Errore nell'invio dei dati - " + status);
            } else {
              var deviceList = data["devices"];
              for (var index in deviceList) {
                var device = deviceList[index];
                if(device.device_id == id_dev && device.status != on) {
                  switchStatus();
                  showSuccess("Il device è stato " + (on ? "acceso" : "spento") + " da remoto");
                }
              }
            }
         },
         "json");
}

$(document).ready(function() {
  $("#errore, #successo").hide();
  $("#lat, #long, #invia").prop("disabled", true);
  $("#accendi_spegni").click(function() {
    id_dev = $("#id").val();
    if(id_dev.length === 0 || id_dev.trim() === 0) {
      showError("<p>Inserisci un id valido, il campo non deve essere vuoto oppure solo spazi</p>");
    } else {
      emptyError();
      switchStatus();
      sendChangeStatus();
      showSuccess("Device " + (on ? "acceso" : "spento"));
      if(on) {
        timeout_var = setInterval(updateStatus, 15000);
      } else {
        clearTimeout(timeout_var);
      }
    }
  });
  $("#invia").click(function() {
    var lat = $("#lat").val();
    var long = $("#long").val();
    if(lat > 90 || lat < -90 || long > 180 || long < -180 || lat.length === 0 || long.length === 0) {
      showError("<p>I valori di latitudine e/o longitudine inseriti sono sbagliati, inserirli correttamente </p>");
    } else {
      emptyError();
      sendPosition(id_dev, lat, long);
    }
  });

});
