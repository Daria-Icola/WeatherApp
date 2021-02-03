$(document).ready(function(){
    alert("Welcome to Weather App")
    fetch(`http://localhost:8888/getData`)
    .then(res=> res.json()
        .then(data => {
            setData(data)
        })
    )

    
    function setData(data) {
        let html = `<div class="temp">${data.data[1]}&deg;C</div><div class="right"><div id="date">${data.data[0]}</div><div id="summary"></div>`
        let parentDOM = document.getElementsByClassName("details");
        parentDOM[0].innerHTML = html

    }
    
})