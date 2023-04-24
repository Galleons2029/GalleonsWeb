
function hello() {
    const heading = document.querySelector('h1');
    if (heading.innerHTML === 'Hello!') {
        heading.innerHTML = 'Goodbye!';
    } else {
        heading.innerHTML = 'Hello!';
    }
}

if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count() {
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;
    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count;

    //setInterval(count, 1000);

    document.querySelector('form').onsubmit = function () {
        const name = document.querySelector('#name').value;
        alert(`Hello, ${name}!`)
    };

    // Change font color
    document.querySelectorAll('.color-button').forEach(buttton => {
        buttton.onclick = function () {
            document.querySelector('#hello').style.color = buttton.dataset.color;
        }
    })

    document.querySelector('select').onchange = function () {
        document.querySelector('#hello').style.color = this.value;
    }
});






