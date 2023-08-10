import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';

function ClientDetail() {
    const [client, setClient] = useState({});
    const { id } = useParams();
    const navigate = useNavigate();
    async function getClient(client_id) {
      try {
        const url = `http://localhost:8000/friendly_agent/clients/${client_id}/`;
        const response = await fetch(url);

        if (response.ok) {
          const data = await response.json();
          setClient(data);
        }
      } catch (error) {
        console.log("No Client Detected");
      }
    }

    useEffect(() => {
      getClient(id);
    }, [id]);

    return (
        <div className="row">
            <div className="col-md-7 col-lg-3">
                <div className="card-body pt-0">
                    <h4 className="card-title"><strong>Client Details</strong></h4>
                    <p></p>
                    <p className="card-text"><strong>First Name: </strong>{client.first_name}</p>
                    <p className="card-text"><strong>Middle Name: </strong>{client.middle_name}</p>
                    <p className="card-text"><strong>Last Name: </strong>{client.last_name}</p>
                    <p className="card-text"><strong>DOB: </strong>{client.dob}</p>
                    <p className="card-text"><strong>Email: </strong>{client.email}</p>
                    <p className="card-text"><strong>Street: </strong>{client.street}</p>
                    <p className="card-text"><strong>City: </strong>{client.city}</p>
                    <p className="card-text"><strong>State: </strong>{client.state}</p>
                    <p className="card-text"><strong>Zip Code: </strong>{client.zipcode}</p>
                    <p className="card-text"><strong>Home Phone: </strong>{client.home_phone}</p>
                    <p className="card-text"><strong>Cell Phone: </strong>{client.cell_phone}</p>
                    <p className="card-text">
                        <strong>Frequent Travel Group: </strong>
                        {client.frequent_travel_group?.group_name ?? ''}
                    </p>
                    <button onClick={() => navigate('/clients')}>Back</button>
                </div>
            </div>


        </div>
    )
}

export default ClientDetail;