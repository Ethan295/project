






//document.addEventListener('contextmenu', event => event.preventDefault()); disabilita il tasto destro del mouse


//definisco ham
document.addEventListener('DOMContentLoaded', function () {


  Object.defineProperty(window, 'ham', {
    configurable: true, // Consenti la riconfigurazione della proprietà
    enumerable: true, // Rendi la proprietà enumerabile
    get: function () {
      return this._ham; // Utilizza this._ham per evitare conflitti con la funzione ham
    },
    set: function (newValue) {
      this._ham = newValue; // Imposta il valore di _ham
      onChangeHam(newValue); // Chiama la funzione onChangeHam quando il valore cambia
    }
  });


$("#upgradeButton1").css("background-color", "red");
$('#upgradeButton1').prop('disabled', true);



  ham = 0;
});



var clickMultiplier = 1;
var upg1Level = 0;
var upg1Price = 15;




function clickPig() {
  ham += clickMultiplier;
  updateHamCounter();

  var explosion = $("<div>").addClass("explosion")
                             .css({
                               left: event.clientX - 40 + "px",
                               top: event.clientY - 40 + "px"
                             });

  var hamImg = $("<img>").attr("src", "ham.png")
                         .addClass("ham-img");
  explosion.append(hamImg);

  var hamCounter = $("<span>").addClass("ham-counter")
                              .text("+" + clickMultiplier);
  explosion.append(hamCounter);

  $("body").append(explosion);

  setTimeout(function() {
    explosion.remove();
  }, 520); // Aumentato il tempo di visualizzazione a 1 secondo
}

function updateHamCounter() {
  var formattedHam;
  if (ham >= 1000) {
    formattedHam = numeral(ham).format('0,0.00a');
  } else {
    formattedHam = ham;
  }
  $("#hamCounter").html(formattedHam + " hams");
}



function updateClickMultiplier() {
  var formattedClickMultiplier;
  if (clickMultiplier >= 1000) {
    formattedClickMultiplier = numeral(clickMultiplier).format('0,0.00a');
  } else {
    formattedClickMultiplier = clickMultiplier;
  }
  $("#clickPowerDisplay").html("Click power: " + formattedClickMultiplier);
}




function getUser() {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "home.php?action=getUser", true); // Aggiorna l'azione per richiedere tutti gli utenti
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4 && xhr.status == 200) {
      var ids = xhr.responseText;

      var idArray = ids.split(',');
      console.log("Numero di ID:", idArray.length);
      for (var i = 0; i < idArray.length; i++) {
        console.log("ID:", idArray[i]);
      }
    }
  };
  xhr.send();
}



function fetchOtherDataFromDatabase() {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "home.php?action=getOtherData", true);
  xhr.onreadystatechange = function () {
    if (xhr.readyState == 4 && xhr.status == 200) {
      var otherData = xhr.responseText;
      console.log("Altri dati dal database:", otherData);
      // Ora puoi fare qualsiasi cosa con gli altri dati
    }
  };
  xhr.send();
}





function upgrade1() {
  upg1Level++;
  ham -= upg1Price;
  updateHamCounter();
  clickMultiplier += 1;
  updateClickMultiplier();
  upg1Price = Math.round(upg1Price * 1.5); // Aggiorna il prezzo dell'aggiornamento

  var valoreFormattato;
  if (upg1Price >= 1000) {
    valoreFormattato = numeral(upg1Price).format('0,0.00a');
  } else {
    valoreFormattato = upg1Price;
  }

  $("#upgradeButton1").html(valoreFormattato);
}











function onChangeHam(newValue) {

  if (upg1Price <= ham) {
    $("#upgradeButton1").css("background-color", "green").prop("disabled", false);
  } else {
    $("#upgradeButton1").css("background-color", "red").prop("disabled", true);
  }
}




