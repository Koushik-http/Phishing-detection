document.getElementById('check-url').addEventListener('click', async () => {
    const url = document.getElementById('url-input').value;
    const response = await fetch('http://127.0.0.1:5000/check-url', {  // Updated URL
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
    });
    
    const data = await response.json();
    document.getElementById('result').innerText = data.message;
    if (data.message=="This URL seems to be safe."){
        setTimeout(()=>{
            window.open(url)
        },2000)
    }
});
