async function sendQuery() {
    let q = document.getElementById("query").value;

    let res = await fetch("http://127.0.0.1:8000/query?q=" + q, {
        method: "POST"
    });

    let data = await res.json();

    document.getElementById("response").innerText = data.response;
}
