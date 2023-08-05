import React, { useState, useEffect } from 'react';

function ClientList(){

    const [clients, setClients] = useState([])

    const getClients = async () => {
        const url = 'http://localhost:8000/friendly_agent/clients/'
        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            const clients = data.clients;
            setClients(clients);
            console.log(clients)
        }}
    useEffect(() => {
        getClients();
    }, [])
    return (<p> Hello World! </p> )
}

export default ClientList