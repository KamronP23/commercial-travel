import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';

function FrequentTravelGroupDetail() {
    const [group, setGroup] = useState({});
    const [clients, setClients] = useState([]);
    const [packages, setPackages] = useState([]);
    const { id } = useParams();
    const navigate = useNavigate();

    async function getGroup(group_id) {
        try {
            const url = `http://localhost:8000/friendly_agent/travel_groups/${group_id}/`;
            const response = await fetch(url)

            if (response.ok) {
                const data = await response.json();
                setGroup(data);
                setClients(data.clients || []);
                setPackages(data.packages || []);
            }
        } catch(error) {
            console.log("No Group Detected")
        }
    }

    useEffect(() => {
        getGroup(id);
    }, [id]);

    return (
        <div className="row">
          <div className="col-md-7 col-lg-3">
            <div className="card-body pt-0">
              <h4 className="card-title"><strong>Group Details</strong></h4>
              <p></p>
              <p className="card-text"><strong>Group Name: </strong>{group.group_name}</p>
              <p className="card-text"><strong>Clients:</strong></p>
                <ul>
                {clients.map((client) => (
                    <li key={client.id}>{client.first_name} {client.last_name}</li>
                ))}
                </ul>
                <p className="card-text"><strong>Packages:</strong></p>
                <ul>
                {packages.map((package1) => (
                    <li key={package1.id}>{package1.trip_name}</li>
                ))}
                </ul>
              <p className="card-text">
                <strong>Frequent Travel Group: </strong>
                {group.frequent_travel_group?.group_name ?? ''}
              </p>
              <button onClick={() => navigate('/packages')}>Back</button>
            </div>
          </div>
        </div>
      );
}

export default FrequentTravelGroupDetail;