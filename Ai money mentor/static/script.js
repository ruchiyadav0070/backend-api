async function analyze() {
    let income = document.getElementById("income").value;
    let expenses = document.getElementById("expenses").value;
    let age = document.getElementById("age").value;

    let res = await fetch("/analyze", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({income, expenses, age})
    });

    let data = await res.json();

    let chat = document.getElementById("chatbox");

    chat.innerHTML += `<p>💰 Savings: ₹${data.savings}</p>`;
    chat.innerHTML += `<p>📈 SIP: ₹${data.sip}</p>`;
    chat.innerHTML += `<p>🛡️ Emergency Fund: ₹${data.emergency}</p>`;
    chat.innerHTML += `<p>🤖 Advice: ${data.advice.join("<br>")}</p>`;

    new Chart(document.getElementById("chart"), {
        type: "pie",
        data: {
            labels: ["Expenses", "Savings"],
            datasets: [{
                data: [expenses, data.savings]
            }]
        }
    });
}
