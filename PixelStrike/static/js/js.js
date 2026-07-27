//alertas
const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const appendAlert = (message, type) => {
    const wrapper = document.createElement('div')
    wrapper.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${message}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
        '</div>'
    ].join('')

    alertPlaceholder.append(wrapper)
}

const alertTrigger = document.getElementById('liveAlertBtn')
if (alertTrigger) {
    alertTrigger.addEventListener('click', () => {
        appendAlert('Oh no! no hay nada mas aquí', 'danger')
    })
}

// Modo oscuro

function togglemodoscuro() {
    document.body.classList.toggle('modo-oscuro');
    guardapreferencia();
}

function guardapreferencia() {
    const esoscuro = document.body.classList.contains('modo-oscuro');
    localStorage.setItem('modoOscuro', esoscuro);
}

function cargapreferencia() {
    const savedMode = localStorage.getItem('modoOscuro');
    
    if (savedMode === 'true') {
        document.body.classList.add('modo-oscuro');
    } else if (savedMode === 'false') {
        document.body.classList.remove('modo-oscuro');
    } else {
    
        const prefiereoscuro = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (prefiereoscuro) {
            document.body.classList.add('modo-oscuro');
            localStorage.setItem('modoOscuro', 'true');
        }
    }
}

function miraeltema() {
    const darkModeMediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    
    darkModeMediaQuery.addEventListener('change', (e) => {
        if (localStorage.getItem('modoOscuro') === null) {
            if (e.matches) {
                document.body.classList.add('modo-oscuro');
            } else {
                document.body.classList.remove('modo-oscuro');
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    cargapreferencia();
    miraeltema();
});