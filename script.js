const output = document.getElementById('output');

function runScan() {
    const steps = [
        "[INFO] Initiating network scan...",
        "[INFO] Target: 192.168.1.100",
        "[WAIT] Checking open ports...",
        "[OK] Port 80 (HTTP) is OPEN",
        "[OK] Port 443 (HTTPS) is OPEN",
        "[OK] Port 22 (SSH) is OPEN",
        "[DONE] Scan completed successfully.",
        "System secure. Admin: C'oodiee"
    ];

    output.innerHTML = "";
    let i = 0;

    function nextLine() {
        if (i < steps.length) {
            const line = document.createElement('div');
            line.textContent = steps[i];
            output.appendChild(line);
            output.scrollTop = output.scrollHeight;
            i++;
            setTimeout(nextLine, 700);
        }
    }
    nextLine();
}

console.log("Network Script Engine V2.0 Ready");

