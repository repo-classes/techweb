function validar(cpf) {
    cpf = cpf.replace(/\D/g, ''); // Remove non-digit characters
    if (cpf.length !== 11 || /^(\d)\1{10}$/.test(cpf)) return false; // Invalid sequence

    let soma = 0;
    for (let i = 0; i < 9; i++) soma += parseInt(cpf[i]) * (10 - i);
    let digito1 = (soma * 10) % 11;
    digito1 = digito1 >= 10 ? 0 : digito1;

    if (parseInt(cpf[9]) !== digito1) return false;

    soma = 0;
    for (let i = 0; i < 10; i++) soma += parseInt(cpf[i]) * (11 - i);
    let digito2 = (soma * 10) % 11;
    digito2 = digito2 >= 10 ? 0 : digito2;

    return parseInt(cpf[10]) === digito2;
}

export async function onRequestGet({ request }) {
    const url = new URL(request.url);
    const cpf = url.searchParams.get('cpf');
    
    if (!cpf) {
        return new Response(JSON.stringify({ erro: 'CPF not provided' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' }
        });
    }

    const valido = validar(cpf);
    return new Response(JSON.stringify({ valido }), {
        headers: { 'Content-Type': 'application/json' }
    });
}

export async function onRequest({ request }) {
    const url = new URL(request.url);
    const cpf = url.searchParams.get('cpf');
    
    if (!cpf) {
        return new Response(JSON.stringify({ erro: 'CPF not provided' }), {
            status: 400,
            headers: { 'Content-Type': 'application/json' }
        });
    }

    const valido = validar(cpf);
    return new Response(JSON.stringify({ valido }), {
        headers: { 'Content-Type': 'application/json' }
    });
}