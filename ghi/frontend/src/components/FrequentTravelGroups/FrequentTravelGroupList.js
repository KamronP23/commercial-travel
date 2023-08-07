import React, { useState, useEffect } from 'react';


function FrequentTravelGroupList() {
    const [groups, setGroups] = useState([]);
    const [clients, setClients] = useState([]);

    const getGroups = async () => {
        const url = 'http://localhost:8000/friendly_agent/travel_groups/';
        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            const groups = data.frequent_travel_groups;
            setGroups(groups);
            console.log(groups);
        }
    }
    const getClients = async () => {
        const url = 'http://localhost:8000/friendly_agent/clients/';
        const response = await fetch(url);

        if (response.ok) {
          const data = await response.json();
          const clients = data.clients;
          setClients(clients);
          console.log(clients);
        }
      };

    useEffect(() => {
        getGroups();
        getClients();
    }, []);

    const sortedGroups = [...groups].sort((a, b) => a.group_name.localeCompare(b.group_name));
    return (
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Group Name</th>
                    <th>Number of Members</th>
                </tr>
            </thead>
            <tbody>
            {sortedGroups.map((group) => {
            const groupCount = clients.filter(client => client.frequent_travel_group.id === group.id).length;
            return (
                <tr key={group.id}>
                <td>{group.group_name}</td>
                <td>{groupCount}</td>
                </tr>
                    )
                })}
            </tbody>
        </table>


        )
    };

export default FrequentTravelGroupList;
