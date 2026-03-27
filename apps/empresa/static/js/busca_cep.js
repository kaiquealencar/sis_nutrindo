// empresa/static/js/busca_cep.js
document.addEventListener('DOMContentLoaded', function() {
    const cepInput = document.getElementById('cep');
    
    function buscarEndereco() {
        const cep = cepInput.value.replace(/\D/g, '');
        var logradouroInput = document.getElementById('logradouro');
        var bairroInput = document.getElementById('bairro');
        var cidadeInput = document.getElementById('cidade');
        var estadoInput = document.getElementById('estado');

        if (cep.length === 8) {
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    if (!data.erro) {
                        logradouroInput.value = data.logradouro || '';
                        bairroInput.value = data.bairro || '';
                        cidadeInput.value = data.localidade || '';
                        estadoInput.value = data.uf || '';

                        logradouroInput.readOnly = true;
                        bairroInput.readOnly = true;
                        cidadeInput.readOnly = true;
                        estadoInput.readOnly = true;
                        
                        logradouroInput.style.backgroundColor = '#e9ecef';
                        bairroInput.style.backgroundColor = '#e9ecef';
                        cidadeInput.style.backgroundColor = '#e9ecef';
                        estadoInput.style.backgroundColor = '#e9ecef';


                        document.getElementById('numero').focus();
                    } else {
                        alert('CEP não encontrado.');
                    }
                })
                .catch(error => console.error('Erro ao buscar CEP:', error));
        }
    }

    // Chama ao sair do campo CEP
    cepInput.addEventListener('blur', buscarEndereco);

    // Opcional: busca ao apertar Enter no campo CEP
    cepInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            buscarEndereco();
        }
    });
});