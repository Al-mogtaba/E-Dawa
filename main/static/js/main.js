(function () {
    'use strict'
    const forms = document.querySelectorAll('.requires-validation')
    Array.from(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
    
          form.classList.add('was-validated')
        }, false)
      })
    })()


// var data = {
//     الخرطوم: [
//         'بحري',
//         'ام درمان',
//         'شرق النيل ',
//         'الخرطوم'],

// };
// var mdicine = {
//     شراب:[],
//     حبوب:[]

// };
// window.onload = function () {
//     var stateList = document.getElementById("stateList"),
//         cityList = document.getElementById("cityList");
//         typeList = document.getElementById("typeList");

//     for (var state in data) {
//         stateList.options[stateList.options.length] = new Option(state, state);
//     }
//     stateList.onchange = function () {
//         cityList.length = 1;
//         for (var city in data[this.value]) {
//             cityList.options[cityList.options.length] = new Option(data[this.value][city], data[this.value][city]);
//         }
//     };

//     for (var type in mdicine) {
//         typeList.options[typeList.options.length] = new Option(type, type);
//     }

// };