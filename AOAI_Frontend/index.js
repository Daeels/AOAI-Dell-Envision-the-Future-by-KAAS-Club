let loader = document.getElementById("loader");
let templist;

document.getElementById("button").addEventListener("click", (event) => {
  event.preventDefault();
  transition("intro", "form1");
});

document.getElementById("stylish").addEventListener("click", (event) => {
  document.getElementById("stylish").style.filter =
    "drop-shadow(3px 3px 5px black)";
});

document.getElementById("button2").addEventListener("click", (event) => {
  event.preventDefault();
  let stylish = document.getElementById("stylish");
  if (stylish.value == "") {
    stylish.style.filter = "drop-shadow(5px 5px 10px red) ";
  } else {
    document.getElementById("button2").style.display = "none";
    document.getElementById("loader").style.display = "inline-block";
    let _data = {
      id: stylish.value,
    };
    fetch("http://20.82.80.40:3000/auth", {
      method: "POST",
      body: JSON.stringify(_data),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        if (data.validation == "ok") {
          document.getElementById("gm").innerHTML =
            "predicted academic success rate : " + data.gm + "%";
          document.getElementById("gi").innerHTML =
            "predicted academic success rate : " + data.gi + "%";
          document.getElementById("ge").innerHTML =
            "predicted academic success rate : " + data.ge + "%";
          transition("form1", "stats");
        } else {
          document.getElementById("loader").style.display = "none";
          document.getElementById("button2").style.display = "inline";
          stylish.style.filter = "drop-shadow(5px 5px 10px red)";
        }
      });
  }
});

let fillieres = ["gm", "gi", "ge"];

fillieres.forEach((element) => {
  document.getElementById("b" + element).addEventListener("click", (event) => {
    event.preventDefault();
    let temp = document.getElementById("b" + element);
    loader.style.display = "inline-block";
    document.getElementById("b" + element).replaceWith(loader);
    let _data = {
      id: stylish.value,
    };
    fetch("http://20.82.80.40:3000/" + element, {
      method: "POST",
      body: JSON.stringify(_data),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        // templist = data.list;
        if (data.validation == "ok") {
          console.log(parseInt(data.cf))
          let innerhtml = "predicted confidence : " + ("⭐".repeat(parseInt(data.cf))) + " <br/>" 
          innerhtml += "predicted insertion satisfaction : " + ("⭐".repeat(parseInt(data.is))) + " <br/>" 
          innerhtml += "predicted field insertion : " + ("⭐".repeat(parseInt(data.fi))) + " <br/>" 
          innerhtml += "predicted salary satisfaction : " + ("⭐".repeat(parseInt(data.s))) + " <br/>" 
          innerhtml += "predicted satisfaction towards work conditions : " + ("⭐".repeat(parseInt(data.cd))) + " <br/>" 

          document.getElementById(element + "-demo").innerHTML = innerhtml
          loader.replaceWith("");
          // for (let i = 0; i < data.l; i++) {
          //   addRow("pform", data.list[i], i);
          // }
          // transition("stats", "form2");
        } else {
          loader.replaceWith(temp);
        }
      });
  });
});

// document.getElementById("button8").addEventListener("click", (e) => {
//   e.preventDefault();
//   let choices = [];
//   for (let i = 0; i < templist.length; i++) {
//     let temp = "q" + i;
//     const rbs = document.querySelectorAll('input[name="' + temp + '"]');
//     for (const rb of rbs) {
//       if (rb.checked) {
//         selectedValue = rb.value;
//         break;
//       }
//     }
//     let obj = {};
//     obj[temp] = selectedValue;
//     choices.push(obj);
//   }
//   console.log(choices);
//   loader.style.display = "none";
//   document.getElementById("temp-demo").innerHTML =
//     "predicted professional insertion rate : 86% <button  style='border-radius: 30px;border : 0' class='waves-effect waves-light btn-xs priback sectext'> more info </button> <br/> predicted professional satisfaction : 46% <button  style='border-radius: 30px;border : 0' class='waves-effect waves-light btn-xs priback sectext'> more info </button> <br/> predicted chances of a successful carreer : 73% <button  style='border-radius: 30px;border : 0' class='waves-effect waves-light btn-xs priback sectext'> more info </button> <br/> personalised explanation and report TBD ";
//   transition("form2", "stats");
//   setTimeout(() => {
//     document.getElementById("pform").textContent = "";
//   }, 500);
// });

function transition(id1, id2) {
  document.getElementById(id2).classList.remove("fadeOutUp");
  document.getElementById(id1).classList.add("fadeOutUp");
  setTimeout(() => {
    document.getElementById(id1).style.display = "none";
    setTimeout(() => {
      document.getElementById(id2).style.display = "block";
    }, 500);
  }, 500);
}

M.AutoInit();
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".sidenav");
  var instances = M.Sidenav.init(elems);
  var elems = document.querySelectorAll(".collapsible");
  var instances = M.Collapsible.init(elems);
});

function addRow(parent, list, i) {
  const div = document.createElement("div");
  div.className = "col s12 m6";
  div.innerHTML =
    `<h4 class="sectext neon">${list.question}</h4>
  <form action="#">` +
    answers(i, list) +
    `</form>`;
  document.getElementById(parent).appendChild(div);
}

function answers(i, list) {
  let temp = ``;
  for (let j = 0; j < list.answer.length; j++) {
    temp += `<p>
    <label>
      <input
        value="${j}"
        class="with-gap"
        name="q${i}"
        type="radio"
      />
      <span class="sectext neon" style="font-size : 1.5em">${list.answer[j]}</span>
    </label>
  </p>`;
  }
  return temp;
}
