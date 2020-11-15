var letters = [
   "A",
   "B",
   "C",
   "D",
   "E",
   "F",
   "G",
   "H",
   "I",
   "J",
   "K",
   "L",
   "M",
   "N",
   "O",
   "P",
   "Q",
   "R",
   "S",
   "T",
   "U",
   "V",
   "W",
   "X",
   "Y",
   "Z"
];
var option = document.getElementById("algorithm-option");
var inputField = document.getElementById("input");
var shiftInputDiv = document.getElementById("shift-input-div");
var shiftInputField = document.getElementById("shift-input");
var output = document.getElementById("output");
var encryptBtn = document.getElementById("encrypt-btn");
var decryptBtn = document.getElementById("decrypt-btn");

// Mozilla Reload Bug Fix
option.value = "caeser";

encryptBtn.addEventListener("click", () => {
   var data = inputField.value;
   if (option.value == "atbash") {
      if (!inputField.value.replace(/\s/g, "").length) {
         alert("Please Fill In The Required Fields");
      } else {
         crypt(data, applyAtbash);
      }
   } else if (option.value == "caeser") {
      if (
         !inputField.value.replace(/\s/g, "").length ||
         !shiftInputField.value.replace(/\s/g, "").length
      ) {
         alert("Please Fill In The Required Fields");
      } else {
         crypt(data, applyCaeserEncrypt);
      }
   } else {
      alert("*Please select an algorithm from the given options.");
   }
});

decryptBtn.addEventListener("click", () => {
   var data = inputField.value;
   if (option.value == "atbash") {
      if (!inputField.value.replace(/\s/g, "").length) {
         alert("Please Fill In The Required Fields");
      } else {
         crypt(data, applyAtbash);
      }
   } else if (option.value == "caeser") {
      if (
         !inputField.value.replace(/\s/g, "").length ||
         !shiftInputField.value.replace(/\s/g, "").length
      ) {
         alert("Please Fill In The Required Fields");
      } else {
         crypt(data, applyCaeserDecrypt);
      }
   } else {
      alert("*Please select an algorithm from the given options.");
   }
});

option.addEventListener("change", e => {
   var selectedOption = option.value;
   if (selectedOption === "caeser") {
      shiftInputDiv.style.display = "block";
   } else if (selectedOption === "atbash") {
      shiftInputDiv.style.display = "none";
   }
});

// Atbash Algorithm Method
function applyAtbash(data) {
   data = data.toUpperCase();
   data = data.split("");
   var newData = data
      .map(char => {
         if (char == " ") {
            return " ";
         } else {
            var index = letters.indexOf(char);
            var newIndex = Math.abs(index - 25);
            return letters[newIndex];
         }
      })
      .join("");
   return newData;
}

// Caeser Algorithm Encryption Method
function applyCaeserEncrypt(data) {
   data = data.toUpperCase();
   data = data.split("");
   var newData = data
      .map(char => {
         if (char == " ") {
            return " ";
         } else {
            var index = letters.indexOf(char);
            var newIndex =
               Math.abs(index + parseInt(shiftInputField.value)) % 26;
            return letters[newIndex];
         }
      })
      .join("");
   return newData;
}

// Caeser Algorithm Decryption Method
function applyCaeserDecrypt(data) {
   data = data.toUpperCase();
   data = data.split("");
   var newData = data
      .map(char => {
         if (char == " ") {
            return " ";
         } else {
            var index = letters.indexOf(char);
            var newIndex =
               Math.abs(index - parseInt(shiftInputField.value)) % 26;
            return letters[newIndex];
         }
      })
      .join("");
   return newData;
}

inputField.addEventListener("keypress", e => {
   var key = e.keyCode || e.charCode;
   if (
      (key >= 65 && key <= 90) ||
      (key >= 97 && key <= 122) ||
      key == 8 ||
      key == 32
   ) {
      return true;
   } else {
      alert("Data can only contain alpahbetical characters");
      e.preventDefault();
   }
});

shiftInputField.addEventListener("keypress", e => {
   var key = e.keyCode || e.charCode;
   if (key >= 48 && key <= 57) {
      return true;
   } else {
      alert("Shift Value is supposed to be number");
      e.preventDefault();
   }
});

inputField.addEventListener("input", () => {
   output.innerHTML = inputField.value;
});

function crypt(data, cb) {
   output.innerHTML = "";
   output.scrollIntoView();
   var result = cb(data).split("");
   var rate = 50;
   var time = data.length * rate;
   //			var temp = 0;
   var randomLetters = [];
   var key = setInterval(() => {
      for (var i = 0; i < data.length; i++) {
         randomLetters[i] = letters[Math.floor(Math.random() * Math.floor(26))];
      }

      output.innerHTML = "";

      randomLetters.forEach(letter => {
         output.innerHTML += letter;
      });

      //				var tempOutput = output.innerHTML.split('');
      //
      //				temp++;
      //
      //				for (var i = 0; i < temp; i++) {
      //					tempOutput[i] = result[i];
      //				}
      //
      //				output.innerHTML = tempOutput.join('');
      //
      //				console.log(temp);
   }, rate);

   setTimeout(() => {
      clearInterval(key);
      output.innerHTML = result.join("");
   }, time);
}