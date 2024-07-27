let input = document.querySelectorAll("input")

let timer=()=>{
    let date1 = "27 July 2025 03:54 PM"
    let newDate = new Date(date1)
    let todayDate = new Date()
    let finaldate = (newDate - todayDate)/1000
    
    if(finaldate<0) return;

    let day = Math.floor((finaldate/3600)/24)
    let hours = Math.floor((finaldate/3600)%24)
    let min = Math.floor((finaldate/60)%60)
    let sec = Math.floor((finaldate%60))
    
    input[0].value = day
    input[1].value = hours
    input[2].value = min
    input[3].value = sec
}

setInterval(() => {
    timer();
}, 1000);