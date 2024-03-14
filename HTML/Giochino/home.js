document.addEventListener('contextmenu', event => event.preventDefault());


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





  document.getElementById('upgradeButton1').classList.add('disabled');
  document.getElementById("upgradeButton1").disabled = true;


  ham = 0;
});



var clickMultiplier = 100;
















function clickPig() {
  ham += clickMultiplier;
  updateHamCounter();

  var explosion = document.createElement("div");
  explosion.className = "explosion";
  explosion.style.left = event.clientX - 40 + "px";
  explosion.style.top = event.clientY - 40 + "px";

  var hamImg = document.createElement("img");
  hamImg.src = "ham.png";
  hamImg.className = "ham-img";
  explosion.appendChild(hamImg);

  var hamCounter = document.createElement("span");
  hamCounter.className = "ham-counter";
  hamCounter.textContent = "+" + clickMultiplier;
  explosion.appendChild(hamCounter);

  document.body.appendChild(explosion);

  setTimeout(function () {
    document.body.removeChild(explosion);
  }, 520); // Aumentato il tempo di visualizzazione a 1 secondo
}

function updateHamCounter() {
  var formattedHam;
  if (ham >= 1000) {
    formattedHam = numeral(ham).format('0,0.00a');
  } else {
    formattedHam = ham;
  }
  document.getElementById("hamCounter").innerHTML = formattedHam + " hams";
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


  console.log("Upgrade 1");

}







function onChangeHam(newValue) {
  var upg1 = document.getElementById('upgradeButton1').innerHTML;

  if (upg1 < ham) {
    document.getElementById('upgradeButton1').classList.remove('disabled');
    document.getElementById("upgradeButton1").disabled = false;
    upgrade1();
  } else {
    document.getElementById('upgradeButton1').classList.add('disabled');
    document.getElementById("upgradeButton1").disabled = true;
  }

}




