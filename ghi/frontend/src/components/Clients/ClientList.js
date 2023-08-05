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
    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Middle Name</th>
                    <th>Last Name</th>
                    <th>DOB</th>
                    <th>Email</th>
                    <th>Street</th>
                    <th>City</th>
                    <th>State</th>
                    <th>Zip code</th>
                    <th>Home</th>
                    <th>Cell</th>
                    <th>Travel Group</th>
                </tr>
            </thead>
            <tbody>
                {clients.map(client => {
                    return (
                        <tr key={client.id}>
                            <td>{ client.first_name }</td>
                            <td>{ client.middle_name }</td>
                            <td>{ client.last_name }</td>
                            <td>{ client.dob }</td>
                            <td>{ client.email }</td>
                            <td>{ client.street }</td>
                            <td>{ client.city }</td>
                            <td>{ client.state }</td>
                            <td>{ client.zipcode }</td>
                            <td>{ client.home_phone }</td>
                            <td>{ client.cell_phone }</td>
                            <td>{ client.frequent_travel_group.group_name }</td>
                        </tr>
                    )
                })}
            </tbody>
        </table>
    )
}

export default ClientList