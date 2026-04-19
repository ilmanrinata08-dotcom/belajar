function checkIP() {
    const ip = document.getElementById("ip").value;
    const output = document.getElementById("result");
    
    if(!ip) {
        output.innerText = "> Masukkan IP, Man!";
        return;
    }

    output.innerText = "> Menganalisis...";

    setTimeout(() => {
        const octet = parseInt(ip.split('.')[0]);
        let kls = "Unknown";

        if(octet <= 126) kls = "Kelas A";
        else if(octet <= 191) kls = "Kelas B";
        else if(octet <= 223) kls = "Kelas C";

        output.innerHTML = `IP: ${ip}<br>Hasil: ${kls}<br>Status: OK`;
    }, 800);
}
console.log("C'oodiee JS Engine Started...");

